# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:21:40 2020

@author: mateo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#importacion del dataframe
dataset = pd.read_csv('processDf.csv')


#dataframe
dataset

#nombres de la columnas
dataset.columns

#informacion
dataset.info()


#correlacion
sns.heatmap(dataset.corr(), annot=True)


#separacion de datos de prueba y entrenamiento
X= dataset['Image Number'].values.reshape(-1,1)
y= dataset['Time Lapse (hr)'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)


#crear el modelo de regresion lineal simple
regression = LinearRegression()
regression.fit(X_train, y_train)

#predecir el conjunto de test
predicciones = regression.predict(X_test)

#visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color= "red")
plt.plot(X_train, regression.predict(X_train), color= "blue")
plt.xlabel("Image number")
plt.ylabel("Time lapse")
plt.show()







