from math import inf
from collections import defaultdict


class Graph:
    W = 0  # Largest Weight
    V = 0  # Number of Vertices

    def __init__(self, V: int) -> None:
        self.g = defaultdict(list)
        self.V = V

    def addEdge(self, x, y, w):
        self.g[x].append([y, w])
        if w > self.W:
            self.W = w

    # Adds double edge to the graph
    def addDEdge(self, x, y, w):
        self.g[x].append([y, w])
        self.g[y].append([x, w])
        if w > self.W:
            self.W = w

    def shortestPath(self, src: int):
        distance = defaultdict(lambda: inf)
        distance[0] = 0
        Bucket = [[] for i in range(self.W*V+1)]
        Bucket[0].append(src)
        index = 0
        while 1:
            # finding the first not empty slot
            while (len(Bucket[index]) == 0 and index < self.W*V):
                index += 1
            # If all buckets are empty, we are done.
            if (index == self.W * V):
                break
            node = Bucket[index].pop(0)
            # looping through each edge going out of that node
            for ed in self.g[node]:
                v = ed[0]
                weight = ed[1]
                dv = distance[v]
                dnode = distance[node]
                if dnode + weight < dv:
                    if dv != inf:
                        Bucket[dv].remove(v)
                    distance[v] = dnode + weight
                    dv = dnode + weight
                    Bucket[dv].append(v)
                    # put the iterator pointing to the node
        for k, value in distance.items():
            print(f'{k} -- {value}')


if __name__ == "__main__":

    V = 9  # number of vertices(nodes)
    # g = defaultdict(list)

    # simple graph with one direction edges
    G1 = Graph(6)
    G1.addEdge(0, 1, 2)
    G1.addEdge(0, 2, 4)
    G1.addEdge(1, 2, 1)
    G1.addEdge(1, 3, 4)
    G1.addEdge(1, 4, 2)
    G1.addEdge(2, 4, 3)
    G1.addEdge(3, 5, 2)
    G1.addEdge(4, 3, 3)
    G1.addEdge(4, 5, 2)
    print('Path map for graph 1 :')
    G1.shortestPath(0)
    # Double direction edges

    G2 = Graph(9)
    G2.addDEdge(0, 1, 4)
    G2.addDEdge(0, 7, 8)
    G2.addDEdge(1, 2, 8)
    G2.addDEdge(1, 7, 11)
    G2.addDEdge(2, 3, 7)
    G2.addDEdge(2, 8, 2)
    G2.addDEdge(2, 5, 4)
    G2.addDEdge(3, 4, 9)
    G2.addDEdge(3, 5, 14)
    G2.addDEdge(4, 5, 10)
    G2.addDEdge(5, 6, 2)
    G2.addDEdge(6, 7, 1)
    G2.addDEdge(6, 8, 6)
    G2.addDEdge(7, 8, 7)

    print('Path map for graph 2 : ')
    G2.shortestPath(0)
