#Aquí importé el archivo graph_creation.py para poder usar la clase graph que nos da los nodos 
# y sus conexiones, luego importé el código de apoyo en el que pasamos como parametro el 
# nodo final para poder calcular la heuristica
import graph_creation as graph
import get_euclidean_distance as heuristic

#Hice una clase que va a contener todos los algoritmos
# se pasa como parametros el grafo, la heuristica, el inicio y el fin
class algorithms_menu:
    def __init__(self, tree, heuristic, start, end):
        self.tree = tree
        self.heuristic = heuristic
        self.start = start
        self.goal = end

    def greedy_bestfirst(self):
        queue = [self.start]
        new_node = ''
        if self.start == self.goal:
            return queue
        
        while queue:
            current_node = queue[-1]
            min_node = 0
            
            if current_node == self.goal:
                return queue
            
            node_childs = [node_tuple[1] for node_tuple in self.tree if node_tuple[0] == current_node]    
            
            for child in node_childs:
                if child == self.goal:
                    queue.append(child)
                    return queue
                if self.heuristic[child]>min_node:
                    min_node = self.heuristic[child]
                    new_node = child

            if new_node not in queue:
                queue.append(new_node)
        
        return queue
    
    def a_star(self):

        queue = [(0, self.start)]
        came_from = {}
        cost_so_far = {}
        came_from[self.start] = None
        cost_so_far[self.start] = 0
        
        while queue:
            current_node = queue[0][1]
            queue = queue[1:]
            
            if current_node == self.goal:
                break
            
            node_childs = [node_tuple[1] for node_tuple in self.tree if node_tuple[0] == current_node]
            
            for child in node_childs:
                new_cost = cost_so_far[current_node] + 1 # assuming a uniform cost of 1 for all edges
                if child not in cost_so_far or new_cost < cost_so_far[child]:
                    cost_so_far[child] = new_cost
                    priority = new_cost + self.heuristic[child]
                    queue.append((priority, child))
                    queue.sort()
                    came_from[child] = current_node
        
        path = [self.goal]
        current = self.goal
        while current != self.start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        
        return path
    
    def weighted_a_star(self):
        pass
    def Beam(self):
        pass
    def Steepest_hill_climbing(self):
        pass
    def Stochastic_hill_climbing(self):
        pass
    def Simulated_Annealing(self):
        pass
    def Branch_Bound(self):
        pass
        
        
def main():
    #Aqui se manda llamar el grafo y nos da una lista de tuplas con todas las conexiones
    tree = graph.fgraph.get_Tuples()
    #print(tree)

    start = "CANCUN"
    goal = "MERIDA"

    #Aqui se manda llamar la heuristica con el goal, te da un diccionario con 
    #{la ciudad: heuristica}
    Pheuristic = heuristic.calcular_heuristica_distancia_de_linea_recta(goal)
    #print(Pheuristic)

    #se declara la clase y se le pasan los parámetros
    menu = algorithms_menu(tree, Pheuristic, start, goal)
    #mandamos llamar el primer método
    print('PATH: ',menu.greedy_bestfirst())
    print('PATH: ',menu.a_star())

    

main()




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