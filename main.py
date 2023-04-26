### INFORMACIÓN GENERAL ###
'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Clase de Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    22-marzo-2023
    Versión 0.0.2

    El presente código utiliza las bibliotecas de algoritmos de búsqueda creadas en este periodo para resolver el problema de encontrar la ruta más corta entre dos ciudades de la República Mexicana. El programa solicita al usuario la ciudad de origen y la ciudad de destino, y muestra la ruta más corta entre ambas ciudades utilizando los algoritmos de búsqueda implementados con un menú de selección.

    Ejecución del programa
        Opcion 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python main.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar

    Entradas:
        matrix.csv = archivo csv con la matriz de adyacencia del grafo
        nodes.csv = archivo csv con los nodos del grafo
        nodo de inicio y nodo final

'''

### DEPENDENCIAS ###
import graph_creation as graph
import get_euclidean_distance as heuristic
import greedy_best_first as gbf

#Menú de selección de algoritmos: 0.5 pts
#Tiempo de ejecución de cada algoritmo: 0.25 pts
#Solicitud de parámetros de los algoritmos al usuario: 0.25 pts
#Implementación de la distancia Haversine: 0.5 pts
#Solicitud y ejecución de cada algoritmo con y sin información paso a paso: 0.5 pts
#Algoritmos (3 de 5 pts):
#Greedy best-first
#A*
#Weighted A*
#Beam
#Steepest hill climbing
#Stochastic hill climbing
#Simulated annealing
#Genetic algorithms

def menu():

    print("--¿Qué algoritmo quiere utilizar?--")
    print("1. Greedy Best-First Search")
    print("2. Weighted A* Search")
    print("3. A* search")
    print("4. Beam Search (The Original algorithm)")
    print("5. Steepest Ascent Hill Climbing Search")
    print("6. Stochastic Hill Climbing Search")
    print("7. Branch and bound")
    print("8. Simulated Annealing")
    print("9.Terminar")
    opc = input("Introduzca la opción deseada (1-9): ")
    return opc

# main
#   Método que crea un Graph con los archivos csv y ejecuta los algoritmos de búsqueda
# Sin entrada
def main():
    log = True

    # Se crea un grafo con archivos csv
    mexico_graph = graph.csv_to_graph('matrix.csv', 'nodes.csv')

    # Se obtiene una lista de tuplas con el grafo
    mexico_tree = mexico_graph.get_tuples()
    if log: 
        print("Mexico Tree: " + str(mexico_tree))

    # Se define el nodo de inicio y el nodo meta
    start = "CANCUN"
    goal = "CUERNAVACA"

    # Se obtiene una lista con las heurísticas 
    heuristics = heuristic.calcular_heuristica_distancia_de_linea_recta(goal)
    if log: 
        print("Heuristics: " + str(heuristics))

    gbf_queue = gbf.greedy_best_first(mexico_tree, start, goal, heuristics)
    print(gbf_queue)
    # menu = algorithms.algorithms_menu(mexico_tree, heuristic_list, start, goal)
    #mandamos llamar el primer método
    # print('PATH: ',menu.greedy_bestfirst())
    # print('PATH: ',menu.a_star())

main()
