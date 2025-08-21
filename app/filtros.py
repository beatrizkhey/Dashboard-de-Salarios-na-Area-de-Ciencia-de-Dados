import streamlit as st
import pandas as pd

def aplicar_filtros(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header('🔍 Filtros')

    # Filtro de Ano
    anos_disponiveis = sorted(df['ano'].unique())
    anos_selecionados = st.sidebar.multiselect('Ano', anos_disponiveis, default=anos_disponiveis)

    # Filtro de Senioridade
    senioridades_disponiveis = sorted(df['senioridade'].unique())
    senioridades_selecionadas = st.sidebar.multiselect('Senioridade', senioridades_disponiveis, default=senioridades_disponiveis)

    # Filtro por Tipo de Contrato
    contratos_disponiveis = sorted(df['contrato'].unique())
    contratos_selecionados = st.sidebar.multiselect('Tipo de Contrato', contratos_disponiveis, default=contratos_disponiveis)

    # Filtro por Tamanho da Empresa
    tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
    tamanhos_selecionados = st.sidebar.multiselect('Tamanho da Empresa', tamanhos_disponiveis, default=tamanhos_disponiveis)

    # ---- Filragem do DataFrame ----
    # O dataframe principal é filtrado com base nas seleções feitas na barra lateral
    df_filtrado = df[
        (df['ano'].isin(anos_selecionados)) &
        (df['senioridade'].isin(senioridades_selecionadas)) &
        (df['contrato'].isin(contratos_selecionados)) &
        (df['tamanho_empresa'].isin(tamanhos_selecionados))
    ]

    return df_filtrado
