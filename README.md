<h1>OpenData-Analysis-RATP</h1>

<h3>Objectif</h3>

Développement d'un script permettant de visualiser l'ensemble des parcours potentiels des agents d'entretien de la RATP et optimiser la planification de leurs itinéraires. <br>

<p align="center" float="left" >
  <img width=480 src="https://user-images.githubusercontent.com/73723037/230899469-e30a5204-9e38-4e03-b1ab-7f100e24a5b1.JPG"> <br>
  <img width=500 src="https://user-images.githubusercontent.com/73723037/230898956-a7ec43ab-544b-4a39-8043-8de421508064.JPG"> <br>
  <img width=550 src="https://user-images.githubusercontent.com/73723037/230899030-3fe02677-8d7f-4d22-9f54-ce686e699940.JPG"> <br>
</p>

<h3> Méthodologie </h3>

- Chargement des données de sanitaire publiques à Paris depuis le fichier JSON disponible <a href="https://data.ratp.fr/explore/dataset/sanitaires-reseau-ratp/information/?location=10,48.85478,2.41287&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InNhbml0YWlyZXMtcmVzZWF1LXJhdHAiLCJvcHRpb25zIjp7fX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJDT1VOVCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibGlnbmUiLCJtYXhwb2ludHMiOjUwLCJzb3J0IjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D">ici</a>.

- Construction d'un graphe pondéré basé sur les coordonnées géographiques de chaque sanitaire.

- Implémentation de l'algorithme permettant de trouver le chemin hamiltonien le plus court pour visiter toutes les sanitaires.

- Représentation par dessus la carte d'Île de France du graphe avec les marqueurs pour chaque sanitaires et du chemin hamiltonien en rouge.

- Sauvegarde de la carte générée sous forme d'un fichier HTML.

<h3> Bibliothèques utilisées </h3>

- NetworkX

- Folium
