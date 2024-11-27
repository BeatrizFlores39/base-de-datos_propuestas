import pandas as pd
import time

# 1. Medir el tiempo de inicio
inicio = time.time()

# 2.# 2. Leer el archivo de ventas
archivo = 'C:\\Users\\ASUS TUF GAMING\\Documents\\tarea_solucion1\\Ventas_Tiendas.xls'  # Cambié la ruta y el nombre del archivo
df = pd.read_excel(archivo)

# 3. Limpiar los datos (Eliminar filas vacías)
df = df.dropna()

# 4. Analizar los datos agrupándolos por zona y país
# Sumamos las ventas y unidades por cada zona y país
zonas_ventas = df.groupby(['zona', 'pais']).agg({
    'importe venta total': 'sum', 
    'importe costo total': 'sum', 
    'unidades': 'sum'
}).reset_index()

# 5. Añadir recomendaciones basadas en las ventas
def obtener_recomendacion(row):
    if row['importe venta total'] < 5000:
        return 'Más marketing'
    elif row['importe venta total'] < 10000:
        return 'Revisar estrategia de ventas'
    else:
        return 'Estrategia efectiva'

# Crear una columna nueva con las recomendaciones
zonas_ventas['recomendación'] = zonas_ventas.apply(obtener_recomendacion, axis=1)

# 6. Guardar los resultados en un nuevo archivo Excel
zonas_ventas.to_excel('analisis_recomendaciones.xlsx', index=False)

# 7. Medir el tiempo de fin y calcular el tiempo total
fin = time.time()

# 8. Mostrar el tiempo de ejecución
tiempo_ejecucion = fin - inicio
print("Tiempo de ejecución: ", tiempo_ejecucion, "segundos")
