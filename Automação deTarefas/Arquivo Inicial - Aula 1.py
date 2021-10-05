#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio: feito por Eduardo Marques
# 
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
# O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior
# 
# E-mail da diretoria: seugmail+diretoria@gmail.com<br>
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1


# PASSO 1 - Abrir o link que eu quero (entrar no sistema)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy(" https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
# Não utilizo o pyautogui.write("") pois ele ignora caracteres especiais
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Esperar carregar o site
time.sleep(5)


# PASSO 2 - navegar até o arquivo desejado
pyautogui.click(x=383, y=345)
pyautogui.press("enter")
time.sleep(2)


# PASSO 3 - Baixar o arquivo
pyautogui.click(x=382, y=410)
pyautogui.click(x=1158, y=155)
pyautogui.click(x=978, y=562)
time.sleep(5)
pyautogui.click(x=598, y=442)


# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# PASSO 4 - Analisar os dados recebidos (aqui descobrir o faturamento e a quantidade)
import pandas as pd

tabela = pd.read_excel(r"C:\Users\eduar\Desktop\Vendas - Dez.xlsx")
# print(table)
display(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()


# ### Vamos agora enviar um e-mail pelo gmail
# PASSO 5: Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)


# PASSO 6: Enviar por email o resultado
pyautogui.click(x=83, y=218)
pyperclip.copy("eduardoreissk8@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyautogui.write("Teste Automação Python")
pyautogui.press("tab")
mensagem = f"""
Olá Eduardo,

Está mensagem é gerada automaticamente para enviar
Faturamento: {faturamento},
Quantidade: {quantidade}

Atenciosamente,
Edu
"""
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")


# #### Use esse código para descobrir qual a posição de um item que queira clicar
# Descobrir a posição atual do mouse
time.sleep(5)
pyautogui.position()

# Como instalar as bibliotecas
get_ipython().system('pip install pyautogui')
get_ipython().system('pip install pyperclip')

