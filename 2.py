import matplotlib.pyplot as plt

import networkx as nx

G=nx.Graph()

G.add_edge(1,2)
G.add_edge(1,8)
G.add_edge(2,3)
G.add_edge(2,8)
G.add_edge(3,4)
G.add_edge(3,8)
G.add_edge(4,7)
G.add_edge(4,9)
G.add_edge(5,6)
G.add_edge(5,7)
G.add_edge(7,8)


def bfs_fired(G, start, fired):
    Q=[start]
    fired.add(start)
    while len(Q)!=0:
        current= Q.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Q.append(neighbour)

fired=set()
bfs_fired(G, 1, fired)
print(fired)
i = 0
for x in G.nodes():
    if x not in fired:
        i+=1
if i==0:
    print('Граф связный')
else:
    print('Граф не связный')
