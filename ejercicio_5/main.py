"""
Reto: reservas de grupos

DATOS
puestos = [[1, 0, 0], [0, 1, 0]]

IMPLEMENTA
reservar_grupo(puestos, coordenadas): recibe una lista de tuplas (fila, columna).
Supone que cada coordenada es una tupla de dos enteros y que el tablero es
rectangular, no vacio, con estados 0 o 1.
- Si la lista esta vacia, devuelve False.
- Si hay coordenadas repetidas, invalidas, negativas o puestos ocupados,
  devuelve False y NO modifica ninguna celda.
- Solo si todas las coordenadas son validas y disponibles, reserva todos los
  puestos (estado 1) y devuelve True.
Utiliza un set para detectar duplicados. Comprueba todas las condiciones
antes de modificar el tablero. No utilices input().

COMPROBACIONES CON PRINT
Usa una copia NUEVA del tablero inicial para CADA caso:
- [(0, 1), (1, 0)]: True.
- [(0, 1), (0, 1)]: False.
- [(0, 1), (0, 0)]: False.
- [(0, 1), (8, 0)]: False.
- []: False.
Muestra el tablero tras cada llamada. Agrega un caso propio.

ANALISIS EN COMENTARIOS
Por que no debes reservar cada puesto inmediatamente despues de comprobarlo,
antes de revisar el resto del grupo?

COMMIT SUGERIDO
Completa ejercicio 5: reserva de grupos sin cambios parciales
"""

def reservar_grupo(puestos, coordenadas):
    if not coordenadas:
        return False

    if len(set(coordenadas)) != len(coordenadas):
        return False

    filas = len(puestos)
    columnas = len(puestos[0])

    for fila, columna in coordenadas:
        if not (0 <= fila < filas and 0 <= columna < columnas):
            return False
        if puestos[fila][columna] != 0:
            return False

    for fila, columna in coordenadas:
        puestos[fila][columna] = 1

    return True


if __name__ == "__main__":
    puestos = [[1, 0, 0], [0, 1, 0]]


    tablero_1 = [fila[:] for fila in puestos]
    print("Caso 1:", reservar_grupo(tablero_1, [(0, 1), (1, 0)]), tablero_1)

    tablero_2 = [fila[:] for fila in puestos]
    print("Caso 2:", reservar_grupo(tablero_2, [(0, 1), (0, 1)]), tablero_2)



    tablero_3 = [fila[:] for fila in puestos]
    print("Caso 3:", reservar_grupo(tablero_3, [(0, 1), (0, 0)]), tablero_3)


    tablero_4 = [fila[:] for fila in puestos]
    print("Caso 4:", reservar_grupo(tablero_4, [(0, 1), (8, 0)]), tablero_4)


   
    tablero_5 = [fila[:] for fila in puestos]
    print("Caso 5:", reservar_grupo(tablero_5, []), tablero_5)


    # Caso propio
    tablero_6 = [fila[:] for fila in puestos]
    print("Caso propio (negativo):", reservar_grupo(tablero_6, [(0, 1), (-1, 2)]), tablero_6)


    tablero_7 = [fila[:] for fila in puestos]
    print("Caso propio (3 puestos):", reservar_grupo(tablero_7, [(0, 1), (0, 2), (1, 2)]), tablero_7)
