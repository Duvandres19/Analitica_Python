# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:02:54 2020

@author: mateo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets

dt=datasets.fetch_california_housing()
dt.feature_names

X= dt.data[:, np.newaxis, 2]
y= dt.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regression = LinearRegression()
regression.fit(X_train, y_train)

y_pred = regression.predict(X_test)

#visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color= "red")
plt.plot(X_train, regression.predict(X_train), color= "blue")
plt.xlabel("Image number")
plt.ylabel("Time lapse")
plt.show()