import random

def buscar_en_anchura(posicion_b, incremento, anchura_cinta_transportadora=100):
    """
    Función que implementa un algoritmo de búsqueda en anchura para encontrar la posición óptima de montaje del bloque del motor.

    Args:
      posicion_b: La posición inicial del bloque en la cinta transportadora.
      incremento: El pequeño incremento en cada movimiento del brazo mecánico.
      anchura_cinta_transportadora: La anchura de la cinta transportadora.

    Returns:
      La posición óptima de montaje del bloque del motor.
    """

    posicion_A = random.randint(0, anchura_cinta_transportadora - 1)

    # Lista de estados por explorar (cola FIFO)
    cola = [posicion_b,]
    # Diccionario para almacenar el padre de cada estado
    padre = {}
    # Diccionario para marcar los estados visitados
    visitados = set()

    while cola:
        # Obtener el siguiente estado por explorar
        posicion_actual = cola.pop(0)

        # Si se ha encontrado la posición óptima, devolverla
        if posicion_actual == posicion_A:
            return reconstruir_camino(padre, posicion_actual)

        # Marcar el estado actual como visitado
        visitados.add(posicion_actual)

        # Imprimir el estado actual
        print(f"Nodo actual: {posicion_actual}")

        # Generar los estados sucesores
        for direccion in ["izquierda", "derecha"]:
            nueva_posicion = posicion_actual + incremento * (1 if direccion == "izquierda" else -1)

            # Si el nuevo estado no está fuera de los límites de la cinta transportadora
            # y no ha sido visitado
            if 0 <= nueva_posicion < anchura_cinta_transportadora and nueva_posicion not in visitados:
                # Agregar el nuevo estado a la cola
                cola.append(nueva_posicion)

                # Actualizar el padre del nuevo estado
                padre[nueva_posicion] = posicion_actual


def reconstruir_camino(padre, posicion_actual):
    """
    Función que reconstruye el camino desde la posición inicial hasta la posición óptima.

    Args:
      padre: Diccionario que almacena el padre de cada estado.
      posicion_actual: La posición actual.

    Returns:
      Lista que representa el camino desde la posición inicial hasta la posición óptima.
    """

    camino = []
    while posicion_actual in padre:
        camino.append(posicion_actual)
        posicion_actual = padre[posicion_actual]

    camino.reverse()
    return camino
