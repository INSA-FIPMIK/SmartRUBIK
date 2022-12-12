from vpython import *
import time
#from vpython.no_notebook import stop_server
import kociemba
from tkinter import *
import serial
import random
import cv2
import numpy as np

#-------------------------
#Test de connection de l'arduino nano
print("\nTentative de connection a l ARDUINO...\n")
ser = serial.Serial("/dev/ttyUSB0",9600,timeout=10)
print(ser.read().decode("utf-8"))


#------------------------------------------------------------------------------------------------------------------------------------------------
#Jumeau

"""Résolution des mouvements. Les mouvements du Rubik's cube sont découpés en "n" étapes intermédiaires. """
n=10
globals()["cubes"] = []

def Creation_jumeau(a):
    """Couleur du fond de l'écran affiché"""
    scene = canvas(background = color.white)

    

    """x, y et z sont les cordonnées d'un cube du Rubik's cube à créer"""
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                """Création d'une liste pour chaque cube qui disposera des couleurs du cube"""


                """"Create a compound object, containing the cube and each of its corresponding labels"""
                """Création d'un liste vide"""
                object = []

                """The cubes are created at (0, 0, 0) and then moved to their final position"""
                """Création d'un cube"""
                cube = box( pos=vec(0, 0, 0), length=0.9, height=0.9, width=0.9, color=vec(0.2, 0.2, 0.2))
                object.append(cube)

                """positionnement du cube"""
                cube.pos = vec(x,y,z)

                """Ajout des informations du cube dans la liste cubes"""
                globals()["cubes"].append( cube )

    """Numéro des faces"""
    k=0

    #face du haut (blanc)
    y = 1.45
    for z in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if a[k] == 'U':
                #blanc
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.white )
            if a[k] == 'R':
                #bleu
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.blue )
            if a[k] == 'F':
                #rouge
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.red)
            if a[k] == 'D':
                #jaune
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.yellow)
            if a[k] == 'L':
                #vert
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.green)
            if a[k] == 'B':
                #orange
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.orange)

            k = k+1

    #face de droite (bleu)
    x = 1.45
    for y in [1, 0, -1]:
        for z in [1, 0, -1]:
            if a[k] == 'U':
                #blanc
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.white )
            if a[k] == 'R':
                #bleu
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.blue )
            if a[k] == 'F':
                #rouge
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.red)
            if a[k] == 'D':
                #jaune
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.yellow)
            if a[k] == 'L':
                #vert
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.green)
            if a[k] == 'B':
                #orange
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.orange)

            k = k+1

    #face avant (rouge)
    z = 1.45
    for y in [1, 0, -1]:
        for x in [-1, 0, 1]:
            if a[k] == 'U':
                #blanc
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.white )
            if a[k] == 'R':
                #bleu
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.blue )
            if a[k] == 'F':
                #rouge
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.red)
            if a[k] == 'D':
                #jaune
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.yellow)
            if a[k] == 'L':
                #vert
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.green)
            if a[k] == 'B':
                #orange
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.orange)

            k = k+1

    #face dessous (jaune)
    y = -1.45
    for z in [1, 0, -1]:
        for x in [-1, 0, 1]:
            if a[k] == 'U':
                #blanc
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.white )
            if a[k] == 'R':
                #bleu
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.blue )
            if a[k] == 'F':
                #rouge
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.red)
            if a[k] == 'D':
                #jaune
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.yellow)
            if a[k] == 'L':
                #vert
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.green)
            if a[k] == 'B':
                #orange
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.02, width=0.9, color=color.orange)

            k = k+1

    #face gauche (vert)
    x = -1.45
    for y in [1, 0, -1]:
        for z in [-1, 0, 1]:
            if a[k] == 'U':
                #blanc
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.white )
            if a[k] == 'R':
                #bleu
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.blue )
            if a[k] == 'F':
                #rouge
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.red)
            if a[k] == 'D':
                #jaune
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.yellow)
            if a[k] == 'L':
                #vert
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.green)
            if a[k] == 'B':
                #orange
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.02, height=0.9, width=0.9, color=color.orange)

            k = k+1

    #face arrière (orange)
    z = -1.45
    for y in [1, 0, -1]:
        for x in [1, 0, -1]:
            if a[k] == 'U':
                #blanc
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.white )
            if a[k] == 'R':
                #bleu
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.blue )
            if a[k] == 'F':
                #rouge
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.red)
            if a[k] == 'D':
                #jaune
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.yellow)
            if a[k] == 'L':
                #vert
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.green)
            if a[k] == 'B':
                #orange
                globals()["face%d"%k] = box( pos=vec(x, y, z), length=0.9, height=0.9, width=0.02, color=color.orange)

            k = k+1

def L():
    """Mouvement L du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.x < -0.9:
                c.rotate( angle=pi/(2*n), axis=vec(1,0,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.x < -0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(1,0,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)


def l():
    """Mouvement l du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.x < -0.9:
                c.rotate( angle=pi/(2*n), axis=vec(-1,0,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.x < -0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(-1,0,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def U():
    """Mouvement T du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.y > 0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,1,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.y > 0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,1,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def u():
    """Mouvement t du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.y > 0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,-1,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.y > 0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,-1,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def R():
    """Mouvement R du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.x > 0.9:
                c.rotate( angle=pi/(2*n), axis=vec(1,0,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.x > 0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(1,0,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def r():
    """Mouvement r du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.x > 0.9:
                c.rotate( angle=pi/(2*n), axis=vec(-1,0,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.x > 0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(-1,0,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def D():
    """Mouvement D du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.y < -0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,1,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.y < -0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,1,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def d():
    """Mouvement d du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.y < -0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,-1,0), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.y < -0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,-1,0), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def F():
    """Mouvement F du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.z > 0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,0,1), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.z > 0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,0,1), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def f():
    """Mouvement f du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.z > 0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,0,-1), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.z > 0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,0,-1), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def B():
    """Mouvement B du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.z < -0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,0,1), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.z < -0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,0,1), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def b():
    """Mouvement b du Rubik's cube"""
    for k in range (n):
        for c in cubes:
            if c.pos.z < -0.9:
                c.rotate( angle=pi/(2*n), axis=vec(0,0,-1), origin=vec(0,0,0) )
        for f in range (0,54):
            if globals()["face%d"%f].pos.z < -0.9:
                globals()["face%d"%f].rotate( angle=pi/(2*n), axis=vec(0,0,-1), origin=vec(0,0,0) )
        sleep(1*10**-4/n)

def atteindre_position(sequences):
    """Fonction prenant en entrée les différents mouvements du Rubik's cube pour les réaliser. Exemple, jumeau('LLR') effectuera les mouvements L,L puis R"""
    function_mappings = {
            'L': "L()",
            'l': "l()",
            'u': "U()",
            'U': "u()",
            'R': "R()",
            'r': "r()",
            'd': "D()",
            'D': "d()",
            'f': "F()",
            'F': "f()",
            'B': "B()",
            'b': "b()",
    }
    liste_sequences = list(sequences)

    for j in range(0,len(sequences)):
        eval(function_mappings[liste_sequences[j]])

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

def mvmt_position_melange(a):
    sol = kociemba.solve('UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB',a)

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

def resoudre (a):
    atteindre_position(mvmt_solution(a))

def melanger (a):
    atteindre_position(mvmt_position_melange(a))


#------------------------------------------------------------------------------------------------------------------------------------------------
#IHM


def nothing(x):
		pass

def get_disteud(a, b):
	t = np.linalg.norm([abs(a_elt - b_elt) for a_elt, b_elt in zip(a, b)])
	return t

def vect2mat(m):
	b = [m[0:3], m[3:6], m[6:9]]
	return b

def drawface(cube, x, y, p, c):
	cv2.rectangle(cube, (x+p*1, y+p), (x+p*2, y+p*2), couleurs["values"][c[0]], -1)
	cv2.rectangle(cube, (x+p*2, y+p), (x+p*3, y+p*2), couleurs["values"][c[1]], -1)
	cv2.rectangle(cube, (x+p*3, y+p), (x+p*4, y+p*2), couleurs["values"][c[2]], -1)

	cv2.rectangle(cube, (x+p*1, y+p*2), (x+p*2, y+p*3), couleurs["values"][c[3]], -1)
	cv2.rectangle(cube, (x+p*2, y+p*2), (x+p*3, y+p*3), couleurs["values"][c[4]], -1)
	cv2.rectangle(cube, (x+p*3, y+p*2), (x+p*4, y+p*3), couleurs["values"][c[5]], -1)

	cv2.rectangle(cube, (x+p*1, y+p*3), (x+p*2, y+p*4), couleurs["values"][c[6]], -1)
	cv2.rectangle(cube, (x+p*2, y+p*3), (x+p*3, y+p*4), couleurs["values"][c[7]], -1)
	cv2.rectangle(cube, (x+p*3, y+p*3), (x+p*4, y+p*4), couleurs["values"][c[8]], -1)

def miss_face (face) :
	# ~ print("yes")
	if (face[2]=='w') or (face[2] == 'y') :
		g_face=[face[2],face[0],face[1]]
	else :
		if (face[1]=='w') or (face[1] == 'y') :
			g_face=[face[1],face[2],face[0]]
		else :
			if (face[0]=='w') or (face[0] == 'y') :
				g_face=[face[0],face[1],face[2]]
			else :
				if (face[0] != 'w') and (face[0] != 'y') and (face[1] != 'w') and (face[1] != 'y') and (face[2] != 'w') and (face[2] != 'y') :
					i=face.index("?")
					if i==0 :
						g_face=[face[0],face[1],face[2]]
					if i==1:
						g_face=[face[1],face[2],face[0]]
					if i==2:
						g_face=[face[2],face[0],face[1]]

	# Possible combinations :

	c1 = ["w","r","b"]
	c2 = ["w","g","r"]
	c3 = ["w","o","g"]
	c4 = ["w","b","o"]
	c5 = ["y","b","r"]
	c6 = ["y","r","g"]
	c7 = ["y","g","o"]
	c8 = ["y","o","b"]

	c=[c1,c2,c3,c4,c5,c6,c7,c8]

	stop=0
	i=g_face.index("?")
	j=0

	while(stop==0):
		suppr_face=[]
		for k in range (0,3):
			suppr_face.append(g_face[k])
		del suppr_face[i]


		cp=[]
		ci=c[j]
		for k in range (0,3):
			cp.append(ci[k])
		del cp[i]


		if (suppr_face == cp):
			stop=1
			if g_face[0] == '?' :
				g_face[0]=ci[0]
			if g_face[1] == '?' :
				g_face[1]=ci[1]
			if g_face[2] == '?' :
				g_face[2]=ci[2]
		j=j+1
		if j== 8 and stop==0:
			if g_face[0] == '?' :
				g_face[0]="H"
			if g_face[1] == '?' :
				g_face[1]="H"
			if g_face[2] == '?' :
				g_face[2]="H"
			print("oupss")
			break

	return(g_face[i])

evt = -1
c1 = 400
c2 = 130
coords2 = [
(c1-95, c2+27),(c1-139, c2+13),(c1-175, c2+6),(c1-42, c2+9),(c1-88, c2+4),(c1-129, c2-8),(c1, c2),(c1-46, c2-10),(c1-63, c2-17),
(c1-106, c2+195),(c1-150, c2+167),(c1-176, c2+248),(c1-111, c2+136),(c1-150, c2+112),(c1-197, c2+90),(c1-117, c2+75),(c1-162, c2+59),(c1-196, c2+46),
(c1+3, c2+162),(c1-19, c2+169),(c1-59, c2+190),(c1+18, c2+87),(c1-21, c2+117),(c1-61, c2+134),(c1+21, c2+41),(c1-17, c2+58),(c1-56, c2+68)
]
c1 = 412
c2 = 120
coords = [
(c1, c2),(c1-42, c2+14),(c1-88, c2+29),(c1-46, c2-8),(c1-88, c2+4),(c1-139, c2+13),(c1-63, c2-17),(c1-129, c2-8),(c1-174, c2),
(c1-196, c2+46),(c1-162, c2+59),(c1-115, c2+77),(c1-197, c2+90),(c1-150, c2+112),(c1-111, c2+136),(c1-176, c2+248),(c1-150, c2+167),(c1-106, c2+195),
(c1-64, c2+76),(c1-17, c2+58),(c1+25, c2+41),(c1-61, c2+134),(c1-21, c2+117),(c1+22, c2+87),(c1-59, c2+190),(c1-19, c2+169),(c1+3, c2+162)
]
colors = []

h = []
s = []
v = []

# ~ def click(event, x, y, flags, params):
	# ~ global point
	# ~ global evt
	# ~ global indice
	# ~ if event == cv2.EVENT_LBUTTONDOWN:
		# ~ point = (x, y)
		# ~ coords.append(point)
		# ~ print(point)
		# ~ h.append(hsv[y, x, 0])
		# ~ s.append(hsv[y, x, 1])
		# ~ v.append(hsv[y, x, 2])

		# ~ print("H: " + str(sum(h)/len(h)))
		# ~ print("S: " + str(sum(s)/len(s)))
		# ~ print("V: " + str(sum(v)/len(v)))
		# ~ print("--------")
		# ~ evt = event

# ~ cv2.namedWindow("frame")
# ~ cv2.namedWindow("frame2")
# ~ cv2.setMouseCallback("frame", click)

couleurs = {
	"center" : {
		"R": [152, 203, 108],
		"G": [87, 224, 176],
		"W": [113, 94, 162],
		"B": [117, 218, 178],
		"O": [110, 201, 53],  #noir"O": [115, 235, 45], ------- [82, 212, 51]
		"Y": [25, 166, 185]
		# ~ "center" : {
		# ~ "R": [152, 203, 108],
		# ~ "G": [87, 224, 176],
		# ~ "W": [113, 94, 162],
		# ~ "B": [117, 218, 178],
		# ~ "O": [82, 212, 51],  #noir"O": [115, 235, 45],
		# ~ "Y": [25, 166, 185]
	},
	"values" : {
		"R": [0, 0, 255],
		"G": [0, 255, 0],
		"W": [255, 255, 255],
		"B": [255, 0, 0],
		"O": [0, 100, 255],
		"Y": [0, 255, 255]
	},
	"lower" : {
		"R": [138, 141, 83],
		"G": [76, 194, 98],
		"W": [85, 40, 70],
		"B": [102, 182, 102],
		"O": [1, 83, 182],
		"Y": [11, 78, 116]
		},
	"upper" : {
		"R": [179, 255, 255],
		"G": [98, 255, 255],
		"W": [141, 149, 255],
		"B": [133, 255, 255],
		"O": [27, 255, 255],
		"Y": [72, 255, 255]
		}
}

def gstreamer_pipeline(
	capture_width=3264,
	capture_height=2464,
	display_width=640,
	display_height=480,
	framerate=21,
	flip_method=2,
	sensor_id=0,
):
	return (
		"nvarguscamerasrc sensor_id=%d wbmode=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 ! "
		"video/x-raw(memory:NVMM), "
		"width=(int)%d, height=(int)%d, "
		"format=(string)NV12, framerate=(fraction)%d/1 ! "
		"nvvidconv flip-method=%d ! "
		"video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
		"videoconvert ! "
		"video/x-raw, format=(string)BGR ! videobalance contrast=1.8 brightness=-0.1 saturation=1.5 ! appsink"
		% (
			sensor_id,
			capture_width,
			capture_height,
			framerate,
			flip_method,
			display_width,
			display_height,
		)
	)

cam1 = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0, sensor_id = 0), cv2.CAP_GSTREAMER)
cam2 = cv2.VideoCapture(gstreamer_pipeline(flip_method = 0, sensor_id = 1), cv2.CAP_GSTREAMER)

c = []

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
	button_solve.config(state="disable")


	"""Pilotage du jumeau en même temps"""
	str_mvt=''.join(mvt_random)
	atteindre_position(str_mvt)

	return

# Color detection fonction
def b_vision():

	for tps in range(10):
		_, frame = cam1.read()
		_, frame2 = cam2.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #image en format HSV
	hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)  #image en format HSV

	colors = []
	colors2 = []

	for k, coord in enumerate(coords):
		# ~ cv2.circle(frame, coord, 1, (0,0,255),2)
		blue = 0
		green = 0
		red = 0
		# ~ cv2.rectangle(frame,(coord[0]-5,coord[1]-5),(coord[0]+5,coord[1]+5),(0,0,255),1)
		for i in range(-5,5):
			for j in range(-5,5):
				blue += hsv[coord[1]+i, coord[0]+j, 0]
				green += hsv[coord[1]+i, coord[0]+j, 1]
				red += hsv[coord[1]+i, coord[0]+j, 2]
		blue /= 100
		green /= 100
		red /= 100
		colors.append([blue, green, red])

	for k, coord in enumerate(coords2):
		# ~ cv2.circle(frame2, coord, 1, (0,0,255),2)
		blue = 0
		green = 0
		red = 0
		# ~ cv2.rectangle(frame2,(coord[0]-5,coord[1]-5),(coord[0]+5,coord[1]+5),(0,0,255),1)
		for i in range(-5,5):
			for j in range(-5,5):
				blue += hsv2[coord[1]+i, coord[0]+j, 0]
				green += hsv2[coord[1]+i, coord[0]+j, 1]
				red += hsv2[coord[1]+i, coord[0]+j, 2]
		blue /= 100
		green /= 100
		red /= 100
		colors2.append([blue, green, red])

	c = colors + colors2

	# ~ cv2.circle(frame, (frame.shape[1]/2,frame.shape[0]/2), 2, (0,255,0), 3)
	# ~ cv2.circle(frame2, (frame2.shape[1]/2,frame2.shape[0]/2), 2, (0,255,0), 3)

	#affichage de l'image
	# ~ cv2.imshow("frame", frame)
	# ~ cv2.moveWindow("frame", 0, 0)
	# ~ cv2.imshow("frame2", frame2)
	# ~ cv2.moveWindow("frame2", 700, 0)

	#cam2
	sortie_d = []   #variables stockant la matrice de sortie
	sortie_l = []
	sortie_f = []
	#cam1
	sortie_u = []
	sortie_r = []
	sortie_b = []
	sortie = []

	if len(c) > 53 :
		for ind in range(len(c)):
			dist = 1000  #initialisation des parametres permettant d'assigner une des 6 couleurs
			temp = 0
			f = "W"

			temp = get_disteud(c[ind], couleurs["center"]["R"]) #calcul distance euclidienne
			if temp < dist:
				f = "R"
				dist = temp
			temp = get_disteud(c[ind], couleurs["center"]["G"])
			if temp < dist:
				f = "G"
				dist = temp
			temp = get_disteud(c[ind], couleurs["center"]["B"])
			if temp < dist:
				f = "B"
				dist = temp
			temp = get_disteud(c[ind], couleurs["center"]["O"])
			if temp < dist:
				f = "O"
				dist = temp
			temp = get_disteud(c[ind], couleurs["center"]["Y"])
			if temp < dist:
				f = "Y"
				dist = temp
			temp = get_disteud(c[ind], couleurs["center"]["W"])
			if temp < dist:
				f = "W"
				dist = temp
			c[ind] = couleurs["values"][f] #assignation valeur couleurs

			if ind < 9:
				sortie_u.append(f)
			if ind > 8 and ind < 18:
				sortie_r.append(f)
			if ind > 17 and ind < 27:
				sortie_b.append(f)
			if ind > 26 and ind < 36:
				sortie_d.append(f)
			if ind > 35 and ind < 45:
				sortie_f.append(f)
			if ind > 44 and ind < 54:
				sortie_l.append(f)

		sortie_d[4] = "Y"
		sortie_l[4] = "G"
		sortie_f[4] = "R"
		sortie_u[4] = "W"
		sortie_r[4] = "B"
		sortie_b[4] = "O"

		sortie = str(sortie_u) + str(sortie_r) + str(sortie_f) + str(sortie_d) + str(sortie_l) + str(sortie_b)

		sortie = str(sortie)
		sortie=sortie.replace("[","")
		sortie=sortie.replace("]","")
		sortie=sortie.replace(",","")
		sortie=sortie.replace("'","")
		sortie=sortie.replace(" ","")
		sortie = sortie.lower()

		sortiee=sortie[0:6]+"X"+sortie[7:15]+"X"+sortie[16:20]+"X"+sortie[21:35]+"X"+"X"+sortie[37:53]+"X"

		face6=miss_face(["?",sortie[38],sortie[18]])
		face15=miss_face([sortie[29],"?",sortie[26]])
		face20=miss_face([sortie[8],"?",sortie[9]])
		face35=miss_face(["?",sortie[51],sortie[17]])
		face36=miss_face([sortie[0],sortie[47],"?"])
		face53=miss_face([sortie[33],sortie[42],"?"])

		sortie=sortie[0:6]+face6+sortie[7:15]+face15+sortie[16:20]+face20+sortie[21:35]+face35+face36+sortie[37:53]+face53

		print(sortie)
		print("rouge", sortie.count("r"))
		print("bleu", sortie.count("b"))
		print("orange", sortie.count("o"))
		print("jaune", sortie.count("y"))
		print("vert", sortie.count("g"))
		print("blanc", sortie.count("w"))

		if sortie.count("r")==9 and sortie.count("b") == 9 and sortie.count("o")==9 and  sortie.count("y") ==9 and sortie.count("g")==9 and sortie.count("w") ==9 :
			button_solve.config(state="normal")
		else :
			button_solve.config(state="disable")
		# ~ print("rouge", sortie.count("r"))
		# ~ print("bleu", sortie.count("b"))
		# ~ print("orange", sortie.count("o"))
		# ~ print("jaune", sortie.count("y"))
		# ~ print("vert", sortie.count("g"))
		# ~ print("blanc", sortie.count("w"))

		#dessin des faces pour une meilleure visualisation
		# ~ cube1 = cv2.bitwise_and(frame, 0)  #creation image visualisation du cube
		# ~ cube2 = cv2.bitwise_and(frame2, 0)
		# ~ drawface(cube1, 75, 10, 50, sortie_u)
		# ~ drawface(cube1, 2, 170, 50, sortie_r)
		# ~ drawface(cube1, 157, 170, 50, sortie_b)
		# ~ drawface(cube2, 75, 10, 50, sortie_d)
		# ~ drawface(cube2, 2, 170, 50, sortie_f)
		# ~ drawface(cube2, 157, 170, 50, sortie_l)
		# ~ cv2.imshow("cube", cube1)
		# ~ cv2.moveWindow("cube", 0, 500)
		# ~ cv2.imshow("cube2", cube2)
		# ~ cv2.moveWindow("cube2", 700, 500)

	# ~ if cv2.waitKey(1) == ord('q'):
		# ~ cv2.destroyAllWindows()

	##########################

	# Enable the solve button
	label_col.config(text='Colors : ' + sortie)



	"""Début Partie Rajouté """
	cube = label_col['text']
	cube = cube.replace('Colors : ',"")
	cube=cube.replace('w','U')
	cube=cube.replace('b','R')
	cube=cube.replace('r','F')
	cube=cube.replace('y','D')
	cube=cube.replace('g','L')
	cube=cube.replace('o','B')

	print(cube)
	Creation_jumeau(cube)

	#sol=kociemba.solve(cube)
	#print("La solution est:")
	#print(sol)
	"""Fin Partie rajouté"""



	return


# Solve fonction : use of kociemba library
def b_solve():
	cube = label_col['text']
	cube = cube.replace('Colors : ',"")
	cube=cube.replace('w','U')
	cube=cube.replace('b','R')
	cube=cube.replace('r','F')
	cube=cube.replace('y','D')
	cube=cube.replace('g','L')
	cube=cube.replace('o','B')

	sol=kociemba.solve(cube)
	print("La solution est:")
	print(sol)

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
	sol=sol.replace("F","f")
	sol=sol.replace("H","F")

	sol=sol.replace("B'","b")

	sol=sol.replace(" ","")
	sol = '&'+sol+'#'

	print(sol)
	label_sol.config(text='Solution : ' + sol)

	# Serial communication
	ser.write(sol.encode('ascii'))

	# Disable the solve button
	button_solve.config(state="disable")
	return

# Control motor fonction : Send a letter of movement the arduino
def b_motor(mov):
	# Serial communication
	ser.write(mov.encode('ascii'))

	"""Effectuer les mouvements sur le jumeau"""
	atteindre_position(mov)


	# Disable the solve button
	button_solve.config(state="disable")
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

# Window creation and configuration
screen = Tk()
screen.title("IHM")
screen.geometry("800x800")
font_perso = ('Times New Roman', 15)

# Images import
image_scramble = PhotoImage(file='Images/scramble.png')
image_solve = PhotoImage(file='Images/solve.png')
image_vision = PhotoImage(file='Images/vision.png')
image_right = PhotoImage(file='Images/right.png')
image_left = PhotoImage(file='Images/left.png')
image_moves = PhotoImage(file='Images/moves.png')


# Widgets text
titre = Label(screen, text = "RUBIK'S CUBE SOLVER", font=('Times New Roman', 25,'bold'))
titre.pack(side = TOP)

credit = Label(screen, text = "Cédric GUILLOT - Anthony PAUL - 2021/2022", font=('Times New Roman', 11))
credit.pack(side = BOTTOM)


# Widgets Button
button_scramble = Button(screen, text = 'SCRAMBLE',font=font_perso,bg='#cecece',activebackground='#cecece', width=180, height=180, image=image_scramble, compound=BOTTOM, command=b_scramble)
button_scramble.place(x=100, y=80)

button_vision = Button(screen, text = 'VISION',font=font_perso,bg='#cecece',activebackground='#cecece', width=180, height=180, image=image_vision, compound=BOTTOM, command=b_vision)
button_vision.place(x=300, y=80)

button_solve = Button(screen, text = 'SOLVE',font=font_perso,bg='#cecece',activebackground='#cecece', width=180, height=180, image=image_solve, compound=BOTTOM, command=b_solve)
button_solve.place(x=500, y=80)

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


