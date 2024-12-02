import time
import random

def linear_search(arr, target):
    """
    Realiza una búsqueda lineal para encontrar un elemento en la lista.
    Retorna el índice del elemento si se encuentra, o -1 si no está.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Generar datos para pruebas
def generate_test_data(n, target_position="random"):
    """
    Genera una lista de tamaño `n` con valores aleatorios.
    El `target_position` puede ser:
    - "start": Coloca el elemento al inicio (mejor caso).
    - "end": Coloca el elemento al final (peor caso).
    - "random": Coloca el elemento en una posición aleatoria (caso promedio).
    """
    arr = [random.randint(0, 1000) for _ in range(n)]
    if target_position == "start":
        arr[0] = -1  # Asegurar que el target esté al inicio
    elif target_position == "end":
        arr[-1] = -1  # Asegurar que el target esté al final
    elif target_position == "random":
        random_idx = random.randint(0, n - 1)
        arr[random_idx] = -1  # Colocar el target en una posición aleatoria
    return arr

# Medir tiempo de ejecución
def measure_time(arr, target):
    """
    Mide el tiempo de ejecución de la búsqueda lineal.
    """
    start = time.time()
    linear_search(arr, target)
    end = time.time()
    return end - start

# Tamaños de entrada para probar
n_values = [10, 100, 1000, 10000, 100000]

# Analizar los tres casos
results = {"n": [], "best_case": [], "worst_case": [], "average_case": []}

for n in n_values:
    # Mejor caso
    best_case_data = generate_test_data(n, target_position="start")
    best_time = measure_time(best_case_data, -1)

    # Peor caso
    worst_case_data = generate_test_data(n, target_position="end")
    worst_time = measure_time(worst_case_data, -1)

    # Caso promedio
    average_case_times = []
    for _ in range(5):  # Promediar 5 corridas para mayor precisión
        average_case_data = generate_test_data(n, target_position="random")
        average_case_times.append(measure_time(average_case_data, -1))
    average_time = sum(average_case_times) / len(average_case_times)

    # Almacenar resultados
    results["n"].append(n)
    results["best_case"].append(best_time)
    results["worst_case"].append(worst_time)
    results["average_case"].append(average_time)

# Visualización de los resultados
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(results["n"], results["best_case"], label="Mejor caso", marker="o")
plt.plot(results["n"], results["worst_case"], label="Peor caso", marker="x")
plt.plot(results["n"], results["average_case"], label="Caso promedio", marker="s")
plt.title("Análisis de tiempo para búsqueda lineal")
plt.xlabel("Tamaño de la entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.show()
