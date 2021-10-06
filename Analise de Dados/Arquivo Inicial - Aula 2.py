#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset


# Passo 1: Importar os dados

# Passo 2: Visualizar os dados
# - Entender as informações que estão disponiveis
# - Descobrir possiveis erros

# Passo 3: Tratamento de dados
# - Valores que estão sendo reconhecidos de forma errada
# - Valores vazios

# Passo 4: Análise inicial
# Passo 5: Análise mais completa


import pandas as pd
import plotly.express as px
# pip install plotly


# Passo 1: importar dados
table = pd.read_csv("telecom_users.csv")


# Passo 2
# display(table)
# Unnamed: 0 e IDCliente são informações inuteis
table = table.drop("Unnamed: 0", axis=1)
table = table.drop("IDCliente", axis=1)
# axis = 0 (linha), axis = 1 (coluna)
display(table.info())


# Passo 3: Tratamento de dados
# - Valores que estão sendo reconhecidos de forma errada
# Para converter o tipo de alguma coluna para outro tipo
# tabela["Coluna"] = pd.to_numeric(Coluna, erro)

# TotalGasto está recebendo um onject (string) enquanto deveria estar recebendo um float
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")
# ,errors="coerce". Quando encontrar um erro, deletar a informação

# - Valores vazios
# Preciso selecionar as melhores linhas e colunas para apagar
# Se uma coluna tem todos dados nulos, ela é inutil
# Se um cliente (linha) tiver algum dado nulo, o cliente se torna inválido
# table = table.dropna(how,axis)

table = table.dropna(how="all", axis=1)
# deletar todas as colunas que tenham todos valores vazios

table = table.dropna(how="any", axis=0)
# deletar qualquer linha que quenha pelo menos um valor vazio

# any = algum valor vazio, all = todos os valores
display(table.info())


# Passo 4: Análise inicial
# Verificar se a porcentagem relatada é a mesma que a real
print(table["Churn"].value_counts())
print(table["Churn"].value_counts(normalize=True))
# normalize = calcular percentual da coluna

print(table["Churn"].value_counts(normalize=True).map("{:.1%}".format))
print("Sim, a porcentagem gira em torno de 25% apresentado inicialmente")


# Passo 5: Análise mais completa

# - Etapa 1, criar o gráfico
# grafico = px.histogram(tabela, coluna)
# grafico de histograma (conta valores)
# para edições nos gráficos: https://plotly.com/python/histograms/

grafico = px.histogram(table, x="Dependentes")
# Mostra o grafico da coluna Dependentes
grafico.show()

coluna = "Dependentes"
grafico = px.histogram(table, x=coluna, color="Churn")
# Mostra o grafico da coluna Dependentes em relação a coluna Churn
# Posso estilizar as cores ,color_discrete_sequence=["blue", "green"]

# - Etapa 2, exibir o gráfico
grafico.show()

# Posso ainda mostrar todos os graficos com um for
for colunas in table.columns:
    grafico = px.histogram(table, x=colunas, color="Churn")
    grafico.show()
    
# O que estiver com o tab, vai ser feitas diversas vezes por causa do for
print("fim")


# ### Conclusões e Ações
# Escreva aqui suas conclusões:

# - Cliente com contrato mensal tem MUITO mais chance de cancelar
#   - Podemos fazer promoções para clientes ir para o contrato anual

# - Clientes com pouco tempo como cliente tendem a cancelar mais os planos
#   - A primeira experiencia do cliente com a operadora pode ser ruim
#   - Talvez a capacitação de clientes está trazendo clientes desqualificados
#   - Criar incentivo para o cara ficar mais tempo como cliente

# - Quanto mais serviçoes o cliente tiver, menos chance dele cancelar
#   - Podemos fazer promoções com mais serviçoes