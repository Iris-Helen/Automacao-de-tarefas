from selenium import webdriver
import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
print(tabela)

nav = webdriver.Chrome()
nav.get("https://google.com")

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    produto = produto.replace("ã", "a").replace("ç", "c").replace("á", "a").replace("ó", "o").replace("ú", "u").replace("é", "e")
    link = f"https://www.melhorcambio.com/{produto.lower()}-hoje"
    print(link)
    nav.get(link)
    preco = nav.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)
    print(tabela)

nav.quit()
tabela["Comprar"] = tabela["Preço Ideal"] > tabela["Preço Atual"]
tabela.to_excel("commodities_atualizado.xlsx", index=False)
