#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos 
# cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.

# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver


# Passo 1: Pegar a cotação do Dólar
# Passo 2: Pegar a cotação do Euro
# Passo 3: Pegar a cotação do Ouro

# Passo 2: Importar a base de dados
# Atualizar os valores que depêndem da cotação (Cotação, preço de compra e preço de venda)

# Passo 3: Exportar o relatório atualizado

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd


# Passo 1: Pegar a cotação do Dólar
# Criar um navegador, pedir para ele acessar uma página, e obter informações de algum objeto na página (vamos utilizar o xpath)

# - Criar um navegador
navegador = webdriver.Chrome("chromedriver.exe")

# - Acessar alguma página
navegador.get("https://www.google.com/")

# - Acessar algum elemento da minha página
# navegador.find_element_by_xpath('xpath').ação 
# A ação pode ser:
    # click() -> clicar
    # send_keys("") -> escrever algo em algum campo, ou atribuir uma ação (Keys.ENTER) = apertar enter
    # get_attributes -> retornar algum atributo que eu queira, (ex. value de algum parágrafo)
# (Lembrar de colocar o xpath entre aspas simples pois em algumas situaçãos as aspas duplas pode ser encontrada nesse xpath)
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_dolar)


# Passo 2: Cotação Euro
navegador.get("https://www.google.com/")

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_euro)


# Passo 3: Cotação Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element_by_xpath(
    '//*[@id="comercial"]').get_attribute("value")

print(cotacao_ouro)


# Passo Adicional: Tratamento de dados
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)


# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# Passo 4: Importar a base de dados
tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

# Atualizar os valores que depêndem da cotação (Cotação, preço de compra e preço de venda)

# - Atualizar cotação
# Sempre que quiser filtrar as linhas de uma tabela utilizo o loc[linha, coluna] = dado
# tabela["Moeda"] == ["Dólar"]. Nas linhas aonde a coluna Moeda é igual a Dólar
# tabela.loc[[0,2,3,5], "Cotação"] = cotacao_dolar
    # Ou seja, na coluna de Cotação, nas linhas 0, 2, 3 e 5
    # Vou substituit o valor atual por cotacao_dolar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
    # Nas linhas em que a coluna "Moeda" for igual a "Dólar", vou substituir a "Cotação" por float(cotacao_dolar)
    
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# - Atualizar preço de compra = preço original * Cotação
tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Cotação"]

# - Atualizar Preço de venda = Preço de compra * Margem
tabela["Preço Final"] = tabela["Preço Base Reais"] * tabela["Margem"]

# Posso ainda formatar a tabela
# tabela["Preço Final"] = tabela["Preço Final"].map("R$ {:.2f}".format)

# Imprimir tabela atualizada
display(tabela)


# ### Agora vamos exportar a nova base de preços atualizada
# Passo 5: Exportar
# Tabela.to_formato serve para exporta a tabela atualizada aqui no python
tabela.to_excel("Produtos Atualizados.xlsx", index=False)
# tabela.to_format("nome do arquivo que quero criar")
# ou ainda posso não querer enviar alguma coluna, coluna=False

