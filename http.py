# Bibliotecas essenciais
import requests  # Faz requisições HTTP para obter os cabeçalhos dos sites
import json      # Manipula dados em formato JSON para exportação e análise
import os        # Acessa variáveis de ambiente como chaves de API
import argparse  # Lida com argumentos de linha de comando
from typing import Dict, List, Tuple
from openai import OpenAI  # Cliente para interagir com modelos de linguagem

# Classe principal para análise de cabeçalhos de segurança
class AnalisadorCabecalhosSeguranca:
    def __init__(self, chave_api: str = None, url_base: str = None, modelo: str = None):
        self.chave_api = chave_api or os.getenv('OPENROUTER_API_KEY') or os.getenv('OPENAI_API_KEY')
        self.url_base = url_base or os.getenv('OPENROUTER_BASE_URL', "https://openrouter.ai/api/v1")
        self.modelo = modelo or os.getenv('LLM_MODEL', 'deepseek/deepseek-chat-v3.1:free')
        if not self.chave_api:
            raise ValueError("A chave da API é obrigatória. Defina OPENROUTER_API_KEY ou use --api-key")
        self.cliente = OpenAI(base_url=self.url_base, api_key=self.chave_api)

    def buscar_cabecalhos(self, url: str, tempo_limite: int = 10) -> Tuple[Dict[str, str], int]:
        """Busca os cabeçalhos HTTP de uma URL"""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        try:
            resposta = requests.get(url, timeout=tempo_limite, allow_redirects=True)
            return dict(resposta.headers), resposta.status_code
        except requests.exceptions.RequestException as erro:
            print(f"Erro ao buscar {url}: {erro}")
            return {}, 0

    def analisar_cabecalhos(self, url: str, cabecalhos: Dict[str, str], status: int) -> str:
        """Analisa os cabeçalhos usando IA"""
        prompt = f"""Analise os cabeçalhos de segurança HTTP para o site {url} (Status: {status})
Cabeçalhos:
{json.dumps(cabecalhos, indent=2)}

Forneça uma análise de segurança completa incluindo:

1. Pontuação de segurança (de 0 a 100) e avaliação geral
2. Problemas críticos de segurança que exigem atenção imediata
3. Cabeçalhos importantes que estão ausentes
4. Análise dos cabeçalhos existentes e sua eficácia
5. Recomendações específicas para melhorias
6. Riscos potenciais com base na configuração atual

Foque em conselhos práticos e acionáveis, seguindo as melhores práticas atuais de segurança na web.
Por favor, não utilize ** ou # na resposta, exceto quando forem realmente necessários para referências específicas.
Use números, algarismos romanos ou letras para organizar o conteúdo. Formate a resposta de forma clara e bem estruturada."""

        try:
            resposta = self.cliente.chat.completions.create(
                model=self.modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            return resposta.choices[0].message.content
        except Exception as erro:
            return f"Falha na análise: {erro}"

    def analisar_url(self, url: str, tempo_limite: int = 10) -> Dict:
        """Analisa uma única URL"""
        print(f"\n🔍 Analisando: {url}")
        print("-" * 50)

        cabecalhos, status = self.buscar_cabecalhos(url, tempo_limite)
        if not cabecalhos:
            return {"url": url, "erro": "Falha ao buscar cabeçalhos"}

        print(f"Código de status: {status}")
        print(f"\nCabeçalhos HTTP ({len(cabecalhos)} encontrados):")
        print("-" * 30)
        for chave, valor in cabecalhos.items():
            print(f"{chave}: {valor}")

        print(f"\n🧠 Analisando com IA...")
        analise = self.analisar_cabecalhos(url, cabecalhos, status)

        print("\n🔐 ANÁLISE DE SEGURANÇA")
        print("=" * 50)
        print(analise)

        return {
            "url": url,
            "codigo_status": status,
            "quantidade_cabecalhos": len(cabecalhos),
            "analise": analise,
            "cabecalhos_brutos": cabecalhos
        }

    def analisar_varias_urls(self, lista_urls: List[str], tempo_limite: int = 10) -> List[Dict]:
        """Analisa várias URLs em sequência"""
        resultados = []
        for i, url in enumerate(lista_urls, 1):
            print(f"\n[{i}/{len(lista_urls)}]")
            resultado = self.analisar_url(url, tempo_limite)
            resultados.append(resultado)
        return resultados

    def exportar_resultados(self, resultados: List[Dict], nome_arquivo: str):
        """Exporta os resultados para um arquivo JSON"""
        with open(nome_arquivo, 'w') as f:
            json.dump(resultados, f, indent=2, ensure_ascii=False)
        print(f"\n📁 Resultados exportados para: {nome_arquivo}")

# Função principal que lida com argumentos de linha de comando
def principal():
    parser = argparse.ArgumentParser(
        description='🔍 Analisa cabeçalhos de segurança HTTP usando IA',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Exemplos:
  python cabecalhos_seg.py https://exemplo.com
  python cabecalhos_seg.py exemplo.com google.com
  python cabecalhos_seg.py exemplo.com --exportar resultados.json

Variáveis de ambiente:
  OPENROUTER_API_KEY - Chave da API do OpenRouter
  OPENAI_API_KEY - Chave da API do OpenAI
  LLM_MODEL - Modelo a ser usado (padrão: deepseek/deepseek-chat-v3.1:free)'''
    )

    parser.add_argument('urls', nargs='+', help='URLs para analisar')
    parser.add_argument('--api-key', help='Chave da API para o serviço de IA')
    parser.add_argument('--base-url', help='URL base da API de IA')
    parser.add_argument('--model', help='Modelo de IA a ser usado')
    parser.add_argument('--timeout', type=int, default=10, help='Tempo limite da requisição (padrão: 10s)')
    parser.add_argument('--exportar', help='Exporta os resultados para um arquivo JSON')

    args = parser.parse_args()

    try:
        analisador = AnalisadorCabecalhosSeguranca(
            chave_api=args.api_key,
            url_base=args.base_url,
            modelo=args.model
        )

        resultados = analisador.analisar_varias_urls(args.urls, args.timeout)

        if args.exportar:
            analisador.exportar_resultados(resultados, args.exportar)

    except ValueError as erro:
        print(f"❌ Erro: {erro}")
        return 1
    except KeyboardInterrupt:
        print("\n⛔ Análise interrompida pelo usuário")
        return 1

# Ponto de entrada do script
if __name__ == '__main__':
    principal()
