🏥 Sistema Preditivo de Obesidade

Este projeto tem como objetivo desenvolver um sistema de Machine Learning capaz de auxiliar profissionais da saúde no diagnóstico do nível de obesidade de pacientes, utilizando dados clínicos e comportamentais.

O sistema foi desenvolvido como parte do Tech Challenge – Fase 4 – Data Analytics (FIAP).


📊 Problema de Negócio

A obesidade é uma condição multifatorial influenciada por fatores genéticos, hábitos alimentares e estilo de vida.
Este projeto visa fornecer uma solução preditiva que permita identificar o nível de obesidade de um paciente de forma rápida e confiável, apoiando a tomada de decisão clínica.

🧠 Solução Proposta

Foi desenvolvido um modelo de Machine Learning utilizando o algoritmo RandomForestClassifier, capaz de prever 7 níveis diferentes de obesidade a partir de informações como:

Idade
Altura e peso (com cálculo automático de IMC)
Frequência de atividade física
Hábitos alimentares
Consumo de água e álcool
Tempo de uso de dispositivos eletrônicos
Meio de transporte utilizado
O modelo foi integrado a uma aplicação web desenvolvida em Streamlit.

⚙️ Pipeline de Machine Learning

Tratamento e padronização dos dados
Criação da feature IMC (Índice de Massa Corporal)
Separação de variáveis numéricas e categóricas
Pré-processamento com ColumnTransformer
Treinamento com RandomForestClassifier
Avaliação de desempenho (acurácia > 75%)
Salvamento do modelo para deploy

🖥️ Aplicação Streamlit

A aplicação permite:
Inserir dados do paciente
Calcular automaticamente o IMC
Exibir a classificação clínica do IMC
Prever o nível de obesidade em português

📈 Dashboard Analítico

Além da aplicação preditiva, foi desenvolvido um dashboard analítico no Power BI contendo:
Total de pacientes
Percentual de pacientes com obesidade
Distribuição da obesidade por gênero
Distribuição por faixa etária
Relação entre obesidade e sedentarismo

📁 Estrutura do Projeto
├── app.py                     # Aplicação Streamlit
├── pipeline_obesity.pkl       # Modelo treinado
├── tratamento_dados_obesidade.ipynb
├── obesity_analise.csv        # Base tratada para o dashboard
├── Obesity.csv                # Base original
├── requirements.txt
└── README.md

▶️ Como Executar o Projeto
1️⃣ Instalar dependências
pip install -r requirements.txt

2️⃣ Executar a aplicação
streamlit run app.py

🧪 Tecnologias Utilizadas

Python
Pandas / NumPy
Scikit-learn
Streamlit
Power BI

👨‍🎓 Autor
Mateus Maia
