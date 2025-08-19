# -*- coding: utf-8 -*-
# https://colab.research.google.com/drive/1PjPgUYyRECKUxNokqYNjuTsqbNwMZRoa#scrollTo=Tru8-khJ7HT9

# Importando a biblioteca
import pandas as pd

# Importando o dataframe
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Manipulando o dataframe
df.head()
df.info()
df.describe()
df.describe(include='object')
df.shape

linhas, colunas = df.shape[0], df.shape[1]

df.columns

#### Modificando o nome das categorias ####
# Dicionário de renomeação
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

# Aplicando a renomeação
df.rename(columns=renomear_colunas, inplace=True)

senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)

contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer',
    'CT': 'Contrato Temporário'
}
df['contrato'] = df['contrato'].replace(contrato)

tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
df['remoto'] = df['remoto'].replace(remoto)

#### Limpando a tabela ####
# Remoção das linhas com anos nulos
df_limpo = df.dropna()

# Deixar o ano como número inteiro
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('Int64'))

# Salvando o arquivo limpo
df_limpo.to_csv('dados-imersao.csv', index=False)
