#1107
def proceso(cadena):
    pila = []
    for i in range(len(cadena)):
        if cadena[i].isnumeric():
            pila.append(ord(cadena[i])- ord('0'))
        else:
            a = int(pila[-1])
            pila.pop()
            b = int(pila[-1])
            pila.pop()
            if cadena[i] == '+':
                pila.append(a + b)
            else:
                pila.append(a * b)
    return pila.pop()
def main():
    while True:
        try:
            entrada = input()
            print(proceso(entrada))
        except:
            break
            
main()
