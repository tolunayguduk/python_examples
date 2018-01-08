import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(100,0.015)
options = {"node_color": 'red', 'node_size':500, 'width' :1, 'with_labels':True}
nx.draw_random(G,**options)

for n in G.neighbors(5):
    for m in G.neighbors(n):
        print(m)

plt.show()

