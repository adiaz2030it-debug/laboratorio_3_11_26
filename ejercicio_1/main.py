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
    return {
        (fila, columna): estado
        for fila, fila_puestos in enumerate(puestos)
        for columna, estado in enumerate(fila_puestos)
    }


def obtener_disponibles(puestos):
    return {
        (fila, columna)
        for fila, fila_puestos in enumerate(puestos)
        for columna, estado in enumerate(fila_puestos)
        if estado == 0
    }


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]
    mapa = crear_mapa(puestos)
    print("Mapa completo:", mapa)
    print("Estado en (1, 2):", mapa[(1, 2)])  
    print("Disponibles:", obtener_disponibles(puestos))  
    
    # Caso propio 
    libros = [[1, 1, 1, 0], [0, 1, 0, 0]]
    mapa_libros = crear_mapa(libros)
    print("Mapa libros:", mapa_libros)
    print("Disponibles libros:", obtener_disponibles(libros)) 

