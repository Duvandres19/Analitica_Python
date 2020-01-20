# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 08:21:37 2020

@author: andre
"""
import pandas as pd

## Crear archivo XLS
data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  9, 5.90,  4,  3.6, 7.48, 4.37,  8.2]}

df = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
df.to_excel('../fuentes/escrituraXLS.xlsx', sheet_name='example')
df = pd.read_excel('../fuentes/escrituraXLS.xlsx', sheet_name='example')