import matplotlib.pyplot as plt

# Leer resultados desde los archivos
def read_results(filename):
    n_values = []
    times = []
    with open(filename, 'r') as file:
        for line in file:
            n, time = line.strip().split()
            n_values.append(int(n))
            times.append(float(time))
    return n_values, times

# Leer datos
recursive_n, recursive_times = read_results("recursive_results.txt")
iterative_n, iterative_times = read_results("iterative_results.txt")

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(recursive_n, recursive_times, label="Recursive", marker="o")
plt.plot(iterative_n, iterative_times, label="Iterative", marker="x")
plt.title("Execution Time: Recursive vs Iterative (C)")
plt.xlabel("n (Fibonacci Number)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
