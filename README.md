# ETL - Análise de Dados da Netflix

## Visão Geral
Este projeto de ETL (“Extract, Transform, Load”) foi criado para praticar conceitos de Engenharia de Dados, utilizando [dados da Netflix disponíveis no Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows). O objetivo é realizar o carregamento e transformação desses dados, armazená-los em um banco de dados relacional e realizar análises exploratórias para gerar insights.

## Fluxo do Projeto
1. Extração:
- Os dados foram obtidos diretamente do arquivo netflix_titles.csv, fornecido pelo Kaggle.

2. Transformação:
- Remoção de dados nulos.
- Eliminação de duplicatas.

3. Carregamento:
- Os dados foram armazenados em um banco de dados MySQL.

4. Análise e Visualização:
- Consultas SQL foram realizadas para gerar insights.
- Gráficos foram criados usando Python e bibliotecas como Matplotlib e Seaborn.

## Tecnologias Utilizadas
- Linguagens: Python, SQL
- Banco de Dados: MySQL

## Estrutura do Projeto
```plaintext
etl-project/
├── data/                     # Contém os arquivos CSV
├── scripts/                  # Contém os scripts Python e SQL
│   ├── extract.py            # Extração dos dados
│   ├── transform.py          # Limpeza e transformação
│   ├── load.py               # Carregamento no banco de dados
│   ├── queries.py            # Conexão e execução de consultas
│   ├── queries.sql           # Arquivo com as queries SQL
├── notebooks/                # Jupyter Notebooks para análise
│   ├── data_analysis.ipynb   # Notebook de análise exploratória
├── README.md                 # Documentação do projeto
```