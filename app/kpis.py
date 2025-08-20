import streamlit as st
import pandas as pd

# Métricas Principais (KPIs - Key Performance Indicators)
def mostrar_kpis(df: pd.DataFrame):
    st.subheader("Métricas gerais (Salário anual em USD)")

    if not df.empty:
        salario_medio = df['usd'].mean()
        salario_maximo = df['usd'].max()
        total_registros = df.shape[0]
        cargo_mais_frequente = df['cargo'].mode()[0]
    else:
        salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, ''

    col1, col2, col3, col4 = st.columns(4)
    col1.metric('Salário médio', f'${salario_medio:,.0f}')
    col2.metric('Salário máximo', f'${salario_maximo:,.0f}')
    col3.metric('Total de registros', f'{total_registros}')
    col4.metric('Cargo mais frequente', cargo_mais_frequente)

    st.markdown("---")
