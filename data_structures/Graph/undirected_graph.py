graph = {}

def add_node(vertex):
    if vertex in graph:
        print(f"{vertex} is already present in graph.")
    else:
        graph[vertex] = []

def add_edge(vertex1, vertex2):
    if vertex1 not in graph:
        print(f"{vertex1} is not present in the graph.")
    elif vertex2 not in graph:
        print(f"{vertex2} is not present in the graph.")
    else:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

def delete_node(vertex):
    if vertex not in graph:
        print(f"{vertex} is not present in the graph.")
    else:
        graph.pop(vertex)
        for i in graph:
            list_ = graph[i]
            if vertex in list_:
                list_.remove(vertex)

def delete_edge(vertex1, vertex2):
    if vertex1 not in graph:
        print(f"{vertex1} is not present in the graph.")
    elif vertex2 not in graph:
        print(f"{vertex2} is not present in the graph.")
    else:
        if vertex2 in graph[vertex1]:
            graph[vertex1].remove(vertex2)
            graph[vertex2].remove(vertex1)

def count_node():
    list_ = []
    for i in graph:
        list_.append(i)
    print(f"Number of Nodes: {len(list_)}")

# Run Code: 
 
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B")
add_edge("B","C")
print(graph)

# delete_node("A")
delete_edge("B", "C")
print(graph)

count_node()