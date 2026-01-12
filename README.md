# *Analisador de Cabeçalhos de Segurança HTTP com IA*

![Pygirl](https://i.pinimg.com/736x/e2/c8/21/e2c82120a3111d153a81596f4b3e71f2.jpg)

Este projeto realiza a análise de cabeçalhos HTTP de sites utilizando modelos de linguagem (LLMs) como o OpenAI ou OpenRouter. Ele identifica falhas de segurança, recomenda melhorias e gera relatórios detalhados com base nas melhores práticas da web.

## Funcionalidades

<pre><div><span><span>-</span></span><span></span><span>Busca </span><span>cabeçalhos </span><span>HTTP </span><span>de </span><span>qualquer </span><span>URL
</span><span><span>-</span></span><span></span><span>Analisa </span><span>os </span><span>cabeçalhos </span><span>com </span><span>IA </span><span>e </span><span>gera </span><span>relatório </span><span>completo
</span><span><span>-</span></span><span></span><span>Pontuação </span><span>de </span><span>segurança </span><span>(0–100)
</span><span><span>-</span></span><span></span><span>Identificação </span><span>de </span><span>cabeçalhos </span><span>ausentes </span><span>ou </span><span>mal </span><span>configurados
</span><span><span>-</span></span><span></span><span>Recomendações </span><span>práticas </span><span>de </span><span>segurança
</span><span><span>-</span></span><span></span><span>Exportação </span><span>dos </span><span>resultados </span><span>em </span><span>JSON</span></div></pre>

## Tecnologias Utilizadas

<pre><div><span><span>-</span></span><span></span><span>Python </span><span>3.10+
</span><span><span>-</span></span><span></span><span>[</span><span><span>Requests</span></span><span>](</span><span><span>https://docs.python-requests.org/</span></span><span>)
</span><span><span>-</span></span><span></span><span>[</span><span><span>OpenAI SDK</span></span><span>](</span><span><span>https://platform.openai.com/docs/</span></span><span>)
</span><span><span>-</span></span><span></span><span>Modelos </span><span>LLM </span><span>via </span><span>OpenRouter </span><span>ou </span><span>OpenAI
</span><span><span>-</span></span><span></span><span>Terminal </span><span>com </span><span>argparse
</span></div></pre>

# **Instalação**

<pre><div><span><span>1.</span></span><span></span><span>Clone </span><span>o </span><span>repositório:
   </span><span><span>```bash
   git clone https://github.com/seu-usuario/analisador-cabecalhos.git
   cd analisador-cabecalhos</span></span></div></pre>

## Instale as dependências:

pip install -r requirements.txt

Configure sua API:

export OPENROUTER_API_KEY=sk-sua-chave-aqui

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

Este projeto faz parte dos meus estudos em **ethical hacking**. A ideia é aprender na prática como os cabeçalhos HTTP influenciam a segurança de aplicações web, identificar vulnerabilidades e aplicar inteligência artificial para gerar relatórios automatizados.

