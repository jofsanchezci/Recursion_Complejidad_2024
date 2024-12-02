
# Comparación de Complejidad Temporal: Implementación Fibonacci en C

Este ejercicio compara las implementaciones **recursiva** e **iterativa** del cálculo del número de Fibonacci en C, midiendo el tiempo de ejecución para diferentes valores de entrada (`n`) y generando resultados gráficos.

---

## **Descripción**

El ejercicio consta de dos programas independientes:
1. **Recursivo**: Utiliza una función recursiva para calcular Fibonacci.
2. **Iterativo**: Usa un enfoque basado en un bucle para calcular Fibonacci.

Ambos programas generan un archivo con los tiempos de ejecución para diferentes valores de `n`, que posteriormente se grafican usando Python.

---

## **Archivos**

- `recursive_fibonacci.c`: Implementación recursiva con medición de tiempos.
- `iterative_fibonacci.c`: Implementación iterativa con medición de tiempos.
- `recursive_results.txt`: Resultados generados por el programa recursivo (n y tiempos).
- `iterative_results.txt`: Resultados generados por el programa iterativo (n y tiempos).
- `graph_results.py`: Script Python para leer los resultados y generar la gráfica.
- `README.md`: Instrucciones para ejecutar y entender el proyecto.

---

## **Requisitos**

### Herramientas necesarias
- **Compilador C**: Compatible con GCC.
- **Python 3.x**: Para generar las gráficas.
- **Bibliotecas Python**:
  - `matplotlib`: Para la visualización gráfica.

Instalación de matplotlib (si no está disponible):
```bash
pip install matplotlib
```

---

## **Instrucciones de Ejecución**

### Paso 1: Compilar los programas en C
Compila ambos programas utilizando `gcc`:
```bash
gcc recursive_fibonacci.c -o recursive
gcc iterative_fibonacci.c -o iterative
```

### Paso 2: Ejecutar los programas
Ejecuta cada programa para generar los resultados:
```bash
./recursive
./iterative
```

Esto creará dos archivos:
- `recursive_results.txt`
- `iterative_results.txt`

### Paso 3: Generar la gráfica
Usa el script Python para procesar los resultados y crear la gráfica:
```bash
python com_C.py
```

---

## **Resultados Esperados**

1. **Implementación Recursiva**:
   - El tiempo de ejecución aumenta exponencialmente con `n`.
   - Uso de memoria mayor debido al manejo de la pila de llamadas.

2. **Implementación Iterativa**:
   - Tiempo de ejecución constante o lineal.
   - Uso de memoria constante, sin acumulación de llamadas recursivas.

---

## **Notas**

- El rango de `n` puede ajustarse modificando el bucle en los archivos `.c`.
- Para analizar el consumo de memoria, herramientas como `valgrind` pueden integrarse en futuros análisis.

---

