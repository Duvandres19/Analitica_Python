# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:04:00 2020

@author: mateo
"""
print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('advertising.csv')

print('Dataset')
print(dataset)

print('Columnas')
print(dataset.columns)


print('Informacion')
dataset.info()

print('Descripcion')
dataset.describe()

sns.distplot(dataset['Age'])

sns.heatmap(dataset.corr(), annot=True)


#Columnas a evaluar
#X = dataset[['Male', 'Age']]
X = dataset['Age'].values.reshape(-1,1)
Y = dataset['Daily Internet Usage'].values.reshape(-1,1)

#dividir dataset en conjuntos de datos de prueba y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)

#crear modelo de regresion lineal simple con el conjunto de entrenamiento
regression = LinearRegression()
regression.fit(X_train, y_train)

#predecir el conjunto de test
y_pred = regression.predict(X_test)


#visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.show()











