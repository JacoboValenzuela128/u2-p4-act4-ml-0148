import pandas as pd
import numpy as np
# Arath Valenzuela NC:0148 (23/10/26) 
n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE')                                 # Etiquetas para las columnas de una tupla 
print(tag_columna)
matriz = np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas y 5 columnas (5*5).")        
print("Con numeros aleatorios comprendidos entre 1 y 6.")    
print(matriz)
# La variable df es DataFrame 
df = pd.DataFrame(matriz, columns= tag_columna)
print("----- La tabla o DataFrame -----")
print(df)
print("----- NC:0148 -----")
print("----- Arath Valenzuela NC:0148 -----")