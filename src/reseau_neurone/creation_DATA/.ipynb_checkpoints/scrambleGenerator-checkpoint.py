import random
import sys
from scrambleImage import scramble
import os
import csv
import numpy as np
import pandas as pd
import kociemba


'''Ce Programme genere aleatoirement des combinaisons de cube et sa resolution'''


def gen_scramble(nb_mvt, moves, directions):
    # Make array of arrays that represent moves ex. U' = ['U', "'"]
    mvt_choisi = valid([[random.choice(moves), random.choice(directions)] for x in range(nb_mvt)], moves)
    cube = scramble(mvt_choisi, nb_mvt)
    print(mvt_choisi)
    # Format scramble to a string with movecount
    return mvt_choisi, cube



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




def resol_kociemba (rubik_str_color):
    '''Resolution de la chaine de caractere via Kociemba
    rubik_str_color <str> : chaine de definition du rubik cube melange'''
    
    #----------Remplacement des couleurs en commandes Kociemba--------------
    # On suppose que le rubik's cube soit posé avec la face blanche en haut, la face rouge a droite

    rubik_str_color = rubik_str_color.replace('w','U')
    rubik_str_color = rubik_str_color.replace('r','R')
    rubik_str_color = rubik_str_color.replace('g','F')
    rubik_str_color = rubik_str_color.replace('y','D')
    rubik_str_color = rubik_str_color.replace('o','L')
    rubik_str_color = rubik_str_color.replace('b','B')
    
    mvt_choisi = kociemba.solve(rubik_str_color)
    mvt_choisi = mvt_choisi.replace(' ', '')
    return mvt_choisi


def resol_inverse (rubik_str):
    '''Resolution de la chaine de caractere par l inverse des mouvements
    rubik_str_color <str> : chaine de definition du rubik cube melange'''

    #retournement des mouvements
    string = ""
    for i in rubik_str:
        string = string + i
    
    
    string = string.replace('L','L')
    string = string.replace('r','R')
    string = string.replace('g','F')
    string = string.replace('y','D')
    string = string.replace('o','L')
    string = string.replace('b','B')
    


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
    directions = ["", "1", "2"]
    nb_mvt = 10
    nb_dataset = 1
    i = 1
    ens_data = pd.DataFrame(dtype='str')
   
    while i <= nb_dataset :
        mvt_choisi, rubik_str = gen_scramble(nb_mvt, moves, directions)
        mvt_choisi = resol_kociemba(rubik_str)
        ens_data = ens_data.append([(rubik_str, mvt_choisi)])
        i+=1
    
    ens_data.to_csv('/menu/app/Documents/SmartRUBIK/data/Creation_Data/Data_test.csv')    
    print("\nData shape : ", ens_data.shape, "\nSaved in Data.csv...\n")
   
       
    
if __name__ == '__main__':
    main()