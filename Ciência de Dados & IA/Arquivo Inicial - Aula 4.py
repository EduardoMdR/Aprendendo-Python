#!/usr/bin/env python
# coding: utf-8

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio
# 
# - Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

# ### Passo a Passo de um Projeto de Ciência de Dados
# 
# - Passo 1: Entendimento do Desafio
# - Passo 2: Entendimento da Área/Empresa
# - Passo 3: Extração/Obtenção de Dados
# - Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# - Passo 5: Análise Exploratória
# - Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
# - Passo 7: Interpretação de Resultados

# # Projeto Ciência de Dados - Previsão de Vendas
# 
# - Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio


#  Criação de graficos
# pip install matplotlib
# pip install seaborn

# Inteligencia artifical
# pip install scikit-learn


# #### Importar a Base de dados
import pandas as pd

tabela = pd.read_csv("advertising.csv")
display(tabela)


# #### Análise Exploratória
# - Vamos tentar visualizar como as informações de cada item estão distribuídas
# - Vamos ver a correlação entre cada um dos itens
# Descobrir a correlação dentro da tabela por meio de gráfico

# https://seaborn.pydata.org/
import seaborn as sns
import matplotlib.pyplot as plt

# pairplot mostra a correlação das informações de uma tabela
# Criar gráfico
sns.pairplot(tabela)

# Exibir grafico
plt.show()

sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
    # tabela.corr() Analisar a correlação dos itens,
    # cmap (muda as cores),
    # annot = me retorna os dados
    # Caso de dúvida, consultar a documentação
        
plt.show() 


# #### Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# 
# - Separando em dados de treino e dados de teste

# Machine Learning
# treino meu código para poder utilizar ele

# Treinar essa inteligencia
# Separa os dados em X e Y

# Separar os dados em Treino e Teste

# Testar se está de boas


from sklearn.model_selection import train_test_split

# Baseado no meu investimento, eu quero prever quanto é que eu vou vender
# Y quem eu quero calcular
# X Quem eu quero descobrir
y = tabela["Vendas"]
x = tabela[["TV","Radio","Jornal"]]

# Separar os dados em treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
    # 70% vai ser utilizado para treino e 30% vai ser utilizado para teste, posso passar esse parâmetro, test_size=0.2
    # O nome das variaveis não é importante, mas essa ordem é
    # A separação da tabela é aleatória, com ,random_state =1 a separação vai ser sempre a mesma
    # Então toda vez que rodar o código, vou ter uma base diferente


# #### Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# 
# - Regressão Linear
# - RandomForest (Árvore de Decisão)


# para criar um inteligencia é preciso, Importar, Criar a inteligencia e treinar

# Importar IA
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Criar a inteligencia
modelo_regressao_linear = LinearRegression()
modelo_arvore_decisao = RandomForestRegressor()

# Treinando a inteligencia
modelo_regressao_linear.fit(x_treino, y_treino)
modelo_arvore_decisao.fit(x_treino, y_treino)


# #### Teste da AI e Avaliação do Melhor Modelo
# 
# - Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece

# Teste da AI e Avaliação do Melhor Modelo

from sklearn.metrics import r2_score

# Criar as previsões
previsao_regressao_linear = modelo_regressao_linear.predict(x_teste)
previsao_arvore_decisao = modelo_arvore_decisao.predict(x_teste)

# Comparar as previsões com o gabarito
print(r2_score(y_teste, previsao_regressao_linear))
print(r2_score(y_teste, previsao_arvore_decisao))
# Quando mais proximo de 1, maior é sua precisão comparada com o gabarito
# O melhor modelo é o de arvore de decisão

# #### Visualização Gráfica das Previsões

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvore_decisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressao_linear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()


# #### Qual a importância de cada variável para as vendas?

sns.barplot(x=x_treino.columns, y=modelo_arvore_decisao.feature_importances_)
plt.show()

# Caso queira comparar Radio com Jornal
# print(df[["Radio", "Jornal"]].sum())

# Novas previsões
novos_valores = pd.read_csv("novos.csv")
nova_precisao = modelo_arvore_decisao.predict(novos_valores)
display(nova_precisao)

