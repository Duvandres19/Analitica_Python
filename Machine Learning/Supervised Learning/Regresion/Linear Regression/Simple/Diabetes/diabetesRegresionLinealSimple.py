# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:57:12 2020

@author: mateo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Importar el dataset
df = pd.read_csv('diabetes.csv')
X = df['Y'].values.reshape(-1,1)
y = df['BMI'].values.reshape(-1,1)

#Información
df.info()

#Columnas
df.columns

#Agrupar los datos de entrenaiento y de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Crear el modelo de regresion lineal
regression = LinearRegression()
regression.fit(X_train, y_train)

#Predeccion conjunto de test
y_pred = regression.predict(X_test)

#Visualizacion
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regression.predict(X_train), color="blue")
plt.xlabel("Y")
plt.ylabel("bmi")
plt.show()
