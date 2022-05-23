# Python Program for Floyd Warshall Algorithm
# Number of vertices in the graph
V = 4
# Value used for unconnected Vertices
INF = 9999
# A print function
def print_matrix(d_matrix):
    print ("Following matrix shows the shortest distances between every pair of vertices")
    for row in range(V):
        for col in range(V):
            if(d_matrix[row][col] == INF):
                print ("%3s" % ("INF"),end=" ")
            else:
                print ("%3d\t" % (d_matrix[row][col]),end=" ")
            if col == V-1:
                print () 
# Floyd Warshall Algorithm
def floydWarshall(graph):
    d_matrix = list(map(lambda row: list(map(lambda col: col, row)), graph))
    #choose each node as intermediate one by one
    for node in range(V):
        # pick all vertices as source one by one
        for row in range(V):
            # Pick all vertices as destination for the current source
            for col in range(V):
 
                # If new path with intermediate source less
                #than current path ==> Update the element
                d_matrix[row][col] = min(d_matrix[row][col],d_matrix[row][node]+d_matrix[node][col])
    print_matrix(d_matrix)
 

#Create a Graph
graph = [[0, 3, INF, 7],
         [8, 0, 2, INF],
         [5, INF, 0,   1],
         [2, INF, INF, 0]]
# Print the solution
floydWarshall(graph)
