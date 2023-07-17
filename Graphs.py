import edge_list as el
import adjacency_list as al
import adjacency_matrix as am
import random
import sys
import time
import pandas as pd
from pympler import asizeof

#increase recursion limit for graph_size > 1000
sys.setrecursionlimit(10000)

size = 1000 # graph size


# be careful about this string, don't recommend to use more than 100 if your graph size >= 1000.
# Maybe somewhere there are memory leaks, but i have no idea where. If you know where it can be, go create a fork :)
number_of_tests = 10 

print_memory = True


def fill_graphs_randomly(edges_num, *graphs):
    for _ in range(edges_num):
        node1 = random.randint(0,size-1)
        node2 = random.randint(0,size-1)

        for graph in graphs:
            graph.add_edge(node1, node2)


def graph_time_test_DFS(*graphs):
    test_time = []

    node_from = random.randint(0, size-1)
    node_to = random.randint(0, size-1)

    for i in graphs:
        print("Graph: ", i)
        time1 = time.time()
        print(i.are_connected(node_from, node_to))
        time2 = time.time()

        test_time.append(time2-time1)
    
    return test_time



test_time = []

# main driver for tests
for i in range(number_of_tests):
    el_test = el.Edge_list()
    al_test = al.Adjacency_list(size)
    am_test = am.Adjacency_matrix(size)

    if print_memory:
        print(asizeof.asizeof(el_test.edglist))
        print(asizeof.asizeof(al_test.adjlist))
        print(asizeof.asizeof(am_test.matrix))

    graph_list = (el_test, al_test, am_test)
    #print("Loop ", i) # debug 
    fill_graphs_randomly(size*2, *graph_list)

    if print_memory:
        print(asizeof.asizeof(el_test.edglist))
        print(asizeof.asizeof(al_test.adjlist))
        print(asizeof.asizeof(am_test.matrix))

    test_time.append(graph_time_test_DFS(*graph_list))

    

    del el_test, al_test, am_test


df = pd.DataFrame(test_time)
df.columns = ['Edge list', 'Adjacency list', 'Adjacency Matrix']

df.to_csv("Output.csv", index=False)