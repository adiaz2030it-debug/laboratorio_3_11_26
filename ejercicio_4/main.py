"""
Reporte de ocupacion

DATOS
puestos = [[1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]]

IMPLEMENTA
1. resumir_filas(puestos): devuelve una lista de tuplas
   (numero_de_fila, ocupados, disponibles). Puedes utilizar sum().
2. transformar_estados(puestos, transformar): aplica la funcion recibida a cada
   estado mediante una comprension anidada. Devuelve una tabla nueva sin
   modificar el tablero original.
Llama a transformar_estados con una lambda que transforme 0 en "Disponible"
y 1 en "Ocupado".

COMPROBACIONES CON PRINT
- Resumen esperado: [(0, 2, 2), (1, 1, 3), (2, 3, 1)].
- Muestra la tabla de textos y el tablero original despues de transformarlo.
- Agrega un tablero propio con una unica fila y comprueba sus resultados.

ANALISIS EN COMENTARIOS
- Es correcto decir que una comprension evita recorrer los puestos? Explica.
- Cuantos estados se transforman en el ejemplo inicial?

COMMIT SUGERIDO
Completa ejercicio 4: reportes y transformacion de estados
"""

def resumir_filas(puestos):
    resultado = []
    for numero_fila, fila in enumerate(puestos):
        ocupados = sum(fila)
        disponibles = len(fila) - ocupados
        resultado.append((numero_fila, ocupados, disponibles))
    return resultado


def transformar_estados(puestos, transformar):
    return [
        [transformar(estado) for estado in fila]
        for fila in puestos
    ]


if __name__ == "__main__":
    puestos = [[1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]]

    print("Resumen:", resumir_filas(puestos))
   

    tabla_textos = transformar_estados(
        puestos,
        lambda estado: "Disponible" if estado == 0 else "Ocupado"
    )
    print("Tabla de textos:", tabla_textos)
    print("Tablero original:", puestos)


