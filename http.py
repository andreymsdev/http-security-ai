# Bibliotecas para requisições, JSON, sistema e IA
import requests  
import json      
import os        
import argparse  
from typing import Dict, List, Tuple
from openai import OpenAI  

# Organiza a lógica de análise de segurança
class AnalisadorCabecalhosSeguranca:
    def __init__(self, chave_api: str = None, url_base: str = None, modelo: str = None):
        # Configura as chaves de acesso e o modelo de IA
        self.chave_api = chave_api or os.getenv('OPENROUTER_API_KEY') or os.getenv('OPENAI_API_KEY')
        self.url_base = url_base or os.getenv('OPENROUTER_BASE_URL', "https://openrouter.ai/api/v1")
        self.modelo = modelo or os.getenv('LLM_MODEL', 'deepseek/deepseek-chat-v3.1:free')
        
        # Garante que a API Key exista para o código não travar depois
        if not self.chave_api:
            raise ValueError("A chave da API é obrigatória.")
        
        # Inicializa o cliente para conversar com a IA
        self.cliente = OpenAI(base_url=self.url_base, api_key=self.chave_api)

    def buscar_cabecalhos(self, url: str, tempo_limite: int = 10) -> Tuple[Dict[str, str], int]:
        # Corrige a URL caso o usuário não digite o protocolo
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        try:
            # Tenta obter os cabeçalhos HTTP do site
            resposta = requests.get(url, timeout=tempo_limite, allow_redirects=True)
            return dict(resposta.headers), resposta.status_code
        except requests.exceptions.RequestException as erro:
            print(f"Erro ao buscar {url}: {erro}")
            return {}, 0

    def analisar_cabecalhos(self, url: str, cabecalhos: Dict[str, str], status: int) -> str:
        # Prepara a instrução para a IA analisar os dados recebidos
        prompt = f"""Analise os cabeçalhos de segurança para {url} (Status: {status}):
{json.dumps(cabecalhos, indent=2)}
Forneça nota, problemas críticos, o que falta e recomendações. Sem usar markdown excessivo."""

        try:
            # Envia para a IA e retorna o texto da análise
            resposta = self.cliente.chat.completions.create(
                model=self.modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            return resposta.choices[0].message.content
        except Exception as erro:
            return f"Falha na análise: {erro}"

    def analisar_url(self, url: str, tempo_limite: int = 10) -> Dict:
        # Orquestra a busca e a análise de uma URL específica
        cabecalhos, status = self.buscar_cabecalhos(url, tempo_limite)
        if not cabecalhos:
            return {"url": url, "erro": "Falha ao buscar"}

        print(f"Código de status: {status}")
        analise = self.analisar_cabecalhos(url, cabecalhos, status)
        print(analise)

        # Retorna um dicionário com os dados consolidados
        return {
            "url": url,
            "codigo_status": status,
            "analise": analise,
            "cabecalhos_brutos": cabecalhos
        }

    def analisar_varias_urls(self, lista_urls: List[str], tempo_limite: int = 10) -> List[Dict]:
        # Loop para processar múltiplos sites em sequência
        return [self.analisar_url(url, tempo_limite) for url in lista_urls]

    def exportar_resultados(self, resultados: List[Dict], nome_arquivo: str):
        # Salva a lista de resultados em um arquivo JSON formatado
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, indent=2, ensure_ascii=False)

def principal():
    # Gerencia os argumentos passados via terminal (linha de comando)
    parser = argparse.ArgumentParser(description='Analisador de Cabeçalhos com IA')
    parser.add_argument('urls', nargs='+', help='URLs para analisar')
    parser.add_argument('--exportar', help='Nome do arquivo para salvar os resultados')
    
    args = parser.parse_args()

    try:
        # Instancia a classe e executa a lógica principal
        analisador = AnalisadorCabecalhosSeguranca()
        resultados = analisador.analisar_varias_urls(args.urls)

        # Se houver o argumento --exportar, salva o arquivo
        if args.exportar:
            analisador.exportar_resultados(resultados, args.exportar)

    except Exception as e:
        print(f"Erro: {e}")

# Inicia o script
if __name__ == '__main__':
    principal()
