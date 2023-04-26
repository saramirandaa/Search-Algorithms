### INFORMACIÓN GENERAL ###
'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Clase de Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    22-marzo-2023
    Versión 0.0.2 (Sin terminar)

    El presente código define una función que realiza el algoritmo de búsqueda de mejor primer opción.

    Ejecución del programa
        Opcion 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python greedy_best_first.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar

    Entradas:
        tree = lista de tuplas con los nodos y sus conexiones
        start = nodo inicial
        goal = nodo final
        heuristic = diccionario con los nodos y sus valores heurísticos

    Salidas:
        queue = lista con el camino a seguir
'''
### DEPENDENCIAS ###
import time

### FUNCIÓN PRINCIPAL ###
def greedy_best_first(tree, start, goal, heuristic, log = False):
    # Inicio de tiempo de ejecución
    start_time = time.time()

    queue = [start]
    new_node = ''
    if start == goal:
        return queue
    
    while queue:
        current_node = queue[-1]
        min_node = 0
        
        if current_node == goal:
            return queue
        
        node_childs = [node_tuple[1] for node_tuple in tree if node_tuple[0] == current_node]    
        
        for child in node_childs:
            if child == goal:
                queue.append(child)
                return queue
            if heuristic[child]>min_node:
                min_node = heuristic[child]
                new_node = child

        if new_node not in queue:
            queue.append(new_node)

    # Fin de tiempo de ejecución
    end_time = time.time()
    if log:
        print("Tiempo de ejecución interno: ", end_time - start_time)
    
    return queue