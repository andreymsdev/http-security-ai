# Analisador de Cabeçalhos de Segurança HTTP com IA

![Pygirl](https://i.pinimg.com/736x/e2/c8/21/e2c82120a3111d153a81596f4b3e71f2.jpg)

Este projeto realiza a análise de cabeçalhos HTTP de sites utilizando modelos de linguagem (LLMs) via OpenAI ou OpenRouter. Ele identifica falhas de segurança, recomenda melhorias e gera relatórios detalhados com base nas melhores práticas da web.

---

## Funcionalidades

* Varredura HTTP: Busca cabeçalhos de qualquer URL instantaneamente.
* Análise Inteligente: Avaliação completa via IA (DeepSeek, GPT, etc).
* Score de Segurança: Pontuação de 0 a 100 baseada em riscos detectados.
* Checklist de Melhorias: Identifica cabeçalhos ausentes e recomenda correções.
* Exportação: Gera relatórios detalhados em formato .json.

## Tecnologias Utilizadas

* Linguagem: Python 3.10+
* Requisições: [Requests](https://docs.python-requests.org/)
* IA: [OpenAI SDK](https://platform.openai.com/docs/)
* Provedor: OpenRouter (Modelos flexíveis)

---

## Instalacao

1. Clone o repositorio:
   ```bash
   git clone [https://github.com/seu-usuario/analisador-cabecalhos.git](https://github.com/seu-usuario/analisador-cabecalhos.git)
   cd analisador-cabecalhos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/analisador-cabecalhos.git](https://github.com/seu-usuario/analisador-cabecalhos.git)
    cd analisador-cabecalhos
    ```

2.  **Instale as dependências:**
    ```bash
    pip install requests openai
    ```

3.  **Configure sua API Key:**
    ```bash
    # Linux/Mac
    export OPENROUTER_API_KEY='sua-chave-aqui'
    
    # Windows (PowerShell)
    $env:OPENROUTER_API_KEY='sua-chave-aqui'
    ```

## Como usar

```bash
# Análise simples de uma URL
python http_security_headers.py --api-key sk-sua-chave http://exemplo.com

# Análise de múltiplas URLs
python http_security_headers.py --api-key sk-sua-chave exemplo.com google.com github.com

# Exportar resultado para JSON
python http_security_headers.py --api-key sk-sua-chave http://exemplo.com --exportar resultado.json

# Teste com DVWA (Metasploitable)
python http_security_headers.py --api-key sk-sua-chave http://192.168.186.129/dvwa/index.php

```

# Observações:

Este projeto faz parte dos meus estudos em Ethical Hacking. O objetivo principal é:

- Entender como os cabeçalhos HTTP influenciam a segurança de aplicações web.

- Automatizar a identificação de vulnerabilidades (XSS, Clickjacking, etc).

- Aplicar Inteligência Artificial para gerar relatórios técnicos acionáveis.
