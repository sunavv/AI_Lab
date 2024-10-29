import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([("Bird", "Animal"), ("Canary", "Bird"), ("Canary", "Yellow")])

nx.draw(G, with_labels=True)
plt.show()
