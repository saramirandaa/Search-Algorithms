### INFORMACIÓN GENERAL ###
'''
    Proyecto de Segundo Parcial
    Universidad Panamericana
    Clase de Inteligencia Artificial
    Sara Miranda, Christian Matos, Dania Venegas
    22-marzo-2023
    Versión 0.2.0

    El presente código define una clase que contiene los nodos y la matriz de adyacencia y una función que crea el grafo a partir de un archivo csv para su uso como biblioteca.

    Ejecución del programa
        Opcion 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python graph_creation.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar
'''
### DEPENDENCIAS ###
import csv

### FUNCIONES O CLASES DE APOYO ###

# Graph
#   Clase que contiene los nodos y la matriz de adyacencia
# Entrada:
#   nodes = lista de nodos
#   graph_matrix = matriz de adyacencia
# Métodos:
#   get_tuples() = regresa una lista de tuplas con las conexiones de los nodos
#   get_weights() = regresa una lista con los pesos de las conexiones
#   get_tuples_weights() = regresa una lista de listas con las conexiones y sus pesos
class Graph:
    # Constructor de la clase
    def __init__(self, matrix, nodes):
        self.matrix = matrix
        self.nodes = nodes

        # Se generan tuplas con los nodos y sus conexiones
        self.formed_nodes = []
        self.weights = []
        self.nodes_and_weigths = []

        # Se recorre la matriz de adyacencia
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                # Si el valor de la matriz es diferente de 0, se agrega a la lista de tuplas
                if self.matrix[y][x] != 0:
                    # Aquí se hace una lista de tuplas con los nodos
                    self.formed_nodes.append((self.nodes[y], self.nodes[x]))
                    # Aquí se hace una lista con los pesos
                    self.weights.append(self.matrix[y][x])
                    #Aquí se hace una lista con los nodos y su peso
                    self.nodes_and_weigths.append([self.formed_nodes[y], self.matrix[y][x]]) 

    def get_tuples(self):
        return self.formed_nodes
    
    def get_weights(self):
        return self.weights
    
    def get_tuples_weights(self):
        return self.nodes_and_weigths


# csv_to_graph
#   Función que lee los archivos csv y los convierte en un Graph
# Entrada:
#   matrix_file = archivo csv con la matriz de adyacencia
#   nodes_file = archivo csv con los nombres de los nodos
# Salida:
#   Graph con los nodos y la matriz de adyacencia
def csv_to_graph(matrix_file, nodes_file):
    # Se inicializan las listas
    matrix = []
    nodes = []

    # Se lee el archivo csv de la matriz de adyacencia
    with open(matrix_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cStr = ",".join(row)
            cStr2 = cStr.split(',')
            A = [int(x) for x in cStr2]
            matrix.append(A)
            del cStr2, A
    # Se lee el archivo csv de los nodos
    with open(nodes_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader: 
            nodes.append(row)  

    # Se convierten de string a lista
    nodesStr = "".join(nodes[0])
    nodes = nodesStr.split(',')
    nodes_copy = nodes.copy()
    nodes.clear()
    for name in nodes_copy:
        nodes.append(name.upper())

    # Se crea el grafo
    graph = Graph(matrix, nodes)
    return graph