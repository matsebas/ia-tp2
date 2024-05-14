## Prueba de procesos de búsqueda
## autor: Matias Sebastiao
## email: matisebastiao@gmail.com
## materia: Inteligencia Artificial
## año: 2024

from busqueda_exaustiva import buscar_en_anchura
from busqueda_heuristica import buscar_a_estrella


def test_busqueda_exaustiva():
    print(f'################################')
    print(f'Prueba de búsqueda exaustiva')
    posicion_encontrada = buscar_en_anchura(3, 1, 10)
    print(f'################################')
    print(f"Posición óptima encontrada: {posicion_encontrada}")
    print(f'################################\n')

def test_busqueda_heuristica():
    print(f'################################')
    print(f'Prueba de búsqueda heurística')
    posicion_encontrada = buscar_a_estrella(5, 3)
    print(f'################################')
    print(f"Posición óptima encontrada: {posicion_encontrada}")
    print(f'################################\n')


if __name__ == '__main__':
    test_busqueda_exaustiva()
    test_busqueda_heuristica()

