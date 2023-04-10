<h1>OpenData-Analysis-RATP</h1>

<h3>Objectif :</h3>
Visualiser les parcours des agents d'entretien, optimiser leurs itinéraires et la planification des tâches de nettoyage en fonction de l'accessibilité des zones et des temps de parcours.

<h3> Méthodologie </h3>

- Chargement des données de sanitaire publiques à Paris depuis un fichier JSON
(disponible <a href="https://data.ratp.fr/explore/dataset/sanitaires-reseau-ratp/information/?location=10,48.85478,2.41287&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InNhbml0YWlyZXMtcmVzZWF1LXJhdHAiLCJvcHRpb25zIjp7fX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJDT1VOVCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibGlnbmUiLCJtYXhwb2ludHMiOjUwLCJzb3J0IjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D">ici</a>).

- Construction d'un graphe pondéré basé sur les coordonnées géographiques de chaque sanitaire.

- Implémentation de l'algorithme permettant de trouver le chemin hamiltonien le plus court pour visiter toutes les sanitaires.

- Représentation par dessus la carte d'Île de France du graphe avec les marqueurs pour chaque sanitaires et du chemin hamiltonien en rouge.

- Sauvegarde de la carte générée sous forme d'un fichier HTML.
