from vpython import *
import time
from tkinter import *
import serial
import random
import cv2
import numpy as np
import pandas as pd 

from solve.solve_kociemba import solve_kociemba
from camera.placement_points import Supervision
import nn.main as main_nn


#-------------------------
#Test de connection de l'arduino nano
print("\nTentative de connection a l ARDUINO...\n")
ser = serial.Serial("/dev/ttyUSB0",9600,timeout=10)
print(ser.read().decode("utf-8"))
print("\nConnexion reussie....\n")
#-------------------------


def mvmt_solution(a):

    sol = kociemba.solve(a)
    sol=sol.replace("R2","RR")
    sol=sol.replace("L2","LL")
    sol=sol.replace("D2","DD")
    sol=sol.replace("B2","BB")
    sol=sol.replace("F2","FF")
    sol=sol.replace("U2","UU")

    sol=sol.replace("R'","H")
    sol=sol.replace("R","r")
    sol=sol.replace("H","R")

    sol=sol.replace("L'","l")

    sol=sol.replace("U'","u")

    sol=sol.replace("D'","H")
    sol=sol.replace("D","d")
    sol=sol.replace("H","D")

    sol=sol.replace("F'","H")
    sol=sol.replace("F","F")
    sol=sol.replace("H","f")

    sol=sol.replace("B'","b")

    sol=sol.replace(" ","")

    return sol


# Scramble fonction : Generated a list of random movements to send to the arduino
def b_scramble():
	list_mvt = ["r","R","l","L","u","U","b","B","f","F","d","D"]
	nb = random.randint(40,50)	# List size
	s='a'
	mvt_random=[]
	for i in range (0,nb,1):
		r=random.choice(list_mvt)

		# Prevent two opposite mouvements in a row
		if r == s.upper() or r==s.lower():
			r=s

		mvt_random.append(r)
		s=r

	mvt_random=str(mvt_random)
	mvt_random=mvt_random.replace("[","")
	mvt_random=mvt_random.replace("]","")
	mvt_random=mvt_random.replace(",","")
	mvt_random=mvt_random.replace("'","")
	mvt_random=mvt_random.replace(" ","")
	print_mvt.config(text='Moves : ' + mvt_random)

	# Sent to arduino with serail communication
	ser.write(mvt_random.encode('ascii'))

	# Disable the solve button
	#button_solve.config(state="disable")


	"""Pilotage du jumeau en même temps"""
	str_mvt=''.join(mvt_random)
	return



# Color detection fonction
def b_vision():
        
    sortie = Supervision()
    print(sortie)
    print("rouge", sortie.count("r"))
    print("bleu", sortie.count("b"))
    print("orange", sortie.count("o"))
    print("jaune", sortie.count("y"))
    print("vert", sortie.count("g"))
    print("blanc", sortie.count("w"))

    '''    if sortie.count("r")==9 and sortie.count("b") == 9 and sortie.count("o")==9 and  sortie.count("y") ==9 and sortie.count("g")==9 and sortie.count("w") ==9 :
        button_solve_nn.config(state="normal")
        button_solve_kociemba.config(state="normal")
    else :
        button_solve_kociemba.config(state="disable")
        button_solve_nn.config(state="disable")

    '''

# Solve fonction : use of kociemba library
def b_solve():
	solve_kociemba()


# Solve fonction with a neuronal network
def c_solve():
    list_mvt = ["r","R","l","L","u","U","b","B","f","F","d","D"]
    cube_resolu = pd.DataFrame(data ={'wwwwwwwwwrrrrrrrrrgggggggggyyyyyyyyyooooooooobbbbbbbbb'})
    rbk_str = pd.read_csv('../data/generated_data/prediction.csv')
    trop_long = 0
  
    while not rbk_str.equals(cube_resolu) or trop_long < 20 :
        #Supervision()
        prediction = main_nn
        prediction = str(prediction)
        prediction = prediction.replace("[","")
        prediction = prediction.replace("]","")
        prediction = prediction.replace(",","")
        
        ser.write(prediction.encode('ascii'))
        
        rbk_str = pd.read_csv('../data/generated_data/prediction.csv')
        trop_long +=1
    # Disable the solve button
    button_solve.config(state="disable")     
        
        
        
        
# Control motor fonction : Send a letter of movement the arduino
def b_motor(mov):
    # Serial communication
    ser.write(mov.encode('ascii'))

    # Disable the solve button
    button_solve_kociemba.config(state="disable")
    button_solve_nn.config(state="disable")
    return



# Pop up fonction
def help_popup() :

	# Pop up creation
	popup = Toplevel()
	popup.title('Help')
	popup.geometry("400x400") # pop up size
	# Canvas creation for display image
	Canv = Canvas(popup)
	Canv.config(height=image_moves.height(),width=image_moves.width())
	Canv.create_image(0,0, anchor=NW, image = image_moves)
	Canv.pack()
	# Exit button
	Button(popup, text='Exit',font=font_perso,command=popup.destroy).pack(side=BOTTOM)
	return





###########################################################################
###################----------------------------------######################
###################-------IHM Configuration----------######################
###################----------------------------------######################
###########################################################################


# Window creation and configuration
screen = Tk()
screen.title("IHM")
screen.geometry("800x800")
font_perso = ('Times New Roman', 15)

# Images import
image_scramble = PhotoImage(file='../data/images/scramble.png')
image_solve = PhotoImage(file='../data/images/solve.png')
image_vision = PhotoImage(file='../data/images/vision.png')
image_right = PhotoImage(file='../data/images/right.png')
image_left = PhotoImage(file='../data/images/left.png')
image_moves = PhotoImage(file='../data/images/moves.png')


# Widgets text
titre = Label(screen, text = "SMART RUBIK", font=('Times New Roman', 25,'bold'))
titre.pack(side = TOP)

credit = Label(screen, text = "Honoré Bonnet - Boubou Gaye Soumare - Anatole Surel - 2022/2023", font=('Times New Roman', 11))
credit.pack(side = BOTTOM)


# Widgets Button
button_scramble = Button(screen, text = 'SCRAMBLE',font=font_perso,bg='#cecece',activebackground='#cecece', width=180, height=180, image=image_scramble, compound=BOTTOM, command=b_scramble)
button_scramble.place(x=25, y=80)

button_vision = Button(screen, text = 'VISION',font=font_perso,bg='#cecece',activebackground='#cecece', width=180, height=180, image=image_vision, compound=BOTTOM, command=b_vision)
button_vision.place(x=230, y=80)

button_solve_nn = Button(screen, text = 'SOLVE WITH NEURONAL NETWORK',font=font_perso,bg='#cecece',activebackground='#cecece', width=200, height=90, image=image_solve, compound=BOTTOM, command=c_solve)
button_solve_nn.place(x=430, y=80)

button_solve_kociemba = Button(screen, text = 'SOLVE WITH KOCIEMBA',font=font_perso,bg='#cecece',activebackground='#cecece', width=200, height=90, image=image_solve, compound=BOTTOM, command=b_solve)
button_solve_kociemba.place(x=430, y=170)

# Display of movement list (of scramble)
print_mvt = Label(screen, text='Moves : ', font=('Times New Roman', 11, 'bold'))
print_mvt.place(x=80 , y= 300)

# Widgets motor control (right/blue)

label_moteur1 = Label(screen, text = 'Right Face',font=font_perso)
label_moteur1.place(x=100, y=350)

button_moteur1l = Button(screen,font=font_perso,image=image_left, bg='#8ca4f2',activebackground='#4374b2', command=lambda: b_motor("R"))
button_moteur1l.place(x=50, y=400)

button_moteur1r = Button(screen,font=font_perso, image=image_right, bg='#8ca4f2',activebackground='#4374b2',command=lambda: b_motor("r"))
button_moteur1r.place(x=150, y=400)

# Widgets motor control (left/green)

label_moteur2 = Label(screen, text = 'Left Face',font=font_perso)
label_moteur2.place(x=350, y=350)

button_moteur2l = Button(screen,font=font_perso,image=image_left,bg='#84ea63', activebackground='#43b260',command=lambda: b_motor("L"))
button_moteur2l.place(x=300, y=400)

button_moteur2r = Button(screen,font=font_perso, image=image_right,bg='#84ea63',activebackground='#43b260',command=lambda: b_motor("l"))
button_moteur2r.place(x=400, y=400)

# Widgets motor control (front/red)

label_moteur3 = Label(screen, text = 'Front Face',font=font_perso)
label_moteur3.place(x=600, y=350)

button_moteur3l = Button(screen,font=font_perso,image=image_left, bg='#f84f4d',activebackground='#b01e10',command=lambda: b_motor("F"))
button_moteur3l.place(x=550, y=400)

button_moteur3r = Button(screen,font=font_perso, image=image_right,bg='#f84f4d',activebackground='#b01e10',command=lambda: b_motor("f"))
button_moteur3r.place(x=650, y=400)

# Widgets motor control (up/white)

label_moteur4 = Label(screen, text = 'Upper Face',font=font_perso)
label_moteur4.place(x=100, y=550)

button_moteur4l = Button(screen,font=font_perso,image=image_left, bg='#ffffff',activebackground='#d8d6d6',command=lambda: b_motor("U"))
button_moteur4l.place(x=50, y=600)

button_moteur4r = Button(screen,font=font_perso, image=image_right,bg='#ffffff',activebackground='#d8d6d6',command=lambda: b_motor("u"))
button_moteur4r.place(x=150, y=600)

# Widgets motor control (down/yellow)

label_moteur5 = Label(screen, text = 'Down Face',font=font_perso)
label_moteur5.place(x=350, y=550)

button_moteur5l = Button(screen,font=font_perso,image=image_left, bg='#f7eb57',activebackground='#b1b521',command=lambda: b_motor("D"))
button_moteur5l.place(x=300, y=600)

button_moteur5r = Button(screen,font=font_perso, image=image_right,bg='#f7eb57',activebackground='#b1b521',command=lambda: b_motor("d"))
button_moteur5r.place(x=400, y=600)

# Widgets motor control (back/orange)

label_moteur6 = Label(screen, text = 'Back Face',font=font_perso)
label_moteur6.place(x=600, y=550)

button_moteur6l = Button(screen,font=font_perso,image=image_left, bg='#f7b357',activebackground='#b6660c',command=lambda: b_motor("B"))
button_moteur6l.place(x=550, y=600)

button_moteur6r = Button(screen,font=font_perso, image=image_right,bg='#f7b357',activebackground='#b6660c',command=lambda: b_motor("b"))
button_moteur6r.place(x=650, y=600)

# Widget help button

button_help = Button(screen, font = ('Times New Roman', 20, 'bold'),text='?', command = help_popup)
button_help.place(x=740,y=10)

label_col = Label(screen, text = 'Colors : ',font=('Times New Roman', 10, 'bold'))
label_col.place(x=80, y=725)

label_sol = Label(screen, text = 'Solution : ',font=('Times New Roman', 10, 'bold'))
label_sol.place(x=80, y=750)

screen.mainloop()


