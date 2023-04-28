import pandas as pd
import plotly.express as px

# importar base de dados
tabela = pd.read_csv("clientes.csv", encoding="latin1", sep=";")
# retirar dados irrelevantes
tabela = tabela.drop("Unnamed: 8", axis=1)
# tratamento da base de dados
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
tabela = tabela.dropna()
print(tabela.info())
# analise dos dados
pd.set_option("display.max_columns", None)
print(tabela.describe())
# count = Informações não vazias
# mean = Média dos valores por coluna
# std = Desvio padrão
# min = valor mínimo
# max = valor máximo
print(tabela)
for coluna in tabela .columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", text_auto=True, histfunc="avg", nbins=10)
    grafico.show()
