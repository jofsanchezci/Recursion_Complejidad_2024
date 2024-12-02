
# Complejidad de los Algoritmos

La complejidad de los algoritmos es un concepto central en ciencias de la computación y se refiere a la medida del tiempo y el espacio necesarios para ejecutar un algoritmo a medida que crece el tamaño de la entrada. Se clasifica en **complejidad temporal** y **complejidad espacial**:

---

## **1. Complejidad Temporal**

Es el tiempo que un algoritmo tarda en completarse, medido generalmente en términos del número de operaciones elementales realizadas. Se utiliza la notación Big-O para expresar cómo aumenta el tiempo con el tamaño de la entrada.

### Ejemplos de clases de complejidad temporal:
- **O(1)**: Tiempo constante, independiente del tamaño de la entrada.  
  **Ejemplo**: Acceso directo a un elemento de un array.
- **O(log n)**: Logarítmico, el tiempo crece lentamente en relación con la entrada.  
  **Ejemplo**: Búsqueda binaria.
- **O(n)**: Lineal, el tiempo crece proporcionalmente al tamaño de la entrada.  
  **Ejemplo**: Recorrer una lista.
- **O(n log n)**: Usual en algoritmos eficientes de ordenamiento como Merge Sort.
- **O(n²)**: Cuadrática, común en algoritmos menos eficientes como Bubble Sort en su forma básica.
- **O(2ⁿ)** o **O(n!)**: Exponencial o factorial, generalmente ineficientes para entradas grandes, como en problemas de fuerza bruta o Backtracking.

---

## **2. Complejidad Espacial**

Es la cantidad de memoria adicional que requiere un algoritmo para ejecutarse. Esto incluye tanto la memoria usada por las variables como el almacenamiento de estructuras auxiliares.

### Factores que influyen:
- **Uso de estructuras de datos auxiliares** (como pilas o colas).
- **La recursión**, que requiere memoria adicional para mantener el estado de las llamadas recursivas.
- **El tamaño del espacio de entrada**.

---

## **3. Comparación y Elección de Algoritmos**

La elección de un algoritmo depende de:
- **Tamaño de la entrada**: Para entradas pequeñas, un algoritmo con alta complejidad puede ser aceptable.
- **Restricciones de tiempo o memoria**: En sistemas con recursos limitados, se prefieren algoritmos más eficientes en memoria.
- **Patrones de entrada**: Algunos algoritmos son más eficientes para ciertos casos, como QuickSort para entradas desordenadas o casi ordenadas.

---

## **4. Análisis de Algoritmos**

El análisis se realiza en tres contextos:
- **Peor caso**: Tiempo máximo que un algoritmo tomará para cualquier entrada de tamaño `n`.
- **Mejor caso**: Tiempo mínimo requerido para la entrada más favorable.
- **Caso promedio**: Tiempo promedio considerando todas las posibles entradas de tamaño `n`.

---

## **5. Herramientas de Análisis**

### Métodos para analizar algoritmos:
- **Contar operaciones fundamentales**: Analizar bucles, recursiones y cálculos.
- **Técnicas matemáticas**: Resolver relaciones de recurrencia (como en `T(n) = 2T(n/2) + O(n)` para Merge Sort).
- **Simulaciones**: Ejecutar el algoritmo con entradas grandes para medir el tiempo y uso de memoria.

---

## **Notas**

Este README proporciona una visión general de los conceptos clave relacionados con la complejidad de algoritmos. Puede ampliarse con ejemplos prácticos y análisis detallados según sea necesario.

---


