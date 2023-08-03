"""
Juego de Gato
"""
import numpy as np

matriz = np.zeros((3,3))
vals = [["_","_","_"],["_","_","_"],["_","_","_"]]#print(vals)

def win(): 
    for i in range(3):
        q,w,e = matriz[i].astype(int)
        if q & w & e == q:
            print("Fin del juego")
            return True
    for i in range(3):
        q,w,e = matriz[:,i].astype(int)
        if q & w & e == q:
            print("Fin del juego")
            return True

    if matriz[0][0].astype(int) & matriz[1][1].astype(int) & matriz[2][2].astype(int) == matriz[0][0].astype(int):
        print("fin del juego")
        return True
    
    if matriz[0][2].astype(int) & matriz[1][1].astype(int) & matriz[2][0].astype(int) == matriz[0][2].astype(int):
        print("fin del juego")
        return True
    return False

def comprobar(j,i,o):
    x = i-1
    y = o-1
    matriz[x][y]=j 
    if j == 1:
        vals[x][y]="X"
    else:
        vals[x][y]="O"

contador = 0
while True:

    FT =f"""
      1   2   3
   1 _{vals[0][0]}_|_{vals[0][1]}_|_{vals[0][2]}_
   2 _{vals[1][0]}_|_{vals[1][1]}_|_{vals[1][2]}_
   3 _{vals[2][0]}_|_{vals[2][1]}_|_{vals[2][2]}_
    
   """
    print(FT)

    j1x,j1y = input("Ingresa 'x' en la posicion que quieres:").split()
    comprobar(1,int(j1x),int(j1y))
    if contador>2:
        gana = win()
        if gana is True:
            break
    j2x,j2y = input("Ingresa 'O' en la posicion que quieres:").split()
    comprobar(2,int(j2x),int(j2y))
    if contador>3:
        ganaa = win()
        if ganaa is True:
            break

    #print(FT)
    #print(matriz)
    #print(vals)
    #print(FT)
    contador+=1
    if contador ==9:
        break

#print(matriz[:,0])

print(FT)