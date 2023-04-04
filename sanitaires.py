import json
import networkx as nx
from geopy.distance import geodesic
import folium

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

# Créer une carte centrée sur Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=13)

# Ajouter des marqueurs pour chaque station
for toilette in data:
    name = toilette['station']
    lat = toilette['coord_geo']['lat']
    lon = toilette['coord_geo']['lon']
    folium.Marker([lat, lon], tooltip=name).add_to(m)

# Dessiner le chemin hamiltonien en rouge
coordinates = [coords[node] for node in hamiltonian_path]
folium.PolyLine(coordinates, color='red', weight=2).add_to(m)

# Trouver tous les plus courts chemins entre toutes les paires de nœuds
for source in G.nodes:
    for target in G.nodes:
        if source != target:
            for path in nx.algorithms.shortest_paths.all_shortest_paths(G, source=source, target=target, weight='weight'):
                coordinates = [coords[node] for node in path]
                folium.PolyLine(coordinates, color='black', weight=1).add_to(m)
(m)

# Afficher la carte
m.save('sanitaires-reseau-ratp.html')
