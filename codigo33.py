import pandas as pd
import time

# 1. Medir el tiempo de inicio
inicio = time.time()

# 2. Leer el archivo de ventas
archivo = r'C:\Users\ASUS TUF GAMING\Documents\tarea_solucion1\file_ventas.xls'
df = pd.read_excel(archivo)

# 3. Limpiar los datos
df = df.dropna()  # Eliminar filas vacías

# Convertir 'ID Cliente' a numérico y eliminar filas con valores no válidos
df['ID Cliente'] = pd.to_numeric(df['ID Cliente'], errors='coerce')
df = df.dropna()  # Eliminar filas con valores no numéricos
clientes = df['ID Cliente'].astype(int).tolist()  # Asegurarnos de que todos los valores sean enteros

# Funciones de búsqueda
# 1. Búsqueda Lineal: O(n)
def busqueda_lineal(lista, objetivo):
    iteraciones = 0
    for i in range(len(lista)):
        iteraciones += 1
        if lista[i] == objetivo:
            return i, iteraciones
    return -1, iteraciones

# 2. Búsqueda Secuencial: O(n)
def busqueda_secuencial(lista, objetivo):
    iteraciones = 0
    for i in range(len(lista)):
        iteraciones += 1
        if lista[i] == objetivo:
            return i, iteraciones
    return -1, iteraciones

# 3. Búsqueda por Índice: O(1) en promedio
def busqueda_por_indice(lista, objetivo):
    iteraciones = 1
    try:
        return lista.index(objetivo), iteraciones
    except ValueError:
        return -1, iteraciones

# 4. Búsqueda por Hash: O(1) en promedio
def busqueda_por_hash(lista, objetivo):
    hash_table = {elem: idx for idx, elem in enumerate(lista)}
    iteraciones = 1
    return hash_table.get(objetivo, -1), iteraciones

# 5. Búsqueda Binaria: O(log n) (requiere lista ordenada)
def busqueda_binaria(lista, objetivo):
    lista_ordenada = sorted(lista)
    bajo = 0
    alto = len(lista_ordenada) - 1
    iteraciones = 0

    while bajo <= alto:
        iteraciones += 1
        medio = (bajo + alto) // 2
        if lista_ordenada[medio] == objetivo:
            return medio, iteraciones
        elif lista_ordenada[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1, iteraciones

# Medimos los tiempos de ejecución
objetivo = 1234  # ID del cliente a buscar

# Búsqueda Lineal
inicio_lineal = time.time()
resultado_lineal, iteraciones_lineal = busqueda_lineal(clientes, objetivo)
tiempo_lineal = time.time() - inicio_lineal

# Búsqueda Secuencial
inicio_secuencial = time.time()
resultado_secuencial, iteraciones_secuencial = busqueda_secuencial(clientes, objetivo)
tiempo_secuencial = time.time() - inicio_secuencial

# Búsqueda por Índice
inicio_indice = time.time()
resultado_indice, iteraciones_indice = busqueda_por_indice(clientes, objetivo)
tiempo_indice = time.time() - inicio_indice

# Búsqueda por Hash
inicio_hash = time.time()
resultado_hash, iteraciones_hash = busqueda_por_hash(clientes, objetivo)
tiempo_hash = time.time() - inicio_hash

# Búsqueda Binaria
inicio_binaria = time.time()
resultado_binaria, iteraciones_binaria = busqueda_binaria(clientes, objetivo)
tiempo_binaria = time.time() - inicio_binaria

# Mostrar los resultados
print("Búsqueda Lineal: Resultado =", resultado_lineal, ", Iteraciones =", iteraciones_lineal, ", Tiempo:", tiempo_lineal, ", Complejidad: O(n)")
print("Búsqueda Secuencial: Resultado =", resultado_secuencial, ", Iteraciones =", iteraciones_secuencial, ", Tiempo:", tiempo_secuencial, ", Complejidad: O(n)")
print("Búsqueda por Índice: Resultado =", resultado_indice, ", Iteraciones =", iteraciones_indice, ", Tiempo:", tiempo_indice, ", Complejidad: O(1) en promedio")
print("Búsqueda por Hash: Resultado =", resultado_hash, ", Iteraciones =", iteraciones_hash, ", Tiempo:", tiempo_hash, ", Complejidad: O(1) en promedio")
print("Búsqueda Binaria: Resultado =", resultado_binaria, ", Iteraciones =", iteraciones_binaria, ", Tiempo:", tiempo_binaria, ", Complejidad: O(log n)")

# Medir el tiempo total
fin_total = time.time()
tiempo_total = fin_total - inicio
print("Tiempo total de ejecución:", tiempo_total)