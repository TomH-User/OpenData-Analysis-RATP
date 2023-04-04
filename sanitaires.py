import json
import networkx as nx
from geopy.distance import geodesic
import matplotlib.pyplot as plt

# Charger les données JSON
with open('sanitaires-reseau-ratp.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Créer un graphe en utilisant les coordonnées géographiques
G = nx.Graph()

# Dictionnaire pour stocker les coordonnées de chaque station
coords = {}

# Parcourir les données et ajouter les nœuds et les arêtes au graphe
for toilette in data:
    name = toilette['station']
    lon = toilette['coord_geo']['lon']
    lat = toilette['coord_geo']['lat']
    coords[name] = (lat, lon)
    G.add_node(name, coords=(lat, lon))
    for other_name, other_coords in coords.items():
        if name != other_name:
            distance = geodesic(coords[name], other_coords).m
            G.add_edge(name, other_name, weight=distance)

# Trouver le chemin hamiltonien avec le plus court chemin
hamiltonian_path = nx.algorithms.approximation.traveling_salesman.traveling_salesman_problem(G, weight='weight')

# Calculer la distance totale du chemin hamiltonien
total_distance = 0
for i in range(len(hamiltonian_path)-1):
    total_distance += G[hamiltonian_path[i]][hamiltonian_path[i+1]]['weight']
total_distance += G[hamiltonian_path[-1]][hamiltonian_path[0]]['weight']

# Dessiner le graphe
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=10)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='lightblue', alpha=0.2)
nx.draw_networkx_edges(G, pos, edgelist=[(hamiltonian_path[i], hamiltonian_path[i+1]) for i in range(len(hamiltonian_path)-1)],
                       edge_color='red', width=2)
plt.axis('off')
plt.title(f"Distance totale: {total_distance:.2f}m")
plt.show()

