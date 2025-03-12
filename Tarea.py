import pandas as pd
import matplotlib.pyplot as pit

df = pd.read_csv("./ElementosBasicosde/housing.csv")

data = {
"Celda": [
        "Longitude", "Latitude", "Housing Median Age", "Total Rooms",
        "Total Bedrooms", "Population", "Households", "Median Income", "Median House Value"
    ],
    "Media": [
        df["longitude"].mean(),
        df["latitude"].mean(),
        df["housing_median_age"].mean(),
        df["total_rooms"].mean(),
        df["total_bedrooms"].mean(),
        df["population"].mean(),
        df["households"].mean(),
        df["median_income"].mean(),
        df["median_house_value"].mean()
    ],
   
}

df_media = pd.DataFrame(data)
print(df_media)

data = {
    "Celda": [
        "Longitude", "Latitude", "Housing Median Age", "Total Rooms",
        "Total Bedrooms", "Population", "Households", "Median Income", "Median House Value" ],
 "Mediana": [
        df["longitude"].median(),
        df["latitude"].median(),
        df["housing_median_age"].median(),
        df["total_rooms"].median(),
        df["total_bedrooms"].median(),
        df["population"].median(),
        df["households"].median(),
        df["median_income"].median(),
        df["median_house_value"].median()
    ],
}

df_mediana = pd.DataFrame(data)
print(df_mediana)

data = {
    "Celda": [
        "Longitude", "Latitude", "Housing Median Age", "Total Rooms",
        "Total Bedrooms", "Population", "Households", "Median Income", "Median House Value" ],
 "Moda": [
        df["longitude"].mode(),
        df["latitude"].mode(),
        df["housing_median_age"].mode(),
        df["total_rooms"].mode(),
        df["total_bedrooms"].mode(),
        df["population"].mode(),
        df["households"].mode(),
        df["median_income"].mode(),
        df["median_house_value"].mode()
    ],
}
df_moda = pd.DataFrame(data)
print(df_moda)

columnas = [
    "longitude", "latitude", "housing_median_age", "total_rooms",
    "total_bedrooms", "population", "households", "median_income", "median_house_value"]

data = {
    "Celda": columnas,
    "Rango": [df[col].max() - df[col].min() for col in columnas]
}

df_rango_moda = pd.DataFrame(data)
print(df_rango_moda)

data = {
    "Celda": columnas,
    "Varianza": [df[col].var() for col in columnas]
}

df_varianza = pd.DataFrame(data)
print(df_varianza)

data = {
    "Celda": columnas,
    "Desviacion Estandar": [df[col].std() for col in columnas]
}

df_desviacion_estandar = pd.DataFrame(data)
print(df_desviacion_estandar)


promedio_precio = df["median_house_value"].mean()


diferencias = df["median_house_value"] - promedio_precio

pit.scatter(df["total_bedrooms"], diferencias)
pit.xlabel("Numero de habitaciones")
pit.ylabel("promedio de casas")
pit.title("Grafico de Dispersión de Numero de Habitaciones vs Promedio de casas")
pit.show()

pit.scatter(df["population"], diferencias)
pit.xlabel("Numero de habitantes")
pit.ylabel("promedio de casas")
pit.title("Grafico de Dispersión de Numero de Habitantes vs Promedio de casas")
pit.show()