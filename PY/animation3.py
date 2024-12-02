import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

# Búsqueda Lineal
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Búsqueda Binaria
def binary_search(arr, target):
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

# Medir tiempo de ejecución
def measure_time(func, arr, target):
    start = time.time()
    func(arr, target)
    end = time.time()
    return end - start

# Generar datos para diferentes tamaños
def generate_data():
    sizes = [10**i for i in range(1, 6)]  # 10, 100, 1000, ..., 10000
    results_linear = []
    results_binary = []
    for size in sizes:
        arr = list(range(size))
        target = random.randint(0, size - 1)
        results_linear.append(measure_time(linear_search, arr, target))
        results_binary.append(measure_time(binary_search, arr, target))
    return sizes, results_linear, results_binary

# Animación de construcción de la gráfica
def animate_graph():
    sizes, results_linear, results_binary = generate_data()

    fig, ax = plt.subplots()
    ax.set_title("Construcción de Gráfica de Complejidad")
    ax.set_xlabel("Tamaño de Entrada (n)")
    ax.set_ylabel("Tiempo de Ejecución (s)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    line_linear, = ax.plot([], [], label="Búsqueda Lineal", marker="o", color="orange")
    line_binary, = ax.plot([], [], label="Búsqueda Binaria", marker="x", color="blue")
    ax.legend()

    def update(frame):
        line_linear.set_data(sizes[:frame], results_linear[:frame])
        line_binary.set_data(sizes[:frame], results_binary[:frame])
        ax.relim()  # Recalcula límites de los ejes
        ax.autoscale_view()  # Ajusta la vista automáticamente
        return line_linear, line_binary


    ani = animation.FuncAnimation(
        fig, update, frames=len(sizes), interval=500, repeat=False
    )
    plt.show()

# Ejecutar la animación
animate_graph()
