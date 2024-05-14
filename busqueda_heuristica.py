import heapq


class Nodo:
    def __init__(self, estado, costo_total, costo_real):
        self.estado = estado
        self.costo_total = costo_total
        self.costo_real = costo_real

    def __lt__(self, other):
        return self.costo_total < other.costo_total


def heuristica(estado_actual, estado_objetivo):
    # Suponiendo que la heurística es la distancia entre los estados en la dirección horizontal
    return abs(estado_actual - estado_objetivo)


def buscar_a_estrella(estado_inicial, estado_objetivo):
    """
    Encuentra la posición de montaje deseada utilizando el algoritmo A*.

    Args:
    - estado_inicial (int): El estado inicial desde el cual comenzar la búsqueda.
    - estado_objetivo (int): El estado objetivo que se desea alcanzar.

    Returns:
    - int or None: La posición de montaje encontrada, o None si no se pudo encontrar.
    """
    # Inicializar la cola de prioridad
    cola_prioridad = []
    heapq.heappush(cola_prioridad, Nodo(estado_inicial, heuristica(estado_inicial, estado_objetivo), 0))

    while cola_prioridad:
        nodo_actual = heapq.heappop(cola_prioridad)
        print("Estado actual:", nodo_actual.estado, "- Costo total:", nodo_actual.costo_total)

        # Verificar si se alcanzó el estado objetivo
        if nodo_actual.estado == estado_objetivo:
            return nodo_actual.estado

        # Expandir nodos vecinos
        for movimiento in [-1, 1]:
            nuevo_estado = nodo_actual.estado + movimiento
            nuevo_costo_real = nodo_actual.costo_real + 1  # Costo uniforme de movimiento
            nuevo_costo_total = nuevo_costo_real + heuristica(nuevo_estado, estado_objetivo)
            nuevo_nodo = Nodo(nuevo_estado, nuevo_costo_total, nuevo_costo_real)
            print("Nodo vecino:", nuevo_nodo.estado, "- Costo total:", nuevo_nodo.costo_total)
            heapq.heappush(cola_prioridad, nuevo_nodo)

    return None
