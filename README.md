# SmartRUBIK

## NOTICE D'UTILISATION
**Comment lancer le SMART RUBIK ?**
- 1 : Avant de mettre sous tension la jetson nano, brancher les caméras.
- 2 : Brancher l'arduino nano sur n'importe quel port de la jetson nano
- 3 : Mettre sous-tension la jetson
- 4 : Se connecter à la jetson via le protocole ssh en utilisant MobaXterm ET -X afin de visualiser les fenêtres qui apparaîtront sur l'écrans (caméras, IHM)
    EXEMPLE : ssh -X jetsonX@192.168.XX.XX
    
*Les étapes 5 et 6 ne sont à faire qu'une fois, pour la première installation !*    
- 5 : Cloner le répértoire GitHub sur lequel vous êtes actuellement
- 6 : Créer un container en suivant les instructions du readme.md du répository https://github.com/nlpTRIZ/jetson_docker_X_forwarding

- 7 : Lancer le container buildé à la racine du répertoire GitHub que vous venez de cloner --> COMMANDE : drun -c {container_name}
- 8 : Dans le dossier src/camera : lancer les programes :
    - "VerificationCamera.py" pour vérifier que les caméras soient bien détectées
    - "Initialisation_camera.py" pour vérifier que les caméras sont correctement placées
- 9 : Lancer le programme "Programme Principal" du dossier src pour avoir l'IHM



## Déscription du code
**Créé à partir de https://github.com/nlpTRIZ/jetson_docker_X_forwarding**

## En supplément des bibliothèques présentes depuis le lien github ci-dessus, le docker du projet SmartRubik contient :
- Streamlit (Pour l'IHM)
- Vpython (visualisation jumeau numérique)
- openCV (traitement de l'image)
- Pyserial (communication avec l'arduino Nano)
- tkinter (gestionnaire de fenêtre)
- kociemba (résolution du rubik's cube)

# Dossier Data
## Dans le dossier Data se trouve les fichiers autre que du code :
- Images nécessaire pour l'affichage du Programme principal (IHM)
- Données nécessaire pour le réseau de neuronne (résolution du rubik's cube)

# Dossier src
## 3 parties distinctes : caméra, réseau de neuronne, solveur et pg principal
### Caméra :
3 programmes sont présents :
- Initialisation_camera.py : à lancer pour vérifier que les caméras sont correctement placées
- placements_points : sous-programme lancer par Programme_principal pour avoir la vision
- VerificationCamera : pour vérifier que les caméras soient bien détectées

But de la visualisation :
- En entrée  : une capture de l'état du rubik's cube via les caméras 
- En sortie : 
    - la chaîne de définition du rubik's cube (rubik_str) --> voir 'cube string notation' dans https://github.com/muodov/kociemba
    - Une image des couleurs des faces récupérées par le cube
### Réseau de neuronne :  
- Main.py et Trainer.py :
Programme principal du réseau de neurone. NN créé à partir de Pytorch et programmation orienté objet.
- Dans le dossier generate_data : 
scrambleImage.py : sous programme générant à partir d'une chaîne de mouvements le cube mélangé.
scrambleGenerator.py : programme main à lancer pour recréer le Dataset enregistré dans /data/Creation_Data/Data.csv
- Paramètres d'entrée : 
nombre de combinaison présente dans le Dataset (nb_dataset)
nombre de mouvements pour chaque combinaison (nb_mvt)
le choix de résolution : via les mouvements inverse généré ou via la bibliothèque Kociemba
Code inspiré du github https://github.com/BenGotts/Python-Rubiks-Cube-Scrambler/tree/f3f717b9c6039a0113b6369e741c35c27f10516a
- Dans le dossier models :
Modèle du réseau de neurone
- Dans le dossier preprocess :
Sous-programme de traitement des données d'entrée 
### Solveur
Sous-programme pour résoudre le cube via la bibliothèque Kociemba

### Programmes principal : 
- Affiche l'interface homme machine pour mélanger le rubik's cube, effectuer des mouvements manuellement, résoudre le rubik's cube




## Les axes d'amélioration pour les prochaines années
- 1 --> Améliorer l'IHM :
    - Boutons à refaire
    - Fonction moteur à modifier (front ne correspond pas au front, etc...) 
- 2 --> Améliorer la vision pour avoir plus de précision 
    - Modifcation des points de prise de couleurs
    - Changement de caméra ? Manque de rapidité, de contraste ou de luminosité ?
- 3 --> Vérifier l'implémentation du réseau de neuronne dans la fonction "c_solve" :
    - Prise d'information de la Rubik string par correctement automatisé
    - Boucle while à revoir ?




