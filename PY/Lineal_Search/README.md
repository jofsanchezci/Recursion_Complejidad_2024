   
# Análisis de Complejidad: Búsqueda Lineal en Python

Este ejemplo realiza un análisis de la **búsqueda lineal** en Python, considerando los tres contextos clásicos de análisis de algoritmos:
- **Mejor caso**: Cuando el elemento buscado está al inicio de la lista.
- **Peor caso**: Cuando el elemento buscado está al final de la lista.
- **Caso promedio**: Cuando el elemento está en una posición aleatoria de la lista.

---

## **Descripción del Algoritmo**

La búsqueda lineal recorre la lista elemento por elemento hasta encontrar el objetivo o llegar al final de la lista.

### **Complejidad Temporal**
1. **Mejor caso**: \( O(1) \), el elemento buscado se encuentra en el primer intento.
2. **Peor caso**: \( O(n) \), el algoritmo recorre toda la lista.
3. **Caso promedio**: \( O(n) \), el tiempo esperado es proporcional al tamaño de la lista.

### **Complejidad Espacial**
El algoritmo utiliza espacio constante (\( O(1) \)), ya que no requiere estructuras adicionales, excepto variables para iterar.

---

## **Archivos**

- `linear_search_analysis.py`: Código principal que implementa la búsqueda lineal, realiza el análisis y genera gráficos.
- `README_LINEAR_SEARCH.md`: Instrucciones para ejecutar y entender el proyecto.

---

## **Requisitos**

### Herramientas necesarias
- **Python 3.x**
- **Bibliotecas estándar de Python**:
  - `matplotlib`: Para graficar resultados.
  - `random`: Para generar datos de prueba.
  - `time`: Para medir el tiempo de ejecución.

Instalación de matplotlib (si no está disponible):
```bash
pip install matplotlib
```

---

## **Instrucciones de Ejecución**

### Paso 1: Ejecutar el script
Ejecuta el archivo `linear_search_analysis.py` para realizar el análisis:
```bash
python linear_search_analysis.py
```

### Paso 2: Visualizar los resultados
El script generará gráficos que muestran:
1. **Mejor caso**: Tiempo de ejecución para el caso más favorable.
2. **Peor caso**: Tiempo de ejecución para el caso más desfavorable.
3. **Caso promedio**: Tiempo promedio considerando múltiples ejecuciones con posiciones aleatorias.

---

## **Resultados Esperados**

1. **Mejor caso**:
   - Tiempo constante \( O(1) \).
2. **Peor caso**:
   - Tiempo lineal \( O(n) \), aumentando con el tamaño de la entrada.
3. **Caso promedio**:
   - Tiempo lineal \( O(n) \), en promedio recorre la mitad de la lista.

---

## **Notas**

- Puedes modificar el rango de `n` (tamaños de entrada) directamente en el script para probar diferentes configuraciones.
- Los resultados gráficos pueden variar ligeramente debido a las operaciones aleatorias.

---

