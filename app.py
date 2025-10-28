# ============================================================
# 📊 APP STREAMLIT - ANÁLISE DE MARKETING
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import base64


# ======================================================
# CARREGAR DADOS
# ======================================================

# Caminho do arquivo CSV
CAMINHO_CSV = "view_base_marketing_analytics.csv"

@st.cache_data
def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, sep=";", encoding="utf-8")
    return df


df = carregar_dados()

# ============================================================
# CONFIGURAÇÕES INICIAIS DO APP
# ============================================================

st.set_page_config(page_title="Análise de Marketing", page_icon="📊", layout="wide")

# ============================================================
# CABEÇALHO ESTILIZADO
# ============================================================

with open("assets/marketing_icon.png", "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()

html_header = f"""
<div style="
    background: linear-gradient(135deg, #FFB84D 0%, #F27C00 100%);
    padding: 60px 20px;
    border-radius: 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 18px rgba(0,0,0,0.15);
    margin-bottom: 30px;
">
    <div style="
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 12px;
        padding: 30px 20px;
        max-width: 1300px;
        margin: auto;
    ">
        <img src="data:image/png;base64,{img_base64}" width="190" style="margin-bottom: 12px;">
        <h1 style="color: #FFFFFF; font-weight: 800; font-size: 38px; margin-bottom: 10px;">
            Análise de Performance em Campanhas de Marketing Digital
        </h1>
        <p style="color: #FFF8EE; font-size: 17px; max-width: 850px; margin: auto; line-height: 1.6;">
            Este relatório apresenta uma análise <b>descritiva</b> e <b>preditiva</b> baseada em indicadores simulados de campanhas digitais.<br>
            O objetivo é fornecer <b>insights estratégicos</b> para otimizar investimentos e identificar oportunidades de melhoria.
        </p>
    </div>
</div>
"""
st.markdown(html_header, unsafe_allow_html=True)

st.markdown("<hr style='border:0.8px solid #E5E5E5; margin: 25px 0;'>", unsafe_allow_html=True)

# ------------------------------------------------------------
# ABAS PRINCIPAIS
# ------------------------------------------------------------
aba1, aba2, aba3 = st.tabs(["📊 Análise Descritiva", "📉 Análise Preditiva", "🧭 Síntese e Recomendações"])

# ============================================================
# ABA 1 - ANÁLISE DESCRITIVA
# ============================================================
with aba1:
    st.markdown("<h3 style='text-align:center; color:#000000; font-weight:900;'>Análise descritiva das campanhas</h3>",
                unsafe_allow_html=True)

    # ============================================================
    # MÉTRICAS GERAIS - CARDS VISUAIS
    # ============================================================
    gasto_total = f"R$ {df['gasto'].sum():,.0f}".replace(",", ".")
    lucro_total = f"R$ {df['lucro'].sum():,.0f}".replace(",", ".")
    ctr_medio = f"{df['ctr'].mean():.2%}"
    leads_totais = f"{df['leads'].sum():,.0f}".replace(",", ".")
    taxa_conv = f"{df['taxa_conversao_calc'].mean():.2%}"
    roi_medio = f"{df['roi_calc'].mean():.2f}"

    st.markdown(f"""
    <div style='display:flex; justify-content:space-around; flex-wrap:wrap; margin-top:15px;'>
      <div style='background-color:#FFF6EB; padding:20px; border-radius:12px; width:15%; text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.08); margin:10px;'>
        <div style='font-size:24px;'>💰</div><div style='font-weight:600;'>Gasto Total</div><div style='font-size:22px; color:#F27C00;'>{gasto_total}</div>
      </div>
      <div style='background-color:#FFF6EB; padding:20px; border-radius:12px; width:15%; text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.08); margin:10px;'>
        <div style='font-size:24px;'>📈</div><div style='font-weight:600;'>Lucro Total</div><div style='font-size:22px; color:#F27C00;'>{lucro_total}</div>
      </div>
      <div style='background-color:#FFF6EB; padding:20px; border-radius:12px; width:15%; text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.08); margin:10px;'>
        <div style='font-size:24px;'>🎯</div><div style='font-weight:600;'>CTR Médio</div><div style='font-size:22px; color:#F27C00;'>{ctr_medio}</div>
      </div>
      <div style='background-color:#FFF6EB; padding:20px; border-radius:12px; width:15%; text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.08); margin:10px;'>
        <div style='font-size:24px;'>🔁</div><div style='font-weight:600;'>Conversão</div><div style='font-size:22px; color:#F27C00;'>{taxa_conv}</div>
      </div>
      <div style='background-color:#FFF6EB; padding:20px; border-radius:12px; width:15%; text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.08); margin:10px;'>
        <div style='font-size:24px;'>💹</div><div style='font-weight:600;'>ROI Médio</div><div style='font-size:22px; color:#F27C00;'>{roi_medio}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:0.0px'>", unsafe_allow_html=True)

    # ============================================================
    # GRÁFICOS
    # ============================================================

    # ----- Gráfico de linha: Gasto vs Lucro ao longo do tempo -----

    df_tempo = (
        df.groupby("mes_referencia", as_index=False)
        .agg({"gasto": "sum", "lucro": "sum"})
        .sort_values("mes_referencia")
    )

    st.markdown("<h4 style='text-align:center; color:#727272; font-weight:700;'>Gasto vs Lucro ao longo do tempo</h4>",
                unsafe_allow_html=True)

    fig = px.line(
        df_tempo,
        x="mes_referencia",
        y=["gasto", "lucro"],
        labels={"value": "R$", "variable": "Indicador", "mes_referencia": "Mês"},
        markers=True,
        color_discrete_sequence=["#0096C7", "#F27C00"]
    )
    fig.update_traces(line=dict(width=3, shape="spline"))
    fig.update_layout(
        plot_bgcolor="#FAFAFA", paper_bgcolor="#FAFAFA",
        font=dict(color="#2E2E2E", size=14),
        legend=dict(orientation="h", y=-0.25, x=0.5, xanchor="center"),
        margin=dict(t=40, b=50), hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div style='background-color:#FFF6EB; border-left:5px solid #F27C00; padding:15px; border-radius:5px; margin-top:15px;'>
    💡 <b>Insight:</b> O lucro permanece superior ao gasto, mas nota-se queda recente. Indica possível saturação de público ou realocação ineficiente de verba.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:0.5px solid #EAEAEA; margin:20px 0;'>", unsafe_allow_html=True)

    # ----- Gráfico de barras: Investimento x Leads por canal -----

    df_canais = (
        df.groupby("canal", as_index=False)
        .agg({"gasto": "sum", "leads": "sum"})
        .sort_values("gasto", ascending=False)
    )

    st.markdown("<h4 style='text-align:center; color:#727272; font-weight:700;'>Investimento vs Leads por canal</h4>",
                unsafe_allow_html=True)

    fig2 = px.bar(
        df_canais,
        x="canal", y="gasto",
        text_auto=".0f",
        color_discrete_sequence=["#0096C7"]
    )
    fig2.add_scatter(
        x=df_canais["canal"], y=df_canais["leads"],
        mode="lines+markers+text", name="Leads",
        line=dict(color="#F27C00", width=3, shape="spline"),
        marker=dict(size=8, color="#F27C00", line=dict(width=1, color="white")),
        text=df_canais["leads"], textposition="top center"
    )
    fig2.update_layout(
        plot_bgcolor="#FAFAFA", paper_bgcolor="#FAFAFA",
        font=dict(color="#2E2E2E", size=14),
        legend=dict(orientation="h", y=-0.25, x=0.5, xanchor="center"),
        margin=dict(t=40, b=50)
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div style='background-color:#FFF6EB; border-left:5px solid #F27C00; padding:15px; border-radius:5px; margin-top:15px;'>
    💡 <b>Insight:</b> Nem sempre o canal com mais investimento gera mais leads, indicando uma indeficiência em parte dos investimentos. 
                        Há potencial para redistribuição de verba.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:0.5px solid #EAEAEA; margin:20px 0;'>", unsafe_allow_html=True)

    # ----- Boxplot: ROI por Faixa Etária -----

    st.markdown("<h4 style='text-align:center; color:#727272; font-weight:700;'>Boxplot do ROI por Faixa Etária</h4>",
                unsafe_allow_html=True)

    bins = [18, 30, 50, 70]
    labels = ["Jovem", "Adulto", "Sênior"]
    df["faixa_etaria"] = pd.cut(df["idade_media_publico"], bins=bins, labels=labels)

    fig3 = px.box(
        df,
        x="faixa_etaria", y="roi_calc",
        color="faixa_etaria",
        color_discrete_sequence=["#0096C7"]
    )
    fig3.update_layout(
        plot_bgcolor="#FAFAFA", paper_bgcolor="#FAFAFA",
        font=dict(color="#2E2E2E", size=14),
        showlegend=False, margin=dict(t=30, b=40)
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("""
    <div style='background-color:#FFF6EB; border-left:5px solid #F27C00; padding:15px; border-radius:5px; margin-top:15px;'>
    💡 <b>Insight:</b> O público adulto apresenta alta dispersão no ROI com presença de alguns outliers, indicando subsegmentos com potencial de alta rentabilidade.
        Uma boa estratégia seria segmentar o público adulto por subfaixas etárias ou comportamento digital para entender onde o retorno é mais expressivo.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# ABA 2 - ANÁLISE PREDITIVA
# ============================================================

with aba2:
    st.markdown("<h3 style='text-align:center; color:#000000; font-weight:900;'>Análise preditiva das campanhas</h3>",
                unsafe_allow_html=True)

    # --------- Regressão Linear: Leads vs Gasto -----

    st.markdown("<h4 style='text-align:center; color:#727272; font-weight:600;'>Regressão Linear – Leads vs Gasto</h4>",
                unsafe_allow_html=True)

    X, y = df[["gasto"]], df["leads"]
    modelo = LinearRegression().fit(X, y)
    y_pred = modelo.predict(X)
    r2 = r2_score(y, y_pred)
    coef, inter = modelo.coef_[0], modelo.intercept_

    st.write(f"**Equação:** Leads = {inter:.2f} + {coef:.2f} × Gasto")
    st.write(f"**R² = {r2:.3f}** — o modelo explica {r2 * 100:.1f}% da variação dos leads.")
    fig4 = px.scatter(df, x="gasto", y="leads", trendline="ols")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown(f"""
        <div style='background-color:#FFF6EB; border-left:5px solid #F27C00; padding:15px; border-radius:5px;'>
        💡 A cada aumento de R$ 1.000 em gasto, prevê-se cerca de {coef * 1000:.0f} leads adicionais, portanto, o modelo não explica uma parte significativa da variação dos dados.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border:0.5px solid #EAEAEA; margin:30px 0;'>", unsafe_allow_html=True)

    # --------- Regressão Linear: Leads vs Cliques -----

    st.markdown(
        "<h4 style='text-align:center; color:#727272; font-weight:600;'>Regressão Linear – Leads vs Cliques</h4>",
        unsafe_allow_html=True)

    X2, y2 = df[["cliques"]], df["leads"]
    modelo2 = LinearRegression().fit(X2, y2)
    y_pred2 = modelo2.predict(X2)
    r2_2 = r2_score(y2, y_pred2)
    coef2, inter2 = modelo2.coef_[0], modelo2.intercept_

    st.write(f"**Equação:** Leads = {inter2:.2f} + {coef2:.2f} × Cliques")
    st.write(f"**R² = {r2_2:.3f}** — o modelo explica {r2_2 * 100:.1f}% da variação dos leads.")
    fig5 = px.scatter(df, x="cliques", y="leads", trendline="ols")
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown(
        f"<div style='background-color:#FFF6EB; border-left:5px solid #F27C00; padding:15px; border-radius:5px;'>💡 O modelo mostra uma forte correlação entre cliques e leads. A cada clique adicional gera em média {coef2:.2f} novos leads.</div>",
        unsafe_allow_html=True)

# ============================================================
# ABA 3 - SÍNTESE E RECOMENDAÇÕES
# ============================================================
with aba3:
    st.markdown(
        "<h3 style='text-align:center; color:#000000; font-weight:900;'>Síntese Geral e Recomendações Estratégicas</h3>",
        unsafe_allow_html=True)

    st.markdown("""
    <div style='background-color:#FFFFFF; border-radius:10px; padding:20px; margin-bottom:20px; box-shadow:0 0 5px rgba(0,0,0,0.05);'>
      <h4 style='color:#F27C00;'>Resumo da Análise</h4>
      <ul>
        <li>As campanhas apresentaram bom desempenho geral, com ROI médio de 8,9 e mais de 146 mil leads.</li>
        <li>Não há correlação forte entre gasto e leads, sugerindo ineficiência parcial.</li>
        <li>Lucro positivo, mas queda recente e concentração em poucos canais.</li>
      </ul>
    </div>

    <div style='background-color:#FFFFFF; border-radius:10px; padding:20px; margin-bottom:20px; box-shadow:0 0 5px rgba(0,0,0,0.05);'>
      <h4 style='color:#F27C00;'>Principais Insights</h4>
      <ul>
        <li>Campanhas caras não garantem mais leads.</li>
        <li>Orçamento concentrado em meios de baixo retorno.</li>
        <li>Adultos têm ROI variado, jovens mostram melhor aderência.</li>
      </ul>
    </div>

    <div style='background-color:#FFFFFF; border-radius:10px; padding:20px; margin-bottom:20px; box-shadow:0 0 5px rgba(0,0,0,0.05);'>
      <h4 style='color:#F27C00;'>Recomendações Estratégicas</h4>
      <ul>
        <li>Revisar a alocação entre canais, priorizando retorno.</li>
        <li>Segmentar adultos em subfaixas e direcionar campanhas para o publico jovens em plataformas como Instagram e TikTok.</li>
        <li>Testar criativos e ofertas para melhorar conversão.</li>
        <li>Monitorar KPIs e expandir análise preditiva com novas variáveis.</li>
      </ul>
    </div>

    <div style='background-color:#FFFFFF; border-radius:10px; padding:20px; box-shadow:0 0 5px rgba(0,0,0,0.05);'>
      <h4 style='color:#F27C00;'>Conclusão</h4>
      <p>Os resultados apontam caminhos claros para otimizar o investimento e aumentar o ROI. Com decisões baseadas em dados, é possível maximizar o impacto e reduzir desperdícios.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FIM DO APP
# ============================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Desenvolvido por Camila Candido · Dados simulados para fins de estudo · © 2025")


