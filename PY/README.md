
# Comparación de Complejidad Temporal: Implementación Fibonacci en Python

Este ejercicio compara las implementaciones **recursiva** e **iterativa** del cálculo del número de Fibonacci en Python, midiendo el tiempo de ejecución y el uso de memoria para diferentes valores de entrada (`n`).

---

## **Descripción**

El ejercicio consta de dos funciones principales:
1. **Recursiva**: Utiliza una función recursiva para calcular Fibonacci.
2. **Iterativa**: Usa un enfoque basado en un bucle para calcular Fibonacci.

Se utiliza la biblioteca `tracemalloc` para medir el uso de memoria y la biblioteca `time` para medir el tiempo de ejecución.

---

## **Archivos**

- `fibonacci_comparison.py`: Código Python que implementa las dos versiones de Fibonacci y realiza las mediciones de rendimiento.
- `README_PYTHON.md`: Instrucciones para ejecutar y entender el proyecto.

---

## **Requisitos**

### Herramientas necesarias
- **Python 3.x**
- **Bibliotecas estándar de Python**:
  - `matplotlib`: Para graficar resultados.
  - `tracemalloc`: Para medir el uso de memoria.
  - `time`: Para medir el tiempo de ejecución.

Instalación de matplotlib (si no está disponible):
```bash
pip install matplotlib
```

---

## **Instrucciones de Ejecución**

### Paso 1: Ejecutar el script
Corre el script `fibonacci_comparison.py`:
```bash
python fibonacci_comparison.py
```

### Paso 2: Visualizar los resultados
El script generará gráficos comparativos que muestran:
1. **Tiempo de ejecución**: Comparación entre las implementaciones recursiva e iterativa.
2. **Uso de memoria**: Comparación del consumo máximo de memoria entre las implementaciones.

---

## **Resultados Esperados**

1. **Implementación Recursiva**:
   - Tiempo de ejecución crece exponencialmente con `n`.
   - Uso de memoria mayor debido a la acumulación de llamadas en la pila.

2. **Implementación Iterativa**:
   - Tiempo de ejecución constante o lineal con respecto a `n`.
   - Uso de memoria constante, sin acumulación de llamadas recursivas.

---

## **Notas**

- Puedes ajustar el rango de `n` directamente en el script para probar diferentes valores.
- El uso de memoria puede variar ligeramente dependiendo del entorno de ejecución.

---

