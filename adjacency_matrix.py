class Adjacency_matrix:
    
    matrix = [[]]

    def __init__(self, size = 0):
        self.size = size
        for i in range(size):
            for _ in range(size):
                self.matrix[i].append(0)
            self.matrix.append([])
            
    def __del__(self):
        self.matrix = None

    def add_edge(self, node1, node2, edge_weight = 1):
        self.matrix[node1][node2] = edge_weight

    def remove_edge(self, node1, node2):
        self.matrix[node1][node2] = 0


    def get_edge(self, node1, node2):
        return self.matrix[node1][node2]

    def print_edges(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != 0:
                    print("{} -> {}, weight = {}".format(i, j, self.matrix[i][j]))

    def print_matrix(self):
        print('Matrix: ')
        for i in range(self.size):
            print(self.matrix[i])
        print('')


    def find_node(self, node_number):
        print("Node number {} is connected with nodes: ".format(node_number), end='')
        for i in range(self.size):
            if self.matrix[node_number][i] != 0:
                print(i, end=' ')

    def are_connected(self, node_from, node_to, visited=None):  # DFS
        if visited is None:
            visited = set()

        visited.add(node_from)

        if node_from == node_to:
            return True

        for i in range(self.size):
            if self.matrix[node_from][i] != 0 and i not in visited:
                if self.are_connected(i, node_to, visited):
                    return True

        return False