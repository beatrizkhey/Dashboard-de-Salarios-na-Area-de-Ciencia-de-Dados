import streamlit as st
from app.dados import carregar_dados, preparar_dados
from app.filtros import aplicar_filtros
from app.kpis import mostrar_kpis
from app.graficos import grafico_top_cargos, grafico_hist_salarios, grafico_trabalho_remoto, grafico_salario_pais

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados", 
    page_icon="📊", layout="wide")

# Carregar e preparar dados
df = carregar_dados()
df = preparar_dados(df)

# Aplicar filtros
df_filtrado = aplicar_filtros(df)

# Conteúdo principal
st.title("Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Use os filtros à esquerda para refinar sua análise.")

# KPIs
mostrar_kpis(df_filtrado)

# Gráficos
st.subheader("Gráficos")
col1, col2 = st.columns(2)
with col1: grafico_top_cargos(df_filtrado)
with col2: grafico_hist_salarios(df_filtrado)

col3, col4 = st.columns(2)
with col3: grafico_trabalho_remoto(df_filtrado)
with col4: grafico_salario_pais(df_filtrado)

# Tabela de Dados Detalhados
st.subheader('Dados Detalhados')
st.dataframe(df_filtrado)