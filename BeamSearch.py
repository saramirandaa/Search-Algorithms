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

    queue = [ (start_node, '') ]
    
    if log:
        print('Beam search explanation\n')
        print('Your selected maximum number of successors: {}\n\n'.format(k) )
    
    while queue:
        
        actual_state = queue.pop(0)
        print( '{}{}'.format( '\tActual node: ' if log else '' ,actual_state[0]) )
        
        if actual_state[0] == goal_node:
            print('\n\t\tSuccessful search!!!')
            return 
        
        possible_nodes = [ city[1] for city in tree if city[0]  == actual_state[0] ]
        values = [ (city, get_haversine_distance(city, goal_node)) for city in possible_nodes ]
        
        auxiliar_list = values.copy() + queue.copy()
        queue = []
        distances = [ distance[1] for distance in auxiliar_list ]
        
        iterations = len( auxiliar_list )
        for city in range(iterations):
            
            if len(queue) >= k:
                break
            
            minimum =  min(distances) 
            
            next_node = auxiliar_list[ distances.index( minimum ) ]
            queue.append(next_node)
            
            auxiliar_list.remove(next_node)
            distances.remove( minimum )
            
        if log:
            print("\nWe start searching for its neighbours and their heuristic values")
            for index in range( len(values) ):
                print('\tNeighbour: {}\t\tHeuristic value: {}'.format( 
                    values[index][0], values[index][1] ))
            print('\nThen we combine all the neighbours with the previous selected successors')
            print('and stay with the ones with less heuristic value')
            for index in range( len(queue) ):
                print('\tSelected node: {}\t\tHeuristic value: {}'.format( 
                    queue[index][0], queue[index][1] ))
            print('\nFinally we will explore the node with the less value')
            print( '\tNext node: {}\n\n'.format( queue[0][0] ) )
           
    
        
    print('\n\tFailed search ')
    return
    # Fin de tiempo de ejecución
    end_time = time.time()
    if log:
        print("Tiempo de ejecución interno: ", end_time - start_time)