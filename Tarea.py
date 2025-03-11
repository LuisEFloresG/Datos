import pandas as pd
import matplotlib.pyplot as pit

df = pd.read_csv("./ElementosBasicosde/housing.csv")

print(df.head())

longitude = df["longitude"].mean()
print('La media del total longitud es: ')
print(longitude)

latitude = df['latitude'].mean()
print('La media del total latitud es: ')
print(latitude)

housing = df['housing_median_age'].mean()
print('La media del total housing es: ')
print(housing)

mediadecuarto = df["total_rooms"].mean()
print("La media del total room es: ")
print(mediadecuarto)

mediadecuarto2 = df["total_bedrooms"].mean()
print("La media del total bedroom es: ")
print(mediadecuarto2)

poblacion = df["population"].mean()
print("La media del total population es: ")
print(poblacion)

households = df["households"].mean()
print('La media del total households es: ')
print(households)

income = df['median_income'].mean()
print('La media de income es: ')
print(income)

value = df['median_house_value'].mean()
print('La media de value es: ')
print(value)

longitud = df["longitude"].median()
print("La mediana de la columna longitud de la casa es: ")
print(longitud)

latitud = df['latitude'].median()
print('La mediana de la columna latitud de la casa es: ')
print(latitud)

housing = df['housing_median_age'].median()
print('La mediana de la columna housing es: ')
print(housing)

mediadecuarto = df["total_rooms"].median()
print("La mediana de la columna room es: ")
print(mediadecuarto)

mediadecuarto2 = df["total_bedrooms"].median()
print("La media de la columna bedroom es: ")
print(mediadecuarto2)

poblacion = df["population"].median()
print("La mediana de la columna population es: ")
print(poblacion)

households = df["households"].median()
print('La mediana de la columna households es: ')
print(households)

income = df['median_income'].median()
print('La mediana de la columna income es: ')
print(income)

value = df['median_house_value'].median()
print('La mediana de la columna value es: ')
print(value)

