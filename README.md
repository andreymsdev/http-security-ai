# *Analisador de Cabeçalhos de Segurança HTTP com IA*

![pygirl](fotos/pygirl.jpg)

<pre><div><span></span><span>Este </span><span>projeto </span><span>realiza </span><span>a </span><span>análise </span><span>de </span><span>cabeçalhos </span><span>HTTP </span><span>de </span><span>sites </span><span>utilizando </span><span>modelos </span><span>de </span><span>linguagem </span><span>(LLMs) </span><span>como </span><span>o </span><span>OpenAI </span><span>ou </span><span>OpenRouter. </span><span>Ele </span><span>identifica </span><span>falhas </span><span>de </span><span>segurança, </span><span>recomenda </span><span>melhorias </span><span>e </span><span>gera </span><span>relatórios </span><span>detalhados </span><span>com </span><span>base </span><span>nas </span><span>melhores </span><span>práticas </span><span>da </span><span>web.</span></div></pre>

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

<pre><div><span>Este </span><span>projeto </span><span>faz </span><span>parte </span><span>dos </span><span>meus </span><span>estudos </span><span>em </span><span><span>**ethical hacking**. </span><span>A </span><span>ideia </span><span>é </span><span>aprender </span><span>na </span><span>prática </span><span>como </span><span>os </span><span>cabeçalhos </span><span>HTTP </span><span>influenciam </span><span>a </span><span>segurança </span><span>de </span><span>aplicações </span><span>web, </span><span>identificar </span><span>vulnerabilidades </span><span>e </span><span>aplicar </span><span>inteligência </span><span>artificial </span><span>para </span><span>gerar </span><span>relatórios </span><span>automatizados.</span></div></pre>

⚠️ **Aprender Hacking é lindo mas sempre com consciência**, e**studar hacking é sobre proteger, não invadir.** Use apenas em ambientes controlados ou com permissão explícita.

 E lembre-se "*você pode enganar todo o mundo por quase todo tempo, quase todo mundo por todo tempo, mas você não pode enganar todo mundo por todo tempo".*
