import pandas as pd

def carregar_dados(caminho: str = "data/dados-imersao.csv") -> pd.DataFrame:
    df = pd.read_csv(caminho)
    return df

def preparar_dados(df: pd.DataFrame) -> pd.DataFrame:
    # Dicionários de renomeação
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
    df.rename(columns=renomear_colunas, inplace=True)

    # Substituições
    df['senioridade'] = df['senioridade'].replace({'SE': 'Senior','MI': 'Pleno','EN': 'Junior','EX': 'Executivo'})
    df['contrato'] = df['contrato'].replace({'FT': 'Tempo Integral','PT': 'Tempo Parcial','FL': 'Freelancer','CT': 'Contrato Temporário'})
    df['tamanho_empresa'] = df['tamanho_empresa'].replace({'S': 'Pequena','M': 'Média','L': 'Grande'})
    df['remoto'] = df['remoto'].replace({0: 'Presencial',50: 'Híbrido',100: 'Remoto'})

    # Limpeza
    df = df.dropna()
    df = df.assign(ano=df['ano'].astype("Int64"))
    return df
