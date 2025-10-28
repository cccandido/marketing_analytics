# 📊 Análise de Performance em Campanhas de Marketing Digital  

**Autora:** [Camila Candido](https://cccandido.github.io/portfolio_projetos/#)  
**Tecnologias:** Python • Streamlit • Pandas • Plotly • Scikit-Learn • SQL (PostgreSQL)  

---

## 🎯 Objetivo

Este projeto tem como objetivo desenvolver uma aplicação interativa para **analisar e prever a performance de campanhas de marketing digital**, simulando o contexto de uma consultoria de dados.  

A proposta é entender **quais canais de divulgação trazem mais retorno**, **avaliar a eficiência dos investimentos** e **identificar oportunidades de otimização** com base em dados reais de desempenho.  

---

## ⚙️ Processo de Desenvolvimento  

### 1️⃣ Modelagem e Construção da Base de Dados  
- Criação de três tabelas principais:
  - `campanhas`: informações sobre cada canal e seu orçamento.  
  - `resultados`: métricas de desempenho (cliques, leads, receita, etc).  
  - `clientes`: perfis simulados (idade e renda).  
- Criação de uma **view analítica (`vw_analise_marketing`)** para consolidar os dados e gerar métricas:
  - CTR (*Click Through Rate*)  
  - Taxa de Conversão  
  - ROI (*Return on Investment*)  
  - Lucro estimado  
  - Perfil médio do público  

---

### 2️⃣ Análise Descritiva  
Implementada em **Streamlit**, a primeira aba do dashboard traz:

- **Indicadores gerais**: ROI, CTR, Taxa de Conversão, Leads e Investimento Total.  
- **Evolução temporal**: linha mostrando gasto e lucro ao longo dos meses.  
- **Eficiência por canal**: gráfico combinando investimento (barras) e geração de leads (linha).  
- **Perfil do público**: distribuição de idade e renda média dos clientes simulados.

💬 *Insight principal:*  
Mesmo com aumento de investimento, o retorno financeiro começou a cair — sinalizando **ineficiência em alguns canais** e **oportunidade de redistribuição orçamentária**.

---

### 3️⃣ Análise Preditiva  
Na segunda aba, foi aplicada **regressão linear simples** com `scikit-learn` para investigar relações entre variáveis:

- **Gasto vs Leads:** mostra que investir mais nem sempre significa gerar mais leads.  
- **Cliques vs Leads:** revela uma correlação forte, indicando que **o engajamento (CTR)** é o principal impulsionador de conversões.

💬 *Insight principal:*  
> “O modelo mostra que o aumento de leads está mais ligado à qualidade do engajamento do público do que ao volume de investimento.”

---

### 4️⃣ Storytelling e Recomendações  

> - **Revisar a alocação de investimento** entre canais, priorizando os mais eficientes.  
> - **Focar em públicos mais jovens**, onde há maior ROI e engajamento.  
> - **Explorar novos criativos e segmentações** para canais de baixo desempenho.  
> - **Monitorar continuamente CTR, conversão e ROI** para otimizar a performance.  
> - **Aprofundar modelos preditivos** com variáveis como tipo de campanha, região e sazonalidade.

---

## 💡 Principais Aprendizados  

- Integração entre **SQL e Python** para criação de *views analíticas*.  
- Construção de **dashboards interativos e narrativos** com Streamlit.  
- Interpretação de métricas de marketing: CTR, conversão, ROI, engajamento.  
- Aplicação prática de **regressão linear** e análise de correlação.  
- Importância do **storytelling e design de dados** na apresentação de insights.  

---

## 📸 Preview  

![Preview do Dashboard](images/preview_dashboard.png)

---

## 🚀 Como Executar Localmente  

bash
# Clonar o repositório
git clone https://github.com/cccandido/marketing_analytics_streamlit.git
cd marketing_analytics_streamlit

# Instalar dependências
pip install -r requirements.txt

# Executar o app
streamlit run app.py

---

## 📦 Estrutura do Projeto

📁 marketing_analytics_streamlit/
│
├── app.py                      # código principal do Streamlit
├── requirements.txt            # dependências do projeto
├── data/
│   └── base_marketing.csv      # base exportada do SQL (simulada)
├── queries/
│   └── vw_analise_marketing.sql  # view SQL usada na modelagem
├── images/
│   └── preview_dashboard.png   # print do dashboard
└── .streamlit/
    └── config.toml             # tema visual

---

## 🧩 Próximos Passos

Adicionar métricas financeiras complementares.

Conectar a um banco PostgreSQL real para automação.

Ampliar a modelagem preditiva com mais variáveis explicativas.

