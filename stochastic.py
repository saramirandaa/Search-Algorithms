import random 

def stochastic_hill_climbing(tree, start, goal, heuristic):
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
            for child in childs:
                cost = heuristic[child]
                #if the cost (the node's heuristic) is smaller or equal than the best cost and the child is not in the visited list
                if cost <= best_cost and child not in visited:
                    #it the cost is smaller than the best one we replace it by that one 
                    if cost < best_cost:
                        best_child = [child]
                        best_cost = cost
                    else:
                        best_child.append(child)
            #if we never find a best child we return an empty path
            if not best_child:
                return None
            #else we choose a random child from the best childs
            current_node = random.choice(best_child)
            iterations += 1

        if current_node != goal:
            return None

        #if the current node is the goal we shall create another list in which 
        #we will be searching its parents until arriving to the starting node
        path = [goal]
        while path[-1] != start:
            for node_tuple in tree:
                if node_tuple[1] == path[-1]:
                    path.append(node_tuple[0])
                    break
        path.reverse()

        return path