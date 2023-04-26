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
                    python beam_search.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar

    Entradas:
        1) Un arbol
        2) El nombre de un nodo de salida
        3) El nombre de un nodo de llegada
        4) Log como valor para definir si muestra los paso o no 


    Salidas:
        1)Lista de tuplas, donde con cada tupla se representa el camino posible. ( Distancia total del camino y la lista de las ciudades)
'''

from get_euclidean_distance import get_haversine_distance
import time
def BeamSearch(tree, start_node, goal_node,k, log = False):
    # Inicio de tiempo de ejecución
    start_time = time.time()
    # Crear la cola de búsqueda inicial con el nodo de inicio
    queue = [ (start_node, '') ]

     # Si el usuario selecciona log=True, imprime información paso a paso
    if log:
        print('Elegiste la opción de explicación paso a paso\n')
        print('Número de estados seleccionados  por el usuario: {}\n\n'.format(k) )
    # Mientras haya nodos en la cola de búsqueda, continúa la búsqueda
    while queue:
         # Obtener el primer nodo de la cola de búsqueda
        actual_state = queue.pop(0)
        print( '{}{}'.format( 'Nodo en donde nos encontramos: ' if log else '' ,actual_state[0]) )
        # Si este nodo es el nodo objetivo, se ha encontrado el camino
        if actual_state[0] == goal_node:
            print('------ Se encontró un camino ------')
            print(queue)
            return 
        # Obtener todos los nodos que son vecinos del nodo actual
        possible_nodes = [ city[1] for city in tree if city[0]  == actual_state[0] ]
        # Calcular la distancia heurística de cada nodo vecino al nodo objetivo
        values = [ (city, get_haversine_distance(city, goal_node)) for city in possible_nodes ]
        
        # Combinar los nodos vecinos con los nodos de la cola de búsqueda
        auxiliar_list = values.copy() + queue.copy()
        queue = []
        distances = [ distance[1] for distance in auxiliar_list ]
        # Seleccionar un número máximo de sucesores para explorar
        iterations = len( auxiliar_list )
        for city in range(iterations):
            
            if len(queue) >= k:
                break
            
            # Encuentra el siguiente nodo con la menor distancia heurística
            minimum =  min(distances) 
            
            next_node = auxiliar_list[ distances.index( minimum ) ]
            queue.append(next_node)
             # Elimina este nodo de la lista auxiliar para evitar duplicados
            auxiliar_list.remove(next_node)
            distances.remove( minimum )
            # Si el usuario selecciona log=True, imprime información paso a paso
        
        if log:
            print("\nBuscamos los vecinos y su heuristica")
            for index in range( len(values) ):
                print('\tVecino: {}\t\tHeuristica: {}'.format( 
                    values[index][0], values[index][1] ))
            for index in range( len(queue) ):
                print('\tNodo Seleccionado: {}\t\tHeuristica: {}'.format( 
                    queue[index][0], queue[index][1] ))
            print( '\tSiguiente nodo : {}\n\n'.format( queue[0][0] ) )
           
    
    # Si no se encuentra una solución, la búsqueda falla
    print('-----No se encontró una solución-----')
    return
    # Fin de tiempo de ejecución
    end_time = time.time()
    if log:
        print("Tiempo de ejecución interno: ", end_time - start_time)