import numpy as np
import matplotlib.pyplot as plt

# Definir el tamaño de entrada (n)
n = np.linspace(1, 100, 500)

# Definir las funciones de complejidad
O_1 = np.ones_like(n)              # O(1)
O_log_n = np.log2(n)              # O(log n)
O_n = n                           # O(n)
O_n_log_n = n * np.log2(n)        # O(n log n)
O_n2 = n**2                       # O(n^2)
O_2n = 2**n                       # O(2^n)

# Limitar las funciones más grandes para visualización
O_2n = np.clip(O_2n, 0, 10**3)    # Limitar O(2^n) para que sea visible

# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.plot(n, O_1, label="O(1)")
plt.plot(n, O_log_n, label="O(log n)")
plt.plot(n, O_n, label="O(n)")
plt.plot(n, O_n_log_n, label="O(n log n)")
plt.plot(n, O_n2, label="O(n²)")
plt.plot(n, O_2n, label="O(2ⁿ)")

# Configurar la gráfica
plt.yscale("log")  # Escala logarítmica en el eje y para visualizar mejor
plt.title("Curvas de Complejidad Algorítmica", fontsize=16)
plt.xlabel("Tamaño de Entrada (n)", fontsize=14)
plt.ylabel("Operaciones (Escala Logarítmica)", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Mostrar la gráfica
plt.show()
