import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance

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

df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['x', 'y']

nombres = list(df_puntos.index)

resultados = []
for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        p1 = nombres[i]
        p2 = nombres[j]
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

df_resultados = pd.DataFrame(resultados)

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
