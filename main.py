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
import time
import graph_creation as graph
import get_euclidean_distance as heuristic
import greedy_best_first as gbf
import a_star
import weighted_a_star as wa_star
import simulated_annealing as sa
import steepest as shc

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

### VARIABLES GLOBALES ###
# log (bool) - variable que indica si se imprime información de depuración
log = True

### FUNCIONES COMPLEMENTARIAS ###
# ask_log
#   Método que pregunta al usuario si desea imprimir información de depuración
# Sin entrada
# Salida: log (bool) - variable que indica si se imprime información de depuración
def ask_log():
    global log
    log = input("¿Desea imprimir información de depuración? (y/n): ")
    if log == "y" or log == "Y":
        log = True
    else:
        log = False

# menu
#   Método que imprime un menú de selección de algoritmos
# Sin entrada
# Salida: opc (int) - opción seleccionada por el usuario
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
    opc = int(input("Introduzca la opción deseada (1-9): "))
    return opc

### FUNCIÓN PRINCIPAL ###
# main
#   Método que crea un Graph con los archivos csv y ejecuta los algoritmos de búsqueda
# Sin entrada
def main():
    # Se pregunta al usuario si desea imprimir información de depuración
    ask_log()

    # Se crea un grafo con archivos csv
    mexico_graph = graph.csv_to_graph('matrix.csv', 'nodes.csv')

    # Se obtiene una lista de tuplas con el grafo
    mexico_tree = mexico_graph.get_tuples()
        
    # Se define el nodo de inicio y el nodo meta
    start = "CANCUN"
    goal = "DURANGO"

    # Se obtiene una lista con las heurísticas 
    heuristics = heuristic.calcular_heuristica_distancia_de_linea_recta(goal)

    # Se imprime el grafo
    if log:
        print("Mexico Tree: " + str(mexico_tree) + "\n")
        print("Heuristics: " + str(heuristics) + "\n")

    #a_star_queue = a_star.a_star(mexico_tree, start, goal, heuristics, log)
    #print(a_star_queue)

    # Se imprime el menú de selección de algoritmos
    opc = menu()
    print("Opción seleccionada: " + str(opc) + "\n")

    # Se obtiene el tiempo de inicio
    start_time = time.time()

    # Se ejecuta el algoritmo seleccionado
    if (opc == 1):
        print("Greedy Best-First Search")
        print(gbf.greedy_best_first(mexico_tree, start, goal, heuristics, log = log))
    elif (opc == 2):
        print("Weighted A* Search")
        print(wa_star.weighted_a_star(mexico_tree, start, goal, heuristics, log = log))
    elif (opc == 3):
        print("A* search")
        print(a_star.a_star(mexico_tree, start, goal, heuristics, log = log))
    elif (opc == 4):
        print("Beam Search (The Original algorithm)")
        # BEAM
        pass
    elif (opc == 5):
        print("Steepest Ascent Hill Climbing Search")
        print(shc.steepest_hill_climbing(mexico_tree, start, goal, heuristics))
    elif (opc == 6):
        print("Stochastic Hill Climbing Search")
        # STOCHASTIC
        pass
    elif (opc == 7):
        print("Branch and bound")
        # BRANCH AND BOUND
        pass
    elif (opc == 8):
        print("Simulated Annealing")
        print(sa.simulated_annealing(mexico_tree, start, goal, heuristics, log = log))
    elif (opc == 9):
        print("Terminando...")
        exit()

    # Se obtiene el tiempo de fin
    end_time = time.time()
    print("Tiempo de ejecución con entrada de usuario: " + str(end_time - start_time) + " segundos")
    print()

    # Se repite el menú de selección de algoritmos
    main()

main()