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

# Initialiser la distance totale à zéro
distance_totale = 0

# Ajouter les distances entre les nœuds consécutifs dans le chemin hamiltonien
for i in range(len(hamiltonian_path)-1):
    node1 = hamiltonian_path[i]
    node2 = hamiltonian_path[i+1]
    edge_data = G.get_edge_data(node1, node2)
    edge_distance = edge_data['weight']
    distance_totale += edge_distance

# Afficher la distance totale en kilomètres
distance_totale_km = distance_totale / 1000
print("Distance totale du chemin hamiltonien :", distance_totale_km, "kilomètres")



# Dessiner le graphe
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=10)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', alpha=0.2)
nx.draw_networkx_edges(G, pos, edgelist=[(hamiltonian_path[i], hamiltonian_path[i+1]) for i in range(len(hamiltonian_path)-1)],
                       edge_color='red', width=2)
plt.axis('off')
plt.show()

