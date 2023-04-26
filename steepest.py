
'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    25-marzo-2023
    Versión 0.0.1

    El presente código ofrece una función que calcula la ruta más corta entre dos nodos mediante el algoritmo de Ascenso a la colina steepest, 
    o steepest_hill climbing. Este algoritmo es una variación del algoritmo de búsqueda informada que permite encontrar soluciones.

    Este algoritmo se calcula con la heuristica de harvesine, utiliza el codigo de best first search para ir buscando el costo (utilizando la heuristica) más pequeño 

    Ejecución:
        1) Usar graph_creation.py para crear un objeto Graph a partir de un archivo csv.
        2) Usar get_euclidean_distance.py para calcular los valores de la heurística de distancia de línea recta.
        3) Importar el archivo simulated_annealing.py en el archivo donde se desee utilizar.
        4) Llamar la función simulated_annealing con los parámetros necesarios e imprimir el resultado.

    Entradas:
        1) Un objeto Graph
        2) El nombre de un nodo de partida
        3) El nombre de un nodo de llegada
        4) Un diccionario con los valores de la heurística de distancia de línea recta
        5) Un valor numérico para la temperatura inicial
        6) Un valor numérico para el factor de reducción de la temperatura
        7) Un valor booleano para imprimir los pasos del algoritmo

    Salidas:
        1) Una lista con los nombres de los nodos que conforman la ruta más corta entre el nodo de partida y el nodo de llegada.
'''
import time

def steepest_hill_climbing(tree, start, goal, heuristic, log = False):
        start_time = time.time()
        #we initialize our current node with the starting node 
        current_node = start
        #initialize our visited nodes list with a set function which will allow us to 
        #not repeat the nodes 
        visited = set()

        #while our current node has not arrived to the goal node 
        while current_node != goal:
            #we add our node to the visited list
            visited.add(current_node)
            
            childs = [node_tuple[1] for node_tuple in tree if node_tuple[0] == current_node]
            best_child = None
            if log:
                print("Current node: ", current_node)
                print("Visited nodes: ", visited)
                print("Childs: ", childs)
            #we initialize the best cost with a very high number (infinity) in order to get through the first if
            best_cost = float('inf')
            #we iterate through the childs of the current node
            for child in childs:
                if log:
                    print("Child: ", child)
                    print("Heuristic: ", heuristic[child])
                #if the child is not in our queue and its smaller than the last one 
                # the child will be the best child and will get its heuristic as the 
                if heuristic[child] < best_cost and child not in visited:
                    best_child = child
                    best_cost = heuristic[child]
                if log:
                    print("Best child: ", best_child)
                    print("Best cost: ", best_cost)
            #if we never find a best child we return an empty path
            if not best_child:
                return None
            #else our current node will be the best child
            current_node = best_child
        #we create a list with the goal as the beginning
        path = [goal]
        #until the last node is the node we set as the start node we get into a cycle
        while path[-1] != start:
            #for every node in a tree we iterate 
            for node_tuple in tree:
                #if the node is the last in the path we add the parent to the list
                if node_tuple[1] == path[-1]:
                    path.append(node_tuple[0])
                    if log:
                        print("Path so far: ", path)
                    break
        #we reverse the list in order to get the path from the start to the goal
        path.reverse()
        end_time = time.time()
        if log:
            print("Tiempo de ejecución interno: ", end_time - start_time)
        return path