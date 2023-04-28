import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("barcos_ref.csv")
print(tabela)
print(tabela.corr()["Preco"])

sns.heatmap(tabela.corr()[["Preco"]], annot=True, cmap="Blues")
plt.show()
