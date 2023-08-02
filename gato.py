"""
Se supone que este es un juego de gato en la consola
"""
import os


win = [[0,7,14],[4,7,10],[0,2,4],[5,7,9],[10,12,14],[0,5,10],[2,7,12],[4,9,14]]


F = True


def cambiar(val,xval,yval): #x & y son las coordenadas de la matriz

    """
Funcion para cambiar x y o

Args:
    val: valor entero que recibe 0 o 1 
    xval: es la posicion de la fila
    yval: es la posicion de la columna

Returns:
    Cambia los valores de la matriz inicial 

Raises:
    KeyError: Raises an exception.
"""
    pos = ""
    if val == 0:
        pos ="X"
    else:
        pos ="O"
    #print(x,y)
    valx = int(xval)
    valy = int(yval)
    formato[valx][valy] = pos

    for listas in formato:
        for combinacion in win:
            if listas in combinacion:
                return True

formato = [['_', '|', '_', '|', '_'],['_', '|', '_', '|', '_'],['_', '|', '_', '|', '_']]

L = """
     0         2         4
 0 ['_', '|', '_', '|', '_']
 1 ['_', '|', '_', '|', '_']
 2 ['_', '|', '_', '|', '_']

"""

print(L)
#formato 12 22   coordenadas alv

S = 0
while S == 0:
    print("formato")
    print(L)
    #for i in range(len(formato)):
    #    print(formato[i])
    for i in range(3):
        print(formato[i])
    print("En que posicion quieres poner X ?")
    x,y = input().split()
    J1 = cambiar(0,x,y)
    if J1 is True:
        print("J2 gana")
        S+=1
    print("En que posicion quieres poner O ?")
    x,y = input().split()
    J2 = cambiar(1,x,y)
    if J2 is True:
        print("J2 gana")
        S+=1
    os.system("cls")
