import sys
import matplotlib.pyplot as plt
import numpy as np

def procesar_combinaciones(archivo):
    # Leer el archivo desde la ruta proporcionada en la terminal
    with open(archivo, 'r') as f:
        combinaciones = f.read().split(',') # Separar las combinaciones por coma

    # Remover el primer elemento que es vacio (epsilon)
    combinaciones = combinaciones[1:]

    # Contadores de ceros y unos
    ceros = []
    unos = []

    # Contar ceros y unos en cada combinación
    for comb in combinaciones:
        ceros.append(comb.count('0'))
        unos.append(comb.count('1'))
    
    return ceros, unos

def graficar_ceros(ceros):
    # Graficar la cantidad de ceros en escala lineal
    plt.figure(figsize=(10, 5))
    plt.plot(ceros, color='purple')
    plt.title('Gráfica de la cantidad de ceros')
    plt.xlabel('Cadena')
    plt.ylabel('Cantidad de ceros')
    plt.show()

def graficar_unos(unos):
    # Graficar la cantidad de unos en escala lineal
    plt.figure(figsize=(10, 5))
    plt.plot(unos, color='palegreen')
    plt.title('Gráfica de la cantidad de unos')
    plt.xlabel('Cadena')
    plt.ylabel('Cantidad de unos')
    plt.show()

def graficar_ceros_logaritmico(ceros):
    # Graficar en escala logarítmica la cantidad de ceros
    plt.figure(figsize=(10, 5))
    plt.plot(np.log10(np.array(ceros) + 1), color='purple') # Sumar 1 para evitar logaritmo de 0
    plt.title('Gráfica del logaritmo base 10 de ceros')
    plt.xlabel('Cadena')
    plt.ylabel('logaritmo base 10 de la cantidad de ceros')
    plt.show()

def graficar_unos_logaritmico(unos):
    # Graficar en escala logarítmica la cantidad de unos
    plt.figure(figsize=(10, 5))
    plt.plot(np.log10(np.array(unos) + 1), color='palegreen') # Sumar 1 para evitar logaritmo de 0
    plt.title('Gráfica del logaritmo base 10 de unos')
    plt.xlabel('Cadena')
    plt.ylabel('logaritmo base 10 de la cantidad de unos')
    plt.show()

if __name__ == "__main__":
    # Verificar que el archivo fue proporcionado como argumento
    if len(sys.argv) != 2:
        print("Uso: python graficas.py <ruta_del_archivo_txt>") # Mensaje de error
        sys.exit(1)

    archivo = sys.argv[1]

    # Procesar combinaciones binarias del archivo
    ceros, unos = procesar_combinaciones(archivo)

    # Graficar datos para 0s
    graficar_ceros(ceros)

    # Graficar datos para 1s
    graficar_unos(unos)

    # Graficar datos en escala logarítmica para 0s
    graficar_ceros_logaritmico(ceros)

    # Graficar datos en escala logarítmica para 1s
    graficar_unos_logaritmico(unos)
