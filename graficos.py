import matplotlib.pyplot as plt

# Dados de exemplo (proporções)
dados = [1, 17, 10]

# Cores pastéis
cores = ['#FFD700', '#FFDAB9', '#98FB98']

# Plotando o gráfico de pizza
plt.pie(dados, labels=['Discordo', 'Concordo',
        'Concordo Totalmente'], colors=cores, autopct='%1.1f%%', startangle=90)

# Ajustando o aspecto para torná-lo um círculo
plt.axis('equal')

# Exibindo o gráfico
plt.savefig("resultado_escala.png")
