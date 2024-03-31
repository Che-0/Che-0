import numpy as np
import os

matrix = np.array([[' ' , ' ',  ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

def posicion(y):
    x = list(map(int, input("Introduce numeros ").split()))
    a = x[0]
    b = x[1]
    if y == 2:
        matrix[a][b] = "o"
    else:
        matrix[a][b] = "x"

def comprobar(j):
    jugador = "J1" if j == 1 else "J2"
    v = 'x' if j == 1 else 'o'
        
    if  ((matrix[0,0] == matrix[1,1] == matrix[2,2] == v) or 
        (matrix[0,2] == matrix[1,1] == matrix[2,0] == v) or
        (np.all(matrix[0:3,0] == v) or np.all(matrix[0:3,1] == v) or np.all(matrix[0:3,2] == v) or
        np.all(matrix[0,0:3] == v) or np.all(matrix[1,0:3] == v) or np.all(matrix[2,0:3] == v))):
        print(f"Ganaste {jugador}")
        return False
    elif np.all(matrix != ' '):
        print("Empate")
        exit()
    else:
        return True

while True:
    print("Jugador 1 x")
    posicion(1)
    print(matrix)
    fin = comprobar(1)
    if not fin:
        break
    
    print("jugador 2")
    posicion(2)
    print(matrix)
    
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    fin = comprobar(2)
    if not fin:
        break