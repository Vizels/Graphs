class Adjacency_list:
    
    adjlist = []

    def __init__(self, size = 0):
        for i in range(size):
            self.adjlist.append([])

    def __del__(self):
        self.adjlist = None

    def add_edge(self, node, *other_nodes):
        for i in other_nodes:
            if i not in self.adjlist[node]:
                self.adjlist[node].append(i)
    
    def remove_edges(self, node, *other_nodes):
        for i in other_nodes:
            self.adjlist[node].remove(i)
    
    def print_graph(self):
        for i in range(len(self.adjlist)):

            print("Node {} is connected to: ".format(i), end='')

            for j in self.adjlist[i]:
                print(j, end=' ')

            print('')
        print('\n')

    def are_connected(self, node_from, node_to, visited = None):
        if visited is None:
            visited = set()

        visited.add(node_from)

        if node_from == node_to:
            return True
        
        for i in self.adjlist[node_from]:
            if i not in visited:
                if self.are_connected(i, node_to, visited):
                    return True

        return False