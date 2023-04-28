import time
import pyautogui
import pyperclip
import pandas as pd

link = "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"
pyautogui.sleep(1)
# Entrar no google
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Google chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=957, y=604)
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
# Ou utilize um atalho para abrir o google
# pyautogui.hotkey("ctrl", "t")

# Logo após descreva o site que deseja entrar, ou a variavel link que criamos
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
# preencher login
pyautogui.click(x=922, y=474)
pyautogui.write("Iris Helen")
time.sleep(1)
pyautogui.click(x=968, y=576)
pyautogui.write("030804")
pyautogui.click(x=968, y=676)
time.sleep(5)
# Fazer o dowload da planilha
pyautogui.click(x=1654, y=376)
# importar a base de dados
tabela = pd.read_csv("C:\\Users\\irish\\Downloads\\Compras.csv", sep=";")
print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela['Quantidade'].sum()
preco_medio = total_gasto/quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)
# Entrar no email
time.sleep(3)
pyautogui.click(x=1819, y=166)
time.sleep(4)
pyautogui.click(x=1591, y=508)
time.sleep(4)
# Escrever email
pyautogui.click(x=33, y=245)
time.sleep(2)
pyautogui.write("abacaxi.company0308@gmail.com")
pyautogui.press("Enter")
time.sleep(1)
pyautogui.click(x=1281, y=502)
pyautogui.write("Relatório de compras")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=1281, y=533)
texto = f"""Caro chefe, segue abaixo o resumo das compras:

Gasto Total: R${total_gasto:,.2f}
Quantidade: {quantidade:,}
Preço médio: R${preco_medio:,.2f}

Att. Iris Helen"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.hotkey("ctrl", "enter")

# print(pyautogui.position())
# time.sleep(5)
