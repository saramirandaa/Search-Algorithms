### INFORMACIÓN GENERAL ###
'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    25-marzo-2023
    Versión 0.0.1

    El presente código ofrece una función que calcula la ruta más corta entre dos nodos mediante el algoritmo de enfriamiento simulado, o simulated annealing. Este algoritmo es una variación del algoritmo de búsqueda local que permite encontrar soluciones a problemas de optimización.

    La solución inicial se calcula con el algoritmo de A*. A partir de esta solución, se generan soluciones vecinas que se evalúan con una función de evaluación. Si la solución vecina es mejor que la solución actual, se acepta como la nueva solución actual. Si la solución vecina es peor que la solución actual, se acepta como la nueva solución actual con una probabilidad que depende de la temperatura actual y de la diferencia entre la solución actual y la solución vecina. La temperatura se va reduciendo en cada iteración hasta llegar a un valor mínimo.

    Esta función está hecha para ser utilizada con un Graph de ciudades de México como parte del proyecto de segundo parcial, pero puede ser utilizada con cualquier Graph que tenga nodos con valores de heurística de distancia de línea recta.

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
### DEPENDENCIAS ###
import time
import random
import math
import a_star

### FUNCIÓN PRINCIPAL ###
def simulated_annealing(graph, start, goal, heuristic, T=0.0, alpha=1.0, stopping_T=0.0, log=False):
    # Validación de los parámetros de entrada
    if T <= 0:
        T = float(input("La temperatura inicial debe ser mayor que 0. Ingrese un valor: "))
    if alpha <= 0 or alpha >= 1:
        alpha = float(input("El factor de reducción de la temperatura debe ser un valor entre 0 y 1. Ingrese un valor: "))
    if stopping_T <= 0:
        stopping_T = float(input("La temperatura mínima debe ser mayor que 0. Ingrese un valor: "))

    # Inicio de tiempo de ejecución
    start_time = time.time()

    # Inicialización de la solución y del costo
    current_solution = a_star.a_star(graph, start, goal, heuristic)
    current_cost = len(current_solution) - 1
    current_node = start
    
    # Inicialización de la mejor solución encontrada hasta el momento
    best_solution = current_solution
    best_cost = current_cost

    # Ciclo principal del algoritmo
    while T > stopping_T:
        # Imprimimos el valor actual de la temperatura, si se ha especificado la opción de log
        if log:
            print("Solución actual: ", current_solution)
            print("Temperatura: ", T)
        
        # Generamos un vecino aleatorio
        node_childs = [node_tuple[1] for node_tuple in graph if node_tuple[0] == current_node]
        neighbor = random.choice(node_childs)
        
        # Calculamos el costo del vecino
        new_cost = current_cost + 1
        # Si el vecino es el nodo de llegada, terminamos
        if neighbor == goal:
            return current_solution + [goal]
        # Si el vecino no es el nodo de llegada, calculamos la heurística y el costo total
        else:
            h = heuristic[neighbor]
            f = new_cost + h
        
        # Calculamos la diferencia de costo
        delta = f - (current_cost + heuristic[current_node])
        
        # Si el vecino es mejor que la solución actual, nos movemos a él
        if delta < 0:
            current_solution.append(neighbor)
            current_cost = new_cost
            current_node = neighbor
        # Si el vecino no es mejor que la solución actual, lo aceptamos con cierta probabilidad
        else:
            # Calculamos la probabilidad de aceptar el vecino
            p = math.exp(-delta / T)
            # Generamos un número aleatorio entre 0 y 1
            r = random.random()
            # Si el número es menor que la probabilidad, nos movemos al vecino
            if r < p:
                current_solution.append(neighbor)
                current_cost = new_cost
                current_node = neighbor
        
        # Actualizamos la mejor solución encontrada hasta el momento
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
        
        # Disminuimos la temperatura
        T = T * alpha

    # Fin de tiempo de ejecución
    end_time = time.time()
    if log:
        print("Tiempo de ejecución interno: ", end_time - start_time)

    # Regresamos la mejor solución encontrada hasta el momento
    return best_solution
