import time
import matplotlib.pyplot as plt
import tracemalloc

# Fibonacci Recursive in Python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Fibonacci Iterative in Python
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Measure execution time and memory usage
def measure_performance(fibonacci_function, n_values):
    times = []
    memory_usages = []
    for n in n_values:
        tracemalloc.start()
        start_time = time.time()
        fibonacci_function(n)
        end_time = time.time()
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times.append(end_time - start_time)
        memory_usages.append(peak_memory / 1024)  # Convert to KB
    return times, memory_usages

# Test for values of n
n_values = list(range(5, 31))  # From 5 to 30
recursive_times, recursive_memory = measure_performance(fibonacci_recursive, n_values)
iterative_times, iterative_memory = measure_performance(fibonacci_iterative, n_values)

# Plotting the results
plt.figure(figsize=(14, 7))

# Time Comparison
plt.subplot(1, 2, 1)
plt.plot(n_values, recursive_times, label="Recursive", marker="o")
plt.plot(n_values, iterative_times, label="Iterative", marker="x")
plt.title("Execution Time Comparison")
plt.xlabel("n (Fibonacci Number)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)

# Memory Comparison
plt.subplot(1, 2, 2)
plt.plot(n_values, recursive_memory, label="Recursive", marker="o")
plt.plot(n_values, iterative_memory, label="Iterative", marker="x")
plt.title("Memory Usage Comparison")
plt.xlabel("n (Fibonacci Number)")
plt.ylabel("Memory Usage (KB)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
