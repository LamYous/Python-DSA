graph = {}

def add_node(vertex):
    if vertex in graph:
        print(f"{vertex} is already present in graph.")
    else:
        graph[vertex] = []

def add_edge(vertex1, vertex2, weight):
    if vertex1 not in graph:
        print(f"{vertex1} is not present in the graph.")
    elif vertex2 not in graph:
        print(f"{vertex2} is not present in the graph.")
    else:
        graph[vertex1].append([vertex2, weight])
        graph[vertex2].append([vertex1, weight])

def delete_node(vertex):
    if vertex not in graph:
        print(f"{vertex} is not present in the the graph")
    else:
        graph.pop(vertex)
        for i in graph:
            for j in graph[i]:
                if vertex == j[0]:
                    graph[i].remove(j)
                    break

def delete_edge(vertex1, vertex2, weight):
    if vertex1 not in graph:
        print(F"{vertex1} is not in the graph")
    elif vertex2 not in graph:
        print(f"{vertex2} is not in the graph")
    else:
        if vertex2 in graph[vertex1]:
            graph[vertex1].remove(vertex2, weight)
            graph[vertex2].remove(vertex1, weight)


add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("B", "C", 5)
print(graph)

# delete_node("A")

delete_edge("A","B",10)
print(graph)