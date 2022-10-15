from unicodedata import name
import pandas as pd 
import chunk 
import re 

#Leer CSV 

pokemon_data_df = pd.read_csv ('C:/Users/Usuario/Desktop/POKEMON PANDAS/pokemon_data.csv')

#Obtener Nombres y velocidad
nombres=pokemon_data_df['Name']
print(*nombres)

#Nombres y Velocidades

nombres_velocidades = pokemon_data_df[['Name','Speed']]
print (nombres_velocidades)




#pokemon_excel_df = pd.read_excel ('C:/Users/Usuario/Desktop/POKEMON PANDAS/pokemon_data.xlsx')
#print (pokemon_excel_df)

