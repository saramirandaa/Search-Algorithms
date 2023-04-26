
def steepest_hill_climbing(tree, start, goal, heuristic):
        #we initialize our current node with the starting node 
        current_node = start
        #initialize our visited nodes list with a set function which will allow us to 
        #not repeat the nodes 
        visited = set()

        #while our current node has not arrived to the goal node 
        while current_node != goal:
            #we add our node to the visited list
            visited.add(current_node)

            childs = [node_tuple[1] for node_tuple in tree if node_tuple[0] == current_node]
            best_child = None
            #we initialize the best cost with a very high number (infinity) in order to get through the first if
            best_cost = float('inf')
            #we iterate through the childs of the current node
            for child in childs:
                #if the child is not in our queue and its smaller than the last one 
                # the child will be the best child and will get its heuristic as the 
                if heuristic[child] < best_cost and child not in visited:
                    best_child = child
                    best_cost = heuristic[child]
            #if we never find a best child we return an empty path
            if not best_child:
                return None
            #else our current node will be the best child
            current_node = best_child
        #we create a list with the goal as the beginning
        path = [goal]
        #until the last node is the node we set as the start node we get into a cycle
        while path[-1] != start:
            #for every node in a tree we iterate 
            for node_tuple in tree:
                #if the node is the last in the path we add the parent to the list
                if node_tuple[1] == path[-1]:
                    path.append(node_tuple[0])
                    break
        #we reverse the list in order to get the path from the start to the goal
        path.reverse()
        return path
