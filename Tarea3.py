import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.spatial import distance

# Definir los puntos
puntos = {
    'A': (2, 3),
    'B': (5, 4),
    'C': (1, 1),
    'D': (6, 7),
    'E': (3, 5),
    'F': (8, 2),
    'G': (4, 6),
    'H': (2, 1)
}

# Convertimos a DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['x', 'y']

# Lista de combinaciones de pares de puntos
pares = list(combinations(df_puntos.index, 2))

# Calcular distancias
resultados = []
for p1, p2 in pares:
    punto1 = df_puntos.loc[p1].values
    punto2 = df_puntos.loc[p2].values
    dist_euc = distance.euclidean(punto1, punto2)
    dist_man = distance.cityblock(punto1, punto2)
    dist_che = distance.chebyshev(punto1, punto2)
    resultados.append({
        'Punto 1': p1,
        'Punto 2': p2,
        'Euclidiana': dist_euc,
        'Manhattan': dist_man,
        'Chebyshev': dist_che
    })

# Convertimos a DataFrame
df_resultados = pd.DataFrame(resultados)

# Mostrar pares más cercanos y más alejados
def mostrar_extremos(df, tipo):
    min_dist = df[tipo].min()
    max_dist = df[tipo].max()
    print(f"\n--- Distancia {tipo} ---")
    print("Pares más cercanos:")
    print(df[df[tipo] == min_dist])
    print("Pares más alejados:")
    print(df[df[tipo] == max_dist])

for tipo in ['Euclidiana', 'Manhattan', 'Chebyshev']:
    mostrar_extremos(df_resultados, tipo)

# Gráfico
plt.figure(figsize=(8, 6))
for nombre, (x, y) in puntos.items():
    plt.scatter(x, y, label=nombre)
    plt.text(x + 0.1, y + 0.1, nombre, fontsize=12)

plt.title("Puntos en el Plano")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
