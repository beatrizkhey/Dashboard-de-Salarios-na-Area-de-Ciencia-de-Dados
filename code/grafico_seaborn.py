import seaborn as sns
import matplotlib.pyplot as plt
from code.tratamento_dados import df, df_limpo

sns.barplot(data=df_limpo, x='senioridade', y='usd', estimator='mean')

# Ordenando as categorias do maior para o menor valor
df.groupby('senioridade')['usd'].mean().sort_values(ascending=False)

ordem = df.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
ordem

# Gráfico de barras (barplot)
plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem, estimator='mean')
plt.title('Salário médio anual por nível de senioridade')
plt.ylabel('Salário mádio (USD)')
plt.xlabel('Senioridade')
plt.show()

# Histograma (histplot)
plt.figure(figsize=(8, 4))
sns.histplot(df_limpo['usd'], bins=100, kde=True)
plt.title('Distribuição dos salários anuais')
plt.ylabel('Salário (USD)')
plt.xlabel('Frequência')
plt.show()

# Boxplot
plt.figure(figsize=(8, 4))
sns.boxplot(x=df_limpo['usd'])
plt.title('Boxplot dos salários')
plt.xlabel('Salário em USD')
plt.show()

# Boxplot - Distribuição salarial por Senioridade
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']

plt.figure(figsize=(8, 5))
sns.boxplot(x='senioridade', y='usd', data=df, order=ordem_senioridade)
plt.title('Distribuição salarial por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário (USD)')
plt.show()

# Boxplot colorido - Distribuição salarial por Senioridade
plt.figure(figsize=(8, 5))
sns.boxplot(
    x='senioridade',
    y='usd',
    data=df,
    order=ordem_senioridade,
    palette='Set2',
    hue='senioridade'
)
plt.title('Distribuição salarial por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário (USD)')
plt.show()

# Barplot - Top 5 Países que com maiores médias salarias para Cientistas de Dados
df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds = df_ds.groupby('residencia')['usd'].mean().sort_values(ascending=False). reset_index()

plt.figure(figsize=(10,5))
sns.barplot(
    x='residencia',
    y='usd',
    data=media_ds.head(5),
    palette='Set2',
    hue='residencia'
)
plt.title('Top 5 Países que com maiores médias salarias para Cientistas de Dados')
plt.xlabel('País')
plt.ylabel('Salário Médio (USD)')
plt.show()