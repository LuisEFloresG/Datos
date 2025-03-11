import pandas as pd
##Escribir una funcion que reciba un diccionario con las notas de los estudiantes del curos y devuelve una serie con minimo,maximo,media,desviación típica

def estadistica_notas(notas):
    notas= pd.Series(notas)
    estadisticas= pd.series([notas.min(), notas.max(), notas.mean(), notas.std(0)], index=['Min','Max', 'Media', 'Desviación Estandar'])
    
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >=6].sort_values(ascending=False)

notas = {'Juan': 5.9,'Juanita': 5,'Pedro': 6.6, 'Fabian': 8.5,'Maximiliano': 7.5,'Sandra': 9.8,
         'Rosario': 9,}

print(estadistica_notas(notas))
print(aprobados(notas))
    