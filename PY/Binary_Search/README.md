   
# Mejora de Aplicaciones con Algoritmos Optimizados: Búsqueda Binaria vs Búsqueda Lineal

Este ejemplo demuestra cómo mejorar el rendimiento de una aplicación al cambiar de un algoritmo menos eficiente (búsqueda lineal) a uno más optimizado (búsqueda binaria). Este cambio reduce significativamente el tiempo de búsqueda en listas ordenadas, especialmente para grandes volúmenes de datos.

---

## **Descripción del Problema**

### Búsqueda Lineal
- **Definición**: Recorre todos los elementos de la lista hasta encontrar el objetivo.
- **Complejidad Temporal**: \( O(n) \), el tiempo aumenta linealmente con el tamaño de la lista.
- **Ventaja**: Funciona con listas desordenadas.

### Búsqueda Binaria
- **Definición**: Divide repetidamente la lista ordenada en mitades para encontrar el objetivo.
- **Complejidad Temporal**: \( O(\log n) \), el tiempo crece logarítmicamente con el tamaño de la lista.
- **Ventaja**: Mucho más rápido para listas grandes, pero requiere que la lista esté ordenada.

---

## **Archivos**

- `search_comparison.py`: Código Python que implementa ambas búsquedas, mide su rendimiento y genera gráficos comparativos.
- `README_OPTIMIZATION.md`: Explicación del ejemplo, instrucciones y conclusiones.

---

## **Requisitos**

### Herramientas necesarias
- **Python 3.x**
- **Bibliotecas estándar de Python**:
  - `time`: Para medir tiempos de ejecución.
  - `matplotlib`: Para graficar resultados.
  - `random`: Para generar datos de prueba.

Instalación de matplotlib (si no está disponible):
```bash
pip install matplotlib
```

---

## **Instrucciones de Ejecución**

### Paso 1: Ejecutar el script
Ejecuta el archivo `search_comparison.py` para realizar las pruebas:
```bash
python search_comparison.py
```

### Paso 2: Visualizar los resultados
El script generará gráficos comparativos que muestran:
1. **Tiempo de búsqueda lineal**: Crece linealmente con el tamaño de la lista.
2. **Tiempo de búsqueda binaria**: Crece logarítmicamente con el tamaño de la lista.

---

## **Resultados Esperados**

1. **Búsqueda Lineal**:
   - Aumenta linealmente con el tamaño de la lista.
   - Menos eficiente para listas grandes.

2. **Búsqueda Binaria**:
   - Tiempo mucho menor para listas grandes, debido a la complejidad logarítmica.

### **Gráficos**
El script generará gráficos para comparar ambos enfoques en términos de tiempo de ejecución.

---

## **Notas**

- Este ejemplo asume que la lista está ordenada para la búsqueda binaria.
- Puedes modificar el rango de tamaños de lista en el script para probar otros valores.

---

