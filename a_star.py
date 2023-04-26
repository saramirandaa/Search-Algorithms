### INFORMACIÓN GENERAL ###
'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    22-marzo-2023
    Versión 1.0.0

    El presente código ofrece una función que calcula la ruta más corta entre dos nodos. Se utilizan los valores de la heurística de distancia de línea recta para informar la selección de nodos de manera que se expandan solo los nodos con la menor distancia de línea recta al nodo objetivo. 

    La heurística se calcula de la siguiente manera: f(n) = g(n) + h(n), donde g(n) es el costo del camino desde el nodo de partida hasta el nodo n y h(n) es la distancia de línea recta entre el nodo n y el nodo de llegada.

    Esta función está hecha para ser utilizada con un Graph de ciudades de México como parte del proyecto de segundo parcial, pero puede ser utilizada con cualquier Graph que tenga nodos con valores de heurística de distancia de línea recta.

    Ejecución:
        1) Usar graph_creation.py para crear un objeto Graph a partir de un archivo csv.
        2) Usar get_euclidean_distance.py para calcular los valores de la heurística de distancia de línea recta.
        3) Importar la función a_star en el archivo donde se desee utilizar.
        4) Llamar la función a_star con los parámetros necesarios e imprimir el resultado.

    Entradas:
        1) Un objeto Graph
        2) El nombre de un nodo de partida
        3) El nombre de un nodo de llegada
        4) Un diccionario con los valores de la heurística de distancia de línea recta
        5) Un valor booleano para imprimir los pasos del algoritmo

    Salidas:
        1) Una lista con los nombres de los nodos que conforman la ruta más corta entre el nodo de partida y el nodo de llegada.
'''
### DEPENDENCIAS ###
import time

### FUNCIÓN PRINCIPAL ###
def a_star(graph, start, goal, heuristic, log = False):
    # Inicio de tiempo de ejecución
    start_time = time.time()

    # Creación de la cola con un elemento inicial
    queue = [(0, start)]

    # Creación de un diccionario para guardar los nodos de los que venimos
    came_from = {}
    came_from[start] = None

    # Creación de un diccionario para guardar los costos de los nodos
    cost_so_far = {}
    cost_so_far[start] = 0

    # Mientras nuestra cola no esté vacía, empezamos a buscar el nodo con el costo más bajo
    while queue:
        # Imprimimos los valores de la cola, los costos y los nodos de los que venimos
        if log:
            print("Cola: ", queue)
            print("Costos: ", cost_so_far)
            print("Visitados: ", came_from)
            print()

        # Inicializamos el nodo actual con el nodo de partida
        current_node = queue[0][1]
        queue = queue[1:]
        
        # Si el nodo actual es el nodo de llegada, terminamos
        if current_node == goal:
            break
        
        # Si no, buscamos los nodos hijos del nodo actual
        node_childs = [node_tuple[1] for node_tuple in graph if node_tuple[0] == current_node]
        
        # Para cada nodo hijo, calculamos el costo y lo agregamos a la cola
        for child in node_childs:
            new_cost = cost_so_far[current_node] + 1
            # Si el nodo hijo no está en el diccionario de costos o el costo calculado es menor al costo que ya está en el diccionario, actualizamos el costo y lo agregamos a la cola
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                # Calculamos la prioridad del nodo hijo
                priority = new_cost + heuristic[child]
                # Agregamos el nodo hijo a la cola
                queue.append((priority, child))
                queue.sort()
                came_from[child] = current_node
    
    # Creamos una lista con los nodos de la ruta más corta
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()

    # Fin de tiempo de ejecución
    end_time = time.time()
    if log:
        print("Tiempo de ejecución interno: ", end_time - start_time)
    
    # Regresamos la lista con los nodos de la ruta más corta
    return path