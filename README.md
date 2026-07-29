# Python e Gemini: Orquestrando LLMs com LangChain

## 📌 Sobre o projeto

Este projeto utiliza o **LangChain** como framework principal para orquestrar uma solução integrada de análise e organização de imagens enriquecidas com anotações inteligentes. O LangChain foi escolhido por sua capacidade de conectar e gerenciar fluxos complexos que combinam IA multimodal e modelos de linguagem, permitindo um desenvolvimento mais modular e escalável.

O projeto expõe um **assistente via terminal**, orquestrado por um agente central que decide, a partir da pergunta do usuário, se deve responder diretamente ou acionar ferramentas (como análise de imagens).

![Demonstração do projeto](img/amostra.gif)

## 🔨 Funcionalidades

- Assistente conversacional via linha de comando
- Análise de imagens com IA multimodal (ex: `"Faça uma análise da imagem exemplo_grafico.jpg"`)
- Respostas diretas a perguntas gerais via cadeias simples (ex: `"Explique o que são desvios condicionais"`)
- Orquestração de agente com múltiplas ferramentas (Agente como Ferramentas)
- Suporte a múltiplos provedores de LLM: **Google Gemini** e **Maritaca AI**

## ✔️ Técnicas e tecnologias utilizadas

- Programação em **Python**
- **API Gemini** (Google) e **API Maritaca**
- Framework **LangChain**
  - Cadeias Simples
  - Agente Orquestrador
  - Agente como Ferramentas
- **Pillow** para manipulação de imagens
- **python-dotenv** para gerenciamento de variáveis de ambiente

## 📂 Estrutura do projeto

```
LLM-LangChain/
├── agente/            # Lógica do agente orquestrador
├── ferramentas/        # Ferramentas (tools) utilizadas pelo agente, ex: análise de imagem
├── imagem/              # Módulos relacionados ao processamento de imagens
├── langchain/           # Configurações e cadeias do LangChain
├── testes/               # Testes do projeto
├── img/                    # Imagens de exemplo e demonstração (ex: amostra.gif)
├── main.py                 # Ponto de entrada — assistente via terminal
├── my_helper.py             # Funções auxiliares
├── my_keys.py                # Carregamento das API keys a partir do .env
├── my_models.py               # Identificadores dos modelos utilizados (Gemini/Maritaca)
├── requirements.txt            # Dependências do projeto
└── .gitignore
```

## 🛠️ Como abrir e rodar o projeto

Após baixar o projeto, você pode abri-lo com o Visual Studio Code. Em seguida, é necessário preparar o ambiente.

### 1. Criar e ativar o ambiente virtual

**Windows:**
```bash
python -m venv venv-gemini-3
venv-gemini-3\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv-gemini-3
source venv-gemini-3/bin/activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 🔑 Gerar API_KEY e associar ao .env

Crie um arquivo `.env` na raiz do projeto com suas chaves de API:

```env
GEMINI_API_KEY="SUA_CHAVE_AQUI"
MARITACA_API_KEY="SUA_CHAVE_AQUI"
```

As chaves são carregadas automaticamente pelo `my_keys.py` através do `python-dotenv`.

> ⚠️ Nunca compartilhe suas chaves de API publicamente. Certifique-se de que o arquivo `.env` está listado no `.gitignore`.

## ▶️ Executando o projeto

```bash
python main.py
```

Isso inicia o assistente em modo interativo no terminal:

```
=== Assistente IA ===
Exemplos:
 - Explique o que são desvios condicionais
 - Faça uma análise da imagem exemplo_grafico.jpg

Digite 'sair' para encerrar.
```

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
