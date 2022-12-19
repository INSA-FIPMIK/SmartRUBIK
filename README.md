# SmartRUBIK
## Créé à partir de https://github.com/nlpTRIZ/jetson_docker_X_forwarding

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
## 3 parties distinctes : le réseau de neuronne, le programme principal et la visualisation grâce aux caméras
### Programmes principal : affiche l'interface homme machine pour mélanger le rubik's cube, effectuer des mouvements manuellement, résoudre le rubik's cube

### Visualisation : interface de communication avec les caméras.
- En entrée  : une capture de l'état du rubik's cube
- En sortie : 
    la chaîne de définition du rubik's cube (rubik_str) --> voir 'cube string notation' dans https://github.com/muodov/kociemba
    Une image des couleurs des faces récupérées par le cube


### Dossier réseau de neuronne :         
- Dans le dossier creation_Data : 
    scrambleImage.py : sous programme générant à partir d'une chaîne de mouvements le cube mélangé.
    scrambleGenerator.py : programme main à lancer pour recréer le Dataset enregistré dans /data/Creation_Data/Data.csv
        Paramètres d'entrée : 
            nombre de combinaison présente dans le Dataset (nb_dataset)
            nombre de mouvements pour chaque combinaison (nb_mvt)
            le choix de résolution : via les mouvements inverse généré ou via la bibliothèque Kociemba

Code inspiré du github https://github.com/BenGotts/Python-Rubiks-Cube-Scrambler/tree/f3f717b9c6039a0113b6369e741c35c27f10516a
- Dans le dossier src:
    sous programme de Reseau_neurone_SUREL.py programmé en orienté objet
- Reseau_neurone_SUREL.py : réseau de neuronne prenant comme données d'entrainements et de test /data/Creation_Data/Data.csv généré par le scrambleGenerator.py
