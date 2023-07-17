class Edge_list:
    edglist = []

    def __del__(self):
        self.edglist = None

    def add_edge(self, node_from, node_to):
        if [node_from, node_to] not in self.edglist:
            self.edglist.append([node_from, node_to])
    
    def remove_edge(self, node_from, node_to):
        self.edglist.remove([node_from, node_to])

    def print_list(self):
        for i in self.edglist:
            print(i)

    def are_connected(self, node_from, node_to, visited=None):
        if visited is None:
            visited = set()

        visited.add(node_from)

        if node_from == node_to:
            return True
                
        for edge in self.edglist:
            if edge[0] == node_from and edge[1] not in visited:
                if self.are_connected(edge[1], node_to, visited):
                    return True

        return False