import pandas as pd
import math
import matplotlib.pyplot as plt

print("-----------------------------------")
print("Generadora de Tablas de Frecuencia")
print("-----------------------------------")

nombre_variable = input("Ingrese el nombre de la variable a evaluar: ")

n = int(input("Ingrese la cantidad de datos que desea ingresar: "))

datos = []

for i in range(n):
    dato = float(input(f"Ingrese el dato {i+1}: "))
    datos.append(dato)

df = pd.DataFrame({nombre_variable: datos})

maximo = df[nombre_variable].max().round(2)
minimo = df[nombre_variable].min().round(2)

rango = (maximo - minimo).round(3)

k = max(1, 1 + round(3.3 * math.log10(n)))

amplitud = round(rango / k, 2)

limites_inferiores = [min(datos) + i * amplitud for i in range(k)]
limites_superiores = [limite + amplitud for limite in limites_inferiores]

limites_superiores[-1] = max(datos) + 0.001

marcas_de_clase = [round((lim_inf + lim_sup) / 2, 3) for lim_inf, lim_sup in zip(limites_inferiores, limites_superiores)]
frecuencia_absoluta = [((lim_inf <= df[nombre_variable]) & (df[nombre_variable] < lim_sup)).sum() for lim_inf, lim_sup in zip(limites_inferiores, limites_superiores)]
frecuencia_relativa = [round(absoluta / len(df) * 100, 3) for absoluta in frecuencia_absoluta]

tabla_frecuencia = pd.DataFrame({
    'Límite Inferior': limites_inferiores,
    'Límite Superior': limites_superiores,
    'Marca de Clase': marcas_de_clase,
    'Frecuencia Absoluta': frecuencia_absoluta,
    'Frecuencia Relativa': frecuencia_relativa
})

print("\n-----------------------------------")
print("Resultados:")
print(f"Valor Máximo: {maximo}")
print(f"Valor Mínimo: {minimo}")
print(f"Rango: {rango}")
print(f"Número de Clases: {k}")
print(f"Amplitud de Clase: {amplitud}")
print("-----------------------------------")

print("\n-----------------------------------")
print("Tabla de Frecuencia:")
print(tabla_frecuencia)
print("-----------------------------------")


# Gráfica de barras
plt.figure(figsize=(10, 6))
plt.barh(tabla_frecuencia['Marca de Clase'], tabla_frecuencia['Frecuencia Absoluta'], height=amplitud, edgecolor='black')
plt.title('Gráfica de Barras')
plt.xlabel('Frecuencia Absoluta')
plt.ylabel('Clase')
plt.grid(axis='x')
plt.show()

# Histograma
plt.figure(figsize=(10, 6))
plt.hist(datos, bins=k, edgecolor='black')
plt.title('Histograma')
plt.xlabel('Clase')
plt.ylabel('Frecuencia Absoluta')
plt.grid(axis='y')
plt.show()