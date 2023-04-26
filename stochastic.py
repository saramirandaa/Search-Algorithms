'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    25-marzo-2023
    Versión 0.0.1

    El presente código ofrece una función que calcula la ruta más corta entre dos nodos mediante el algoritmo de Ascenso a la colina Stochastico, 
    o stochastic hill climbing. Este algoritmo es una variación del algoritmo de búsqueda informada que permite encontrar soluciones.

    Este algoritmo se calcula con la heuristica de harvesine, utiliza el codigo de best first search y ascenso a la colina para ir buscando el costo (utilizando la heuristica) más pequeño 
    A diferencia del ascenso a la colina steepest, este algoritmo busca un hijo random y de ahí va siguiendo la secuencia hasta encontrar el mejor costo

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

import random 
import time

def stochastic_hill_climbing(tree, start, goal, heuristic, log=False):
        start_time = time.time()
        #we set a certain number of iterations with the purpose of not getting into an infinite loop
        max_iterations=100
        current_node = start
        visited = set()
        iterations = 0

        #while we haven't gotten to the goal and the iterations haven't reached the max num of iterations
        while current_node != goal and iterations < max_iterations:
            #we add the current node to the visited list
            visited.add(current_node)
            #we look for the node's childs
            childs = [node_tuple[1] for node_tuple in tree if node_tuple[0] == current_node]
            best_child = []
            #we create a best cost variable with a very high number in order to get through the first if
            best_cost = float('inf')
            if log:
                print('Current node:', current_node)
                print('Childs:', childs)
                print('Visited:', visited)
                print("Best child:", best_child)
            for child in childs:
                cost = heuristic[child]
                if log:
                    print('Child:', child)
                    print('Cost:', cost)
                #if the cost (the node's heuristic) is smaller or equal than the best cost and the child is not in the visited list
                if cost <= best_cost and child not in visited:
                    #it the cost is smaller than the best one we replace it by that one 
                    if cost < best_cost:
                        best_child = [child]
                        best_cost = cost
                        if log:
                            print('Best child:', best_child)
                            print('Best cost:', best_cost)
                    else:
                        best_child.append(child)
                        if log:
                            print('Best child:', best_child)
                            print('Best cost:', best_cost)
            #if we never find a best child we return an empty path
            if not best_child:
                return None
            #else we choose a random child from the best childs
            current_node = random.choice(best_child)
           
            iterations += 1
            if log:
               print('Current RANDOM node:', current_node)
               print('Iterations:', iterations)

        if current_node != goal:
            return None

        #if the current node is the goal we shall create another list in which 
        #we will be searching its parents until arriving to the starting node
        path = [goal]
        while path[-1] != start:
            for node_tuple in tree:
                if node_tuple[1] == path[-1]:
                    path.append(node_tuple[0])
                    if log:
                        print("Path so far: ", path)
                    break
        path.reverse()
        end_time = time.time()
        if log:
            print("Tiempo de ejecución interno: ", end_time - start_time)
        return path