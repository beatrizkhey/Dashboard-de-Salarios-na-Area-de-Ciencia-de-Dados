import streamlit as st
import pandas as pd
import plotly.express as px


# Barplot - Top 10 Cargos por Salário Médio Anual
def grafico_top_salarios_cargos(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no gráfico de cargos com maiores salários.')
        return
        
    top_salarios_cargos = df.groupby('cargo')['usd'].mean().nlargest(10).sort_values().reset_index()
    fig = px.bar(top_salarios_cargos, x='usd', y='cargo', orientation='h',
                 title='Top 10 cargos por salário médio anual',
                 labels={'usd': 'Média salarial (USD)', 'cargo': ''})
    fig.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig, use_container_width=True)


# Barplot - Top 10 Cargos Mais Frequentes
def grafico_top_cargos_frequentes(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no gráfico de cargos mais frequentes.')
        return
    
    cargos_contagem = df['cargo'].value_counts().reset_index()
    cargos_contagem.columns = ['cargo', 'frequencia']
    top_frequencia_cargos = cargos_contagem.nlargest(10, 'frequencia').sort_values(by='frequencia').reset_index(drop=True)

    fig = px.bar(
       top_frequencia_cargos, 
       x='frequencia', 
       y='cargo', 
       orientation='h',
       title='Top 10 Cargos Mais Frequentes',
       labels={'frequencia': 'Número de profissionais', 'cargo': ''}
    )
    fig.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig, use_container_width=True)


# Donut chart - Proporção dos Tipos de Trabalho
def grafico_trabalho_remoto(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no gráfico de modalidades de trabalho.')
        return
    
    remoto_contagem = df['remoto'].value_counts().reset_index()
    remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

    fig = px.pie(remoto_contagem, names='tipo_trabalho', values='quantidade', hole=0.5,
                 title='Proporção dos Tipos de Trabalho')
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)


# Donut chart - Distribuição de Tipos de Contrato
def grafico_tipo_contrato(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no gráfico de tipos de contrato.')
        return
    
    tipo_contrato_contagem = df['contrato'].value_counts().reset_index()
    tipo_contrato_contagem.columns = ['contrato', 'quantidade']

    fig = px.pie(tipo_contrato_contagem, names='contrato', values='quantidade', hole=0.5, 
                 title='Proporção dos Tipos de Contrato')
    fig.update_traces(textinfo='percent+label', textposition='inside', insidetextorientation='radial')
    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)


# Choropleth map - Salário Médio de Cientista de Dados por País
def mapa_salario_pais(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no gráfico salário médio de Cientista de Dados por país.')
        return

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


# Choropleth map - Número de Profissionais por País de Residência
def mapa_profissional_pais(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no gráfico de número de profissionais por país de residência.')
        return
    
    profissionais_contagem = (df.groupby('residencia_iso3').size().reset_index(name='contagem'))

    fig = px.choropleth(
        profissionais_contagem,
        locations='residencia_iso3',
        color='contagem',
        color_continuous_scale='rdylgn',
        title='Número de Profissionais por País de Residência',
        labels={'contagem': 'Número de profissionais'}
    )
    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)


# Histograma - Distribuição de Salários Anuais
def grafico_hist_salarios(df: pd.DataFrame):
    if df.empty:
        st.warning('Nenhum dado para exibir no histograma.')
        return
    
    fig = px.histogram(df, x='usd', nbins=30, title='Distribuição de salários anuais')
    fig.update_layout(title_x=0.1)
    st.plotly_chart(fig, use_container_width=True)


# Histograma - Distribuição de Níveis de Experiência
def grafico_hist_senioridade(df: pd.DataFrame):
   if df.empty:
      st.warning('Nenhum dado para exibir no histograma.')
      return
   
   fig = px.histogram(
      df, 
      x='senioridade', 
      nbins=30, 
      title='Distribuição de Níveis de Experiência',
      labels={'senioridade': 'Níveis de Experiência'}
    )
   fig.update_layout(title_x=0.1)
   st.plotly_chart(fig, use_container_width=True)


# Histograma - Distribuição de Tipos de Contrato
def grafico_hist_contrato(df: pd.DataFrame):
   if df.empty:
      st.warning('Nenhum dado para exibir no histograma')
      return
   
   fig = px.histogram(
      df,
      x='contrato',
      nbins=30,
      title='Distribuição de Tipos de Contrato',
      labels={'contrato': 'Tipo de Contrato'}
   )
   fig.update_layout(title_x=0.1)
   st.plotly_chart(fig, use_container_width=True)


   
