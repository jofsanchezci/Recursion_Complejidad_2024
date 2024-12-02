    def linear_search(arr, target):
    """
    Busca un elemento en la lista mediante búsqueda lineal.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Busca un elemento en la lista mediante búsqueda binaria.
    La lista debe estar ordenada.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

import time

# Generar una lista de 1 millón de elementos
data = list(range(1, 1_000_001))
target = 999_999

# Búsqueda lineal
start_time = time.time()
linear_result = linear_search(data, target)
linear_time = time.time() - start_time

# Búsqueda binaria
start_time = time.time()
binary_result = binary_search(data, target)
binary_time = time.time() - start_time

# Mostrar resultados
print(f"Búsqueda Lineal: Índice {linear_result}, Tiempo {linear_time:.6f} segundos")
print(f"Búsqueda Binaria: Índice {binary_result}, Tiempo {binary_time:.6f} segundos")


import matplotlib.pyplot as plt

# Tamaños de entrada
sizes = [10**i for i in range(1, 7)]  # 10, 100, 1000, ..., 1,000,000
linear_times = []
binary_times = []

for size in sizes:
    data = list(range(1, size + 1))
    target = size

    # Medir tiempo de búsqueda lineal
    start_time = time.time()
    linear_search(data, target)
    linear_times.append(time.time() - start_time)

    # Medir tiempo de búsqueda binaria
    start_time = time.time()
    binary_search(data, target)
    binary_times.append(time.time() - start_time)

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label="Búsqueda Lineal", marker="o")
plt.plot(sizes, binary_times, label="Búsqueda Binaria", marker="x")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de Búsqueda Lineal vs Búsqueda Binaria")
plt.legend()
plt.grid(True, which="both", linestyle="--")
plt.show()
