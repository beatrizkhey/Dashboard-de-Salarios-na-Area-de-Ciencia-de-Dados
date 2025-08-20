import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', estimator='mean')
plt.title('Salário médio anual por nível de senioridade')
plt.ylabel('Salário mádio (USD)')
plt.xlabel('Senioridade')
plt.show()