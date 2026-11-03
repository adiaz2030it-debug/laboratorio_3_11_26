"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    # TODO: implementa esta funcion.
    return {(fila, columna): puestos[fila][columna] for fila in range(len(puestos)) for columna in range(len(puestos[fila]))}


def obtener_disponibles(puestos):
    # TODO: implementa esta funcion.
    return {(fila, columna) for fila in range(len(puestos)) for columna in range(len(puestos[fila])) if puestos[fila][columna] == 0}


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]
    libros = [[1, 1, 1, 0], [0, 9, 0, 0]]
    print(crear_mapa(puestos))
    print(obtener_disponibles(puestos))
    print(crear_mapa(libros))
    print(obtener_disponibles(libros))

    # TODO: escribe las llamadas y muestra los resultados con print.
    # TODO: agrega al menos un caso propio.

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.

"""
se revisan 6 celdas
se revisan f*c celdas para f filas y c columnas
"""
