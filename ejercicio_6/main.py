"""
Reto: varios laboratorios

DATOS
laboratorios = {
    "A": [[1, 0, 0], [0, 1, 0]],
    "B": [[1, 1], [1, 1]],
    "C": [[0, 0, 0]]
}

IMPLEMENTA
1. resumir_laboratorios(laboratorios): devuelve un diccionario con cada nombre
   como clave y una tupla (total_de_puestos, ocupados, disponibles) como valor.
2. laboratorios_con_cupo(resumen, cantidad): devuelve un set con los nombres
   de los laboratorios con al menos cantidad puestos disponibles.
   Si cantidad <= 0, devuelve un set vacio.
No modifiques los datos recibidos. Puedes utilizar sum().

COMPROBACIONES CON PRINT
- Resumen esperado: {"A": (6, 2, 4), "B": (4, 4, 0), "C": (3, 0, 3)}.
- Para cantidad 3: {"A", "C"}.
- Para cantidad 4: {"A"}.
- Para cantidad 5: set vacio.
- Comprueba tambien cantidad 0.
- Agrega un laboratorio propio y repite las consultas.
El orden de los elementos de un set no importa.

ANALISIS EN COMENTARIOS
Usa P para el total de puestos y L para el numero de laboratorios.
Que elementos revisa cada funcion? Justifica sus complejidades por separado.

COMMIT SUGERIDO
Completa ejercicio 6: resumen de multiples laboratorios
"""

def resumir_laboratorios(laboratorios):
    resumen = {}
    for nombre, matriz in laboratorios.items():
        total = sum(len(fila) for fila in matriz)
        ocupados = sum(sum(fila) for fila in matriz)
        disponibles = total - ocupados
        resumen[nombre] = (total, ocupados, disponibles)
    return resumen


def laboratorios_con_cupo(resumen, cantidad):
    if cantidad <= 0:
        return set()
    return {
        nombre
        for nombre, (_, _, disponibles) in resumen.items()
        if disponibles >= cantidad
    }


if __name__ == "__main__":
    laboratorios = {
        "A": [[1, 0, 0], [0, 1, 0]],
        "B": [[1, 1], [1, 1]],
        "C": [[0, 0, 0]]
    }

    resumen = resumir_laboratorios(laboratorios)
    print("Resumen:", resumen)


    print("Cupo >= 3:", laboratorios_con_cupo(resumen, 3))  
    print("Cupo >= 4:", laboratorios_con_cupo(resumen, 4))  
    print("Cupo >= 5:", laboratorios_con_cupo(resumen, 5)) 
    print("Cupo >= 0:", laboratorios_con_cupo(resumen, 0))  

    # Caso propio
    laboratorios_ampliados = {
        **laboratorios,
        "D": [[0, 1, 0, 0], [0, 0, 1, 0]]
    }
    resumen_ampliado = resumir_laboratorios(laboratorios_ampliados)
    print("\nResumen ampliado:", resumen_ampliado)
    
    print("Cupo >= 3 (ampliado):", laboratorios_con_cupo(resumen_ampliado, 3))  
    print("Cupo >= 4 (ampliado):", laboratorios_con_cupo(resumen_ampliado, 4)) 
    print("Cupo >= 5 (ampliado):", laboratorios_con_cupo(resumen_ampliado, 5))
    print("Cupo >= 0 (ampliado):", laboratorios_con_cupo(resumen_ampliado, 0)) 
