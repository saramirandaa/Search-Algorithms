def a_star(tree, start, goal, heuristic):
    #we initialize a queue with the starting node and with 
    queue = [(0, start)]
    #we create a came from dictionary which will tell us the path we took
    came_from = {}
    #we create another dictionary which will tell us the costs of the nodes
    cost_so_far = {}
    #we initialize the dictionary of the starting node with an empty cost       
    came_from[start] = None
    #we initialize the dictionary of the starting node with a cost of 0
    cost_so_far[start] = 0
    
    #while our queue is not empty we start searching for the node with the lowest cost 
    while queue:
        #initialize the current node with the starting node
        current_node = queue[0][1]
        queue = queue[1:]
        
        if current_node == goal:
            break
        
        node_childs = [node_tuple[1] for node_tuple in tree if node_tuple[0] == current_node]
        
        for child in node_childs:
            new_cost = cost_so_far[current_node] + 1 # assuming a uniform cost of 1 for all edges
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost + heuristic[child]
                queue.append((priority, child))
                queue.sort()
                came_from[child] = current_node
    
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    
    return path