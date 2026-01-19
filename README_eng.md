# AI-Powered HTTP Security Headers Analyzer

![Pygirl](https://i.pinimg.com/736x/e2/c8/21/e2c82120a3111d153a81596f4b3e71f2.jpg)

This project performs the analysis of HTTP security headers from websites using Large Language Models (LLMs) via OpenAI or OpenRouter. It identifies security flaws, recommends improvements, and generates detailed reports based on web security best practices.

---

## Features

* HTTP Scanning: Instantly fetches headers from any URL.
* Intelligent Analysis: Complete evaluation via AI (DeepSeek, GPT, etc).
* Security Score: 0 to 100 rating based on detected risks.
* Improvement Checklist: Identifies missing headers and recommends fixes.
* Export: Generates detailed reports in .json format.

## Technologies Used

* Language: Python 3.10+
* Requests: [Requests](https://docs.python-requests.org/)
* AI: [OpenAI SDK](https://platform.openai.com/docs/)
* Provider: OpenRouter (Flexible models)

---

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/analisador-cabecalhos.git](https://github.com/your-username/analisador-cabecalhos.git)
   cd analisador-cabecalhos

2. ```bash
   pip install requests openai

3.
```bash
# Linux/Mac
export OPENROUTER_API_KEY='your-key-here'

# Windows (PowerShell)
$env:OPENROUTER_API_KEY='your-key-here'

```

## Usage

```bash
# Simple analysis of a single URL
python http_security_headers.py --api-key sk-your-key [http://example.com](http://example.com)

# Multiple URL analysis
python http_security_headers.py --api-key sk-your-key example.com google.com github.com

# Export results to JSON
python http_security_headers.py --api-key sk-your-key [http://example.com](http://example.com) --exportar report.json

# Test with DVWA (Metasploitable)
python http_security_headers.py --api-key sk-your-key [http://192.168.186.129/dvwa/index.php](http://192.168.186.129/dvwa/index.php)
```

