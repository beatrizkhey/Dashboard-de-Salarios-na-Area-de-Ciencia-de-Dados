import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

### Barplot interativo - Salário Médio por Nível de Senioridade
# Calcular média salarial
media_senioridade = df.groupby('senioridade')['usd'].mean().reset_index()

# Criar gráfico
fig = px.bar(
    media_senioridade, x='senioridade', y='usd',
    title='Salário Médio por Nível de Senioridade',
    labels={'senioridade': 'Senioridade', 'usd': 'Salário Médio (USD)'}, color='senioridade'
)
fig.update_layout(xaxis={'categoryorder': 'total descending'})
fig.show()

### Gráfico de Pizza (Pie/Donut) - Proporção dos Tipos de Trabalho
# Contar a frequeencia de cada tipo de trabalho
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# Criar gráfico de pizza
fig = px.pie(
    remoto_contagem,
    names='tipo_trabalho',
    values='quantidade',
    title='Proporção dos Tipos de Trabalho',
    hole=0.4 # opicional: transforma em donut chart
)
fig.update_traces(textinfo='percent+label')
fig.show()

### Barplot interativo - Top 5 cargos com maiores médias salariais
top_cargos = df_limpo.groupby('cargo')['usd'].mean().round(2).sort_values(ascending=False).head().reset_index()
top_cargos

# Grafico interativo
fig = px.bar(
    top_cargos,
    x='cargo',
    y='usd',
    title='Top 5 cargos com maiores médias salariais',
    labels={'usd': 'Salário médio (USD)', 'cargo': 'Cargo'}
)
fig.update_layout(xaxis_title='Cargo', yaxis_title='Salário médio (USD)')
fig.show()

### Barplot interativo - Média Salarial por Senioridade
senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(
    senioridade_media_salario,
    x='senioridade',
    y='usd',
    title='Média Salarial por Senioridade',
    labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'}
)

fig.show()

### Mapa do salário médio do Cientista de Dados por país
# Instalar biblioteca
# pip install pycountry
import pycountry

# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
  try:
    return pycountry.countries.get(alpha_2=code).alpha_3
  except:
    return None

# Criar nova coluna com código ISO-3
df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

# Calcular média salarial com código ISO-3
df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Gerar o mapa
fig = px.choropleth(
    media_ds_pais,
    locations='residencia_iso3',
    color='usd',
    color_continuous_scale='rdylgn',
    title='Salário médio de Cientista de Dados por país',
    labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
)

fig.show()