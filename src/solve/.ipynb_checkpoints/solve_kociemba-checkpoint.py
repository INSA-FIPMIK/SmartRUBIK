import kociemba
import pandas as pd


def solve_kociemba():
    rbk_str = pd.read_csv('../data/generated_data/prediction.csv')
    cube = rbk_str.iloc[0]['rbk_str']
    print(cube)
    cube=cube.replace('w','U')
    cube=cube.replace('b','R')
    cube=cube.replace('r','F')
    cube=cube.replace('y','D')
    cube=cube.replace('g','L')
    cube=cube.replace('o','B')
    print(cube)
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
    #ser.write(sol.encode('ascii'))

    # Disable the solve button
    button_solve.config(state="disable")
    return