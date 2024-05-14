## Prueba de procesos de búsqueda

Este repositorio contiene implementaciones de algoritmos de búsqueda exhaustiva y heurística en Python, utilizados para encontrar una posición óptima en un problema de búsqueda.

### Autor
- Matias Sebastiao
- Email: matisebastiao@gmail.com

### Materia
- Inteligencia Artificial

### Año
- 2024

## Contenido del repositorio

### Archivos principales
1. `busqueda_exaustiva.py`: Contiene la implementación del algoritmo de búsqueda exhaustiva.
2. `busqueda_heuristica.py`: Contiene la implementación del algoritmo de búsqueda heurística (A*).
3. `main.py`: Archivo principal que realiza pruebas de los algoritmos de búsqueda exhaustiva y heurística.

### Ejecución
Para ejecutar las pruebas de los algoritmos de búsqueda, simplemente ejecute el archivo `main.py` desde la línea de comandos o desde su IDE preferido. Asegúrese de tener Python instalado en su sistema.

### Pruebas
El archivo `main.py` contiene pruebas de los algoritmos de búsqueda exhaustiva y heurística. Las pruebas consisten en encontrar una posición óptima en un problema de búsqueda utilizando ambos algoritmos.

### Código de ejemplo
```python
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
