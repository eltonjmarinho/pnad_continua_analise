# Análise de Dados - PNAD Contínua (IBGE)

[![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)](#)
[![Linguagem](https://img.shields.io/badge/Linguagem-Python%20%7C%20R-blue)](#)

## 📌 Sobre o Projeto
Este repositório contém scripts e notebooks desenvolvidos para a extração, tratamento e análise de dados da **Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua)**, conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE). 

O objetivo principal deste projeto é explorar os microdados da pesquisa para extrair insights socioeconômicos sobre o mercado de trabalho, renda, educação e outras características da população brasileira.

## 🎯 Objetivos Específicos
* **Extração:** Coleta automatizada ou download estruturado dos microdados do portal do IBGE.
* **Tratamento:** Limpeza de dados, tratamento de valores nulos e aplicação dos dicionários de variáveis do IBGE.
* **Análise Exploratória (EDA):** Visualização de tendências em indicadores de desemprego, desigualdade de renda, etc.
* **Modelagem/Estatística:** (Se houver) Aplicação de modelos estatísticos ou de machine learning para prever ou agrupar características populacionais.

## 📂 Estrutura do Repositório

Sinta-se livre para adaptar esta estrutura à realidade do seu projeto:

```text
pnad_continua_analise/
│
├── data/
│   ├── raw/             # Microdados brutos baixados do IBGE (geralmente ignorados no git)
│   ├── processed/       # Dados limpos e prontos para análise
│   └── dicionarios/     # Dicionários de variáveis fornecidos pelo IBGE (.xls ou .csv)
│
├── notebooks/           # Jupyter Notebooks ou R Markdown com análises exploratórias
│   ├── 01_extracao.ipynb
│   ├── 02_limpeza_e_tratamento.ipynb
│   └── 03_analise_exploratoria.ipynb
│
├── src/                 # Scripts fonte (Python ou R) com funções auxiliares
│   ├── data_loader.py
│   └── utils.py
│
├── results/             # Gráficos, tabelas e relatórios gerados
│
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Linguagem:** Python 3.x (ou R)
* **Manipulação de Dados:** `pandas`, `numpy`
* **Visualização:** `matplotlib`, `seaborn`, `plotly`
* **Pacotes Específicos (opcional):** `PNADcIBGE` (se usando R), `geopandas` (para mapas).

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/eltonjmarinho/pnad_continua_analise.git
   cd pnad_continua_analise
   ```

2. **Crie um ambiente virtual (Recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Baixe os dados do IBGE:**
   * Siga as instruções no notebook `01_extracao.ipynb` ou coloque os arquivos CSV/TXT baixados do site do IBGE na pasta `data/raw/`.

5. **Execute os notebooks ou scripts:**
   * Inicie o Jupyter e abra os arquivos na pasta `notebooks/`.
   ```bash
   jupyter notebook
   ```

## 📊 Principais Resultados e Insights
*(Adicione aqui um breve resumo do que você descobriu com a sua análise. Ex: "Observou-se uma queda na taxa de desocupação no 3º trimestre do ano X, impulsionada pelo setor de serviços...")*

## ✍️ Autor
* **Elton J. Marinho** - [GitHub](https://github.com/eltonjmarinho)

## 📄 Licença
Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/) - veja o arquivo LICENSE para detalhes.
