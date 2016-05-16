import matplotlib.pyplot as plt

import networkx as nx

G=nx.Graph()
Tree=nx.Graph()

G.add_edge(1,2, weight=1)
G.add_edge(1,8, weight=2)
G.add_edge(2,3, weight=3)
G.add_edge(2,8, weight=4)
G.add_edge(3,4, weight=5)
G.add_edge(3,8, weight=6)
G.add_edge(4,7, weight=7)
G.add_edge(4,9, weight=8)
G.add_edge(5,6, weight=9)
G.add_edge(5,7, weight=10)
G.add_edge(7,8, weight=11)

def dej(G, start):
    shortest_path={vertex: float('+inf') for vertex in G}
    shortest_path[start]=0
    Q=[start]
    while Q:
        current = Q.pop(0)
        for neighbour in G[current]:
            offering_path = shortest_path[current]+ G[current][neighbour]
            if offering_path < shortest_path[neighbour]:
                shortest_path[neighbour]=offering_path
                Q.append(neighbour)
    return shortest_path

for node in G:
    print(G.node, dej(G, 1))
