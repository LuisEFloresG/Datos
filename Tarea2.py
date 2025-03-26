import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
df_ventas = pd.read_csv("./Analisis/proyecto1.csv")
df_sucursales = pd.read_csv("./Analisis/catalogo_sucursal.csv")

# Calcular ventas totales
ventas_totales = df_ventas["ventas_tot"].sum()
print(f"Ventas Totales: {ventas_totales}")

# Calcular número de socios con adeudo y sin adeudo
socios_con_adeudo = df_ventas[df_ventas["adeudo_actual"] > 0].shape[0]
socios_sin_adeudo = df_ventas[df_ventas["adeudo_actual"] == 0].shape[0]
total_socios = df_ventas.shape[0]

porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100

print(f"Socios con adeudo: {socios_con_adeudo} ({porcentaje_con_adeudo:.2f}%)")
print(f"Socios sin adeudo: {socios_sin_adeudo} ({porcentaje_sin_adeudo:.2f}%)")

# Gráfica de ventas totales respecto al tiempo
df_ventas_fecha = df_ventas.groupby("fec_ini_cdto")["ventas_tot"].sum().reset_index()
plt.figure(figsize=(10,5))
plt.bar(df_ventas_fecha["fec_ini_cdto"], df_ventas_fecha["ventas_tot"], color="blue")

plt.title("Ventas Totales a lo Largo del Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Ventas totales")
plt.legend()
plt.show()

# Gráfica de desviación estándar de pagos respecto al tiempo
df_std = df_ventas.groupby("fec_ini_cdto")["pagos_tot"].std().reset_index()
plt.figure(figsize=(10,5))
plt.plot(df_std["fec_ini_cdto"], df_std["pagos_tot"], marker="o", linestyle="-", color="green")
plt.title("Desviación Estándar de los Pagos a lo Largo del Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Desviación Estándar del Pago")
plt.show()

# Deuda total de los clientes
deuda_total = df_ventas["adeudo_actual"].sum()
print(f"Deuda Total de los Clientes: {deuda_total}")

# Porcentaje de utilidad respecto al adeudo
utilidad_porcentaje = ((ventas_totales - deuda_total) / ventas_totales) * 100
print(f"Porcentaje de Utilidad: {utilidad_porcentaje:.2f}%")

# Gráfico circular de ventas por sucursal
df_ventas_sucursal = df_ventas.groupby("id_sucursal")["ventas_tot"].sum().reset_index()
plt.figure(figsize=(8,8))
plt.pie(df_ventas_sucursal["ventas_tot"], labels=df_ventas_sucursal["id_sucursal"], autopct="%1.1f%%")
plt.title("Ventas por Sucursal")
plt.show()

# Gráfico de deudas por sucursal respecto al margen de utilidad
df_deuda_sucursal = df_ventas.groupby("id_sucursal")["adeudo_actual"].sum().reset_index()
df_utilidad_sucursal = df_ventas.groupby("id_sucursal")["ventas_tot"].sum().reset_index()
df_merged = df_deuda_sucursal.merge(df_utilidad_sucursal, on="id_sucursal")

plt.figure(figsize=(10,5))
plt.bar(df_merged["id_sucursal"], df_merged["adeudo_actual"], color="red", label="Deuda")
plt.bar(df_merged["id_sucursal"], df_merged["ventas_tot"], color="blue", alpha=0.5, label="Ventas")
plt.xticks(rotation=45)
plt.title("Deudas Totales por Sucursal vs Margen de Utilidad")
plt.xlabel("Sucursal")
plt.ylabel("Monto")
plt.show()
