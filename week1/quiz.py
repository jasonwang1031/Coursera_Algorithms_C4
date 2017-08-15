def bellman_ford(graph, source):
    global has_cycle

    distance, predecessor = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                compare(u, v, graph, distance, predecessor)

    # check for negative cycles
    for u in graph:
        for v in graph[u]:
            if distance[v] > distance[u] + graph[u][v]:
                has_cycle = True

    return distance, predecessor

def initialize(graph, source):
    destination = {}
    predecessor = {}
    for vertice in graph:
        destination[vertice] = float('Inf')
        predecessor[vertice] = None
    destination[source] = 0
    return destination, predecessor

def compare(vertice, previous, graph, distance, predecessor):
    if distance[previous] > distance[vertice] + graph[vertice][previous]:
        distance[previous] = distance[vertice] + graph[vertice][previous]
        predecessor[previous] = vertice

def getSmallest(distances, smallest):
    for idx in distances:
        if not smallest or distances[idx] < smallest:
            smallest = distances[idx]

    return smallest


if __name__ == "__main__":

    GRAPH_1_FILENAME = "g1.txt" 
    GRAPH_2_FILENAME = "g2.txt" 
    GRAPH_3_FILENAME = "g3.txt" 
    graphs = [GRAPH_1_FILENAME, GRAPH_2_FILENAME, GRAPH_3_FILENAME] 

    smallest = False

    for g in graphs:

        small = False
        has_cycle = False
        inFile = open(g, 'r') 

        num_vertices = 0
        num_edges = 0
        graph = {}
        vertices = []

        # initializing the graph with an array of edges [tale, head]
        for f in inFile:
            if(num_vertices == 0):
                num_vertices, num_edges = map(int, f.split())
            else: 
                tale, head, length = map(int, f.split())
                if tale not in vertices:
                    vertices.append(tale)
                if head not in vertices:
                    vertices.append(head)
                if tale not in graph:
                    graph[tale] = {}
                graph[tale][head] = length

        vertices = sorted(vertices)

        # adding vertices without outgoing edges
        for vertice in vertices:
            if vertice not in graph:
                graph[vertice] = {}

        for vertice in vertices:
            d, p = bellman_ford(graph, vertice)
            small = getSmallest(d, small)

        if has_cycle:
            continue
        elif not smallest or smallest > small:
            smallest = small


    if not smallest:
        print ('result: NULL')
    else:
        print ('result: ' + str(smallest))