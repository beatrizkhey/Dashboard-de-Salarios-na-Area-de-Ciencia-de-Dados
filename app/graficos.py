import streamlit as st
import pandas as pd
import plotly.express as px
import pycountry


def grafico_top_cargos(df: pd.DataFrame):
    if df.empty:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")
        return
        
    top_cargos = df.groupby('cargo')['usd'].mean().nlargest(10).sort_values().reset_index()
    fig = px.bar(top_cargos, x="usd", y="cargo", orientation="h",
                 title="Top 10 cargos por salário médio anual",
                 labels={"usd": "Média salarial (USD)", "cargo": ""})
    fig.update_layout(title_x=0.1, yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)


def grafico_hist_salarios(df: pd.DataFrame):
    if df.empty:
        st.warning("Nenhum dado para exibir no histograma.")
        return
    
    fig = px.histogram(df, x="usd", nbins=30, title="Distribuição de salários anuais")
    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)


def grafico_trabalho_remoto(df: pd.DataFrame):
    if df.empty:
        st.warning("Nenhum dado para exibir no gráfico de trabalho remoto.")
        return
    
    remoto_contagem = df['remoto'].value_counts().reset_index()
    remoto_contagem.columns = ["tipo_trabalho", "quantidade"]
    fig = px.pie(remoto_contagem, names="tipo_trabalho", values="quantidade", hole=0.5,
                 title="Proporção dos tipos de trabalho")
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)


def iso2_to_iso3(code):
  try:
    return pycountry.countries.get(alpha_2=code).alpha_3
  except:
    return None
  

def grafico_salario_pais(df: pd.DataFrame):
    if df.empty:
        st.warning("Nenhum dado para exibir no gráfico de países.")
        return

    df['residencia_iso3'] = df['residencia'].apply(iso2_to_iso3)

    df_ds = df[df['cargo'] == 'Data Scientist']
    media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

    fig = px.choropleth(
        media_ds_pais,
        locations='residencia_iso3',
        color='usd',
        color_continuous_scale='rdylgn',
        title='Salário médio de Cientista de Dados por país',
        labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
    )

    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)
