#1386
from queue import PriorityQueue

def main():
    coleccion = PriorityQueue()
    resp = ''
    y = input()
    if len(y) == 1:
        resp = y
    else:
        resp = y[0]
        x = int(y[2:])
    
    while resp != 'T':
        if resp == 'S':
            dato = int(x)
            coleccion.put(-dato)
        elif resp == 'A':
            if len(coleccion.queue) != 0:
                z = coleccion.get()
                print(-z)
                coleccion.put(z)
            else:
                print('Error')
        elif resp == 'R':
            if len(coleccion.queue) != 0:
                coleccion.get()
            else:
                print('Error')
        elif resp == 'I':
            dato = int(x)
            if len(coleccion.queue) != 0:
                dato +=  -coleccion.get()
                coleccion.put(-dato)
            else:
                print('Error')
        elif resp == 'D':
            dato = int(x)
            if len(coleccion.queue) != 0:
                dato = -coleccion.get()-dato
                coleccion.put(-dato)
            else:
                print('Error')
                
        y = input()
        if len(y) == 1:
            resp = y
        else:
            resp = y[0]
            x = int(y[2:])
main()