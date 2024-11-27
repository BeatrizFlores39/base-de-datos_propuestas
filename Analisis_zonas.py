# Importamos las librerías necesarias
import pandas as pd  # Para trabajar con datos y tablas

# Ruta del archivo con los datos de ventas
file_path = r"C:\Users\ASUS TUF GAMING\Documents\tarea_solucion1\file_ventas.xls"

# Cargamos los datos del archivo Excel
# Esto crea una tabla a partir del archivo que contiene los registros de ventas
df = pd.read_excel(file_path)

# Seleccionamos las columnas importantes para el análisis
# Estas columnas son las que contienen información clave sobre ventas y zonas
columns_to_use = ['Zona', 'Tipo de producto', 'Unidades', 'Importe venta total']
df = df[columns_to_use]

# Eliminamos filas que tengan datos faltantes, para evitar errores en los cálculos
df = df.dropna()

# Agrupamos las ventas por zona para calcular totales
ventas_zona = df.groupby('Zona').agg({
    'Unidades': 'sum',  # Total de unidades vendidas por zona
    'Importe venta total': 'sum'  # Total de ingresos por zona
}).reset_index()

# Clasificamos las zonas en tres niveles según las unidades vendidas
# Esto nos ayuda a identificar cuáles zonas tienen mejor desempeño
ventas_zona['Clasificación'] = pd.qcut(
    ventas_zona['Unidades'], 
    q=3, 
    labels=['Bajas ventas', 'Ventas promedio', 'Altas ventas']
)

# Agrupamos los datos para identificar el producto más vendido y el menos vendido por zona
productos_por_zona = df.groupby(['Zona', 'Tipo de producto']).agg({
    'Unidades': 'sum'  # Total de unidades vendidas por producto en cada zona
}).reset_index()

# Ordenamos para encontrar el producto más vendido por zona
productos_estrella = productos_por_zona.sort_values(['Zona', 'Unidades'], ascending=[True, False]).groupby('Zona').head(1)

# Ordenamos para encontrar el producto menos vendido por zona
productos_rezagados = productos_por_zona.sort_values(['Zona', 'Unidades'], ascending=[True, True]).groupby('Zona').head(1)

# Generamos recomendaciones para cada zona
# Combinamos la clasificación de la zona con los productos estrella y rezagados
recomendaciones = ventas_zona[['Zona', 'Clasificación']].copy()
recomendaciones['Producto estrella'] = productos_estrella['Tipo de producto'].values
recomendaciones['Producto rezagado'] = productos_rezagados['Tipo de producto'].values
recomendaciones['Recomendación'] = recomendaciones.apply(
    lambda row: f"Promocionar {row['Producto estrella']} y revisar estrategia para {row['Producto rezagado']}.", axis=1
)

# Guardamos los resultados en un nuevo archivo Excel
# Esto incluye un resumen por zona, productos estrella y rezagados, y recomendaciones
output_file = r"C:\Users\ASUS TUF GAMING\Documents\tarea_solucion1\analisis_recomendaciones.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    ventas_zona.to_excel(writer, index=False, sheet_name='Resumen por Zona')
    productos_estrella.to_excel(writer, index=False, sheet_name='Productos Estrella')
    productos_rezagados.to_excel(writer, index=False, sheet_name='Productos Rezagados')
    recomendaciones.to_excel(writer, index=False, sheet_name='Recomendaciones')

print(f"¡Análisis completado! Archivo guardado en: {output_file}")
