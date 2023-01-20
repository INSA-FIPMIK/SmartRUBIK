import cv2
import numpy as np
import csv
import pandas as pd
import os 

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
    print("yes")
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
        print("yo")
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
        if j== 8 : 
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
def click(event, x, y, flags, params):
    global point
    global evt
    global indice
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        coords.append(point)
        print(point)
        evt = event
c1 = 395
c2 = 137
coords2 = [    
(c1-95, c2+27),(c1-139, c2+13),(c1-170, c2+6),(c1-42, c2+9),(c1-88, c2+4),(c1-129, c2-8),(c1, c2),(c1-46, c2-10),(c1-63, c2-17),
(c1-106, c2+195),(c1-150, c2+167),(c1-183, c2+164),(c1-111, c2+136),(c1-150, c2+112),(c1-197, c2+90),(c1-117, c2+75),(c1-162, c2+59),(c1-196, c2+46),
(c1+3, c2+162),(c1-19, c2+169),(c1-59, c2+190),(c1+18, c2+87),(c1-21, c2+117),(c1-61, c2+134),(c1+21, c2+41),(c1-17, c2+58),(c1-56, c2+68)
]
c1 = 380
c2 = 145
coords = [    
(c1, c2),(c1-42, c2+14),(c1-88, c2+29),(c1-46, c2-8),(c1-88, c2+4),(c1-139, c2+13),(c1-63, c2-17),(c1-129, c2-8),(c1-174, c2),
(c1-196, c2+46),(c1-162, c2+59),(c1-115, c2+77),(c1-197, c2+90),(c1-150, c2+112),(c1-111, c2+136),(c1-183, c2+164),(c1-150, c2+167),(c1-106, c2+195),
(c1-64, c2+76),(c1-17, c2+58),(c1+25, c2+41),(c1-61, c2+134),(c1-21, c2+117),(c1+22, c2+87),(c1-59, c2+190),(c1-19, c2+169),(c1+3, c2+162)
]
colors = []

h = []
s = []
v = []



cv2.namedWindow("frame")
cv2.namedWindow("frame2")
cv2.setMouseCallback("frame", click)

couleurs = {
    "center" : {
        "R": [152, 203, 108],
        "G": [87, 224, 176],
        "W": [113, 94, 162],
        "B": [117, 218, 178],
        "O": [110, 201, 53],  #noir"O": [115, 235, 45], ------- [82, 212, 51]
        "Y": [25, 166, 185]
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
    framerate=30 #21,
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

while 1:
    _, frame = cam1.read()
    _, frame2 = cam2.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #image en format HSV
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)  #image en format HSV
    colors = []
    colors2 = []
    
    for k, coord in enumerate(coords):
        cv2.circle(frame, coord, 1, (0,0,255),2)
        blue = 0
        green = 0
        red = 0
        cv2.rectangle(frame,(coord[0]-5,coord[1]-5),(coord[0]+5,coord[1]+5),(0,0,255),1)
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
        cv2.circle(frame2, coord, 1, (0,0,255),2)
        blue = 0
        green = 0
        red = 0
        cv2.rectangle(frame2,(coord[0]-5,coord[1]-5),(coord[0]+5,coord[1]+5),(0,0,255),1)
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
    
    #cv2.circle(frame, (frame.shape[1]/2,frame.shape[0]/2), 2, (0,255,0), 3)
    #cv2.circle(frame2, (frame2.shape[1]/2,frame2.shape[0]/2), 2, (0,255,0), 3)
    
    #affichage de l'image
    cv2.imshow("frame", frame)
    cv2.moveWindow("frame", 0, 0)
    cv2.imshow("frame2", frame2)
    cv2.moveWindow("frame2", 700, 0)    
    
    if cv2.waitKey(1) == ord('g'):
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
            
            
            ####
            _sortie = str(sortie_u) +"_"+ str(sortie_r) +"_"+ str(sortie_f) +"_"+ str(sortie_d) +"_"+ str(sortie_l) +"_"+ str(sortie_b)

            _sortie = str(_sortie)
            _sortie=_sortie.replace("[","")
            _sortie=_sortie.replace("]","")
            _sortie=_sortie.replace(",","")
            _sortie=_sortie.replace("'","")
            _sortie=_sortie.replace(" ","")
            _sortie = _sortie.lower()
            print(_sortie)
            ####
            
            
            
            
            sortiee=sortie[0:6]+"X"+sortie[7:15]+"X"+sortie[16:20]+"X"+sortie[21:35]+"X"+"X"+sortie[37:53]+"X"
            print(sortiee)


            
            face6=miss_face(["?",sortie[38],sortie[18]])
            face15=miss_face([sortie[29],"?",sortie[26]])
            face20=miss_face([sortie[8],"?",sortie[9]])
            face35=miss_face(["?",sortie[51],sortie[17]])
            face36=miss_face([sortie[0],sortie[47],"?"])
            face53=miss_face([sortie[33],sortie[42],"?"])
            
            sortie=sortie[0:6]+face6+sortie[7:15]+face15+sortie[16:20]+face20+sortie[21:35]+face35+face36+sortie[37:53]+face53
            
            print("***")
            print(face6)
            print(face15)
            print(face20)
            print(face35)
            print(face36)
            print(face53)
            
            print(sortie)
            #print("woggworywogwrbbgbrgrbrrboryywrwywgbybywgggooboyryowboy")
            
                        
            print("rouge", sortie.count("r"))
            print("bleu", sortie.count("b"))
            print("orange", sortie.count("o"))
            print("jaune", sortie.count("y"))
            print("vert", sortie.count("g"))
            print("blanc", sortie.count("w"))

            #dessin des faces pour une meilleure visualisation
            cube1 = cv2.bitwise_and(frame, 0)  #creation image visualisation du cube
            cube2 = cv2.bitwise_and(frame2, 0)
            drawface(cube1, 75, 10, 50, sortie_u)
            drawface(cube1, 2, 170, 50, sortie_r)
            drawface(cube1, 157, 170, 50, sortie_b)
            drawface(cube2, 75, 10, 50, sortie_d)
            drawface(cube2, 2, 170, 50, sortie_f)
            drawface(cube2, 157, 170, 50, sortie_l)
            cv2.imshow("cube", cube1)
            cv2.moveWindow("cube", 0, 500)
            cv2.imshow("cube2", cube2)
            cv2.moveWindow("cube2", 700, 500)
            
            
      
    if cv2.waitKey(1) == ord('r'):
        Data = pd.DataFrame(columns=['rbk_str'], dtype='str')
        Data.loc['rbk_str'] = str(sortie)
        Data.to_csv(os.path.join("../data/generated_data/prediction.csv"))
        
      
        
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
