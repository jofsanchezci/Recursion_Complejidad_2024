import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Generar datos
def generate_data(n, target_position="random"):
    arr = list(range(1, n + 1))
    if target_position == "start":
        arr[0] = -1  # Target at the start (best case)
    elif target_position == "end":
        arr[-1] = -1  # Target at the end (worst case)
    elif target_position == "random":
        random_idx = random.randint(0, n - 1)
        arr[random_idx] = -1  # Target at random position
    return arr

# Algoritmo de búsqueda lineal con pasos
def linear_search_steps(arr, target):
    steps = []
    for i in range(len(arr)):
        steps.append((i, False))  # Marca el índice actual
        if arr[i] == target:
            steps.append((i, True))  # Marca cuando encuentra el objetivo
            break
    return steps

# Animación del proceso
def animate_linear_search(arr, target):
    # Generar pasos
    steps = linear_search_steps(arr, target)
    n = len(arr)
    
    # Configuración inicial del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(range(n), arr, color="lightblue")
    ax.set_title("Animación de Búsqueda Lineal")
    ax.set_xlabel("Índices")
    ax.set_ylabel("Valores")
    
    # Actualizar cada frame
    def update(step):
        index, found = step
        for bar in bars:
            bar.set_color("lightblue")
        bars[index].set_color("orange")
        if found:
            bars[index].set_color("green")
    
    # Crear la animación
    ani = animation.FuncAnimation(fig, update, frames=steps, interval=500, repeat=False)
    plt.show()

# Configuración de datos y ejecución
n = 20
target = -1
data = generate_data(n, target_position="random")
animate_linear_search(data, target)
def binary_search_steps(arr, target):
    steps = []
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        steps.append((left, right, mid, False))  # Estado actual
        if arr[mid] == target:
            steps.append((left, right, mid, True))  # Marca objetivo encontrado
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps

def animate_binary_search(arr, target):
    steps = binary_search_steps(arr, target)
    n = len(arr)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(range(n), arr, color="lightblue")
    ax.set_title("Animación de Búsqueda Binaria")
    ax.set_xlabel("Índices")
    ax.set_ylabel("Valores")
    
    def update(step):
        left, right, mid, found = step
        for i, bar in enumerate(bars):
            if i < left or i > right:
                bar.set_color("gray")
            else:
                bar.set_color("lightblue")
        bars[mid].set_color("orange")
        if found:
            bars[mid].set_color("green")
    
    ani = animation.FuncAnimation(fig, update, frames=steps, interval=500, repeat=False)
    plt.show()

# Ejecución
data = generate_data(n, target_position="random")
animate_binary_search(data, target)
