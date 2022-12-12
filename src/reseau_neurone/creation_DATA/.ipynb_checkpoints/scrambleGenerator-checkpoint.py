import random
import sys
from scrambleImage import scramble
import os
import csv
import numpy as np
import pandas as pd


'''Ce Programme genere aleatoirement un mouvement comprenant soit un ou 2 rotations'''


def gen_scramble(nb_mvt, moves, directions):
    # Make array of arrays that represent moves ex. U' = ['U', "'"]
    mvt_choisi = valid([[random.choice(moves), random.choice(directions)] for x in range(nb_mvt)], moves)
    cube = scramble(mvt_choisi, nb_mvt)

    # Format scramble to a string with movecount
    #return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) + "[" + str(nb_mvt) + "]"
    return ''.join(str(mvt_choisi[x][0]) + str(mvt_choisi[x][1]) for x in range(len(mvt_choisi))), cube


def valid(ar, moves):
    # Check if Move behind or 2 behind is the same as the random move
    # this gets rid of 'R R2' or 'R L R2' or similar for all moves
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar
 
    
    
def main():
    '''Creation d un dataset aleatoire comprenant la position du cube avec les mouvements a excecuter pour le resoudre
    moves <list> : tableau regroupant les 6 rotations possibles
    directions <list> : tableau des directions possibles des rotations --> sens horaire, anti_horaire ou demi-tour complet
    nb_mvt <int> : nombre de mouvements d une combinaison
    nb_dataset <int> : nombre de combinaisons presentent dans le dataset.csv
    ens_data <array pandas> : dataset sous forme de array pandas
    mvt_choisi <str> : mouvement d une combinaison 
    rubik_str <str> : definition du rubik cube
 '''
    
    
    
    moves = ["U", "D", "F", "B", "R", "L"]
    directions = ["", "'", "2"]
    nb_mvt = 1
    nb_dataset = 10
    i = 1
    ens_data = pd.DataFrame(dtype='str')
       
    while i <= nb_dataset :
        mvt_choisi, rubik_str = gen_scramble(nb_mvt, moves, directions)
        ens_data = ens_data.append([(rubik_str, mvt_choisi)])
        i+=1
    
    ens_data.to_csv('/menu/app/Projet_Rubik_cube/data/Creation_Data/Data.csv')    
    print("\nData shape : ", ens_data.shape, "\nSaved in Data.csv...\n")
   
       
    
if __name__ == '__main__':
    main()