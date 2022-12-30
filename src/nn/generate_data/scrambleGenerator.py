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
    '''Generation des mouvements de manière aléatoire suivants les arrays mouvements et directions'''
    # Make array of arrays that represent moves ex. U' = ['U', "'"]
    mvt_choisi = valid([[random.choice(moves), random.choice(directions)] for x in range(nb_mvt)], moves)
    cube = scramble(mvt_choisi, nb_mvt)
    return mvt_choisi, cube



def valid(ar, moves):
    '''Suppression des redondance tels que  : R R2 à la suite '''
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar




def resol_kociemba (rubik_str):
    '''Resolution de la chaine de caractere via Kociemba
    rubik_str_color <str> : chaine de definition du rubik cube melange'''
    
    #----------Remplacement des couleurs en commandes Kociemba--------------
    # On suppose que le rubik's cube soit posé avec la face blanche en haut, la face rouge a droite

    rubik_str = rubik_str.replace('w','U')
    rubik_str = rubik_str.replace('r','R')
    rubik_str = rubik_str.replace('g','F')
    rubik_str = rubik_str.replace('y','D')
    rubik_str = rubik_str.replace('o','L')
    rubik_str = rubik_str.replace('b','B')
    
    mvt_choisi = kociemba.solve(rubik_str)
    
    mvt_choisi = mvt_choisi.replace(" U'","U1")
    mvt_choisi = mvt_choisi.replace(" D'","D1")
    mvt_choisi = mvt_choisi.replace(" F'","F1")
    mvt_choisi = mvt_choisi.replace(" B'","B1")
    mvt_choisi = mvt_choisi.replace(" R'","R1")
    mvt_choisi = mvt_choisi.replace(" L'","L1")
    
    mvt_choisi = mvt_choisi.replace(" U ","U0")
    mvt_choisi = mvt_choisi.replace(" D ","D0")
    mvt_choisi = mvt_choisi.replace(" F ","F0")
    mvt_choisi = mvt_choisi.replace(" B ","B0")
    mvt_choisi = mvt_choisi.replace(" R ","R0")
    mvt_choisi = mvt_choisi.replace(" L ","L0")
    
    
    print("\nresolution via Kociemba : ", mvt_choisi)
    return mvt_choisi


def resol_inverse (mvt_choisi, nb_mvt):
    '''Resolution de la chaine de caractere par l inverse des mouvements
    rubik_str_color <str> : chaine de definition du rubik cube melange'''
       
    #retournement des mouvements 
    mvt_choisi = np.array(mvt_choisi)
    mvt_choisi = np.flip(mvt_choisi)
    mvt_choisi = ''.join(str(mvt_choisi[x][0]) + str(mvt_choisi[x][1]) + ' ' for x in range(len(mvt_choisi)))

    mvt_choisi = mvt_choisi.replace('1U','U0')
    mvt_choisi = mvt_choisi.replace('1D','D0')
    mvt_choisi = mvt_choisi.replace('1F','F0')
    mvt_choisi = mvt_choisi.replace('1B','B0')
    mvt_choisi = mvt_choisi.replace('1R','R0')
    mvt_choisi = mvt_choisi.replace('1L','L0')
    
    mvt_choisi = mvt_choisi.replace('0U','U1')
    mvt_choisi = mvt_choisi.replace('0D','D1')
    mvt_choisi = mvt_choisi.replace('0F','F1')
    mvt_choisi = mvt_choisi.replace('0B','B1')
    mvt_choisi = mvt_choisi.replace('0R','R1')
    mvt_choisi = mvt_choisi.replace('0L','L1')
    
    mvt_choisi = mvt_choisi.replace('2U','U2')
    mvt_choisi = mvt_choisi.replace('2D','D2')
    mvt_choisi = mvt_choisi.replace('2F','F2')
    mvt_choisi = mvt_choisi.replace('2B','B2')
    mvt_choisi = mvt_choisi.replace('2R','R2')
    mvt_choisi = mvt_choisi.replace('2L','L2')
    
    #print("\nresolution via inverse : ", mvt_choisi)
    return mvt_choisi
    


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
    directions = ["0", "1", "2"]
    nb_mvt = int(input("Nombre de mvt :"))
    nb_dataset = int(input("Taille du Dataset :"))
    i = 1
    ens_data = pd.DataFrame(columns=['mvt','rbk_str'], dtype='str')
    choix = 0

    while i <= nb_dataset :
        mvt_choisi, rubik_str = gen_scramble(nb_mvt, moves, directions) #creation d'un mélange avec ça combinaison et les mouvements effectue
        if choix == 0:
            mvt_choisi = resol_inverse(mvt_choisi, nb_mvt) #retournement des mouvements
        else :
            mvt_choisi = resol_kociemba(rubik_str) #resolution du melange via Kociemba
        
        ens_data.loc[i] = mvt_choisi, rubik_str
        i+=1
    
    #Sauvegarde du fichier
    ens_data.to_csv('../../../data/Creation_Data/Data.csv')    
    print("\nData shape : ", ens_data.shape, "\nSaved in Data.csv...\n")
   
       
    
if __name__ == '__main__':
    main()