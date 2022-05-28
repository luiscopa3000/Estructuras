#Leer un archivo de texto
def leerArch():
    archivo = open("archivo.txt", "r")
    lineas = archivo.readlines()
    temp = ""
    for linea in lineas:
        temp =  linea+ "\n"+ temp
    return temp
#estraer palabras cada coma, espacio, punto, etc
def extrae(texto, temp={}):
    import re
    busqueda = re.split(r"[ ,.^$*+?{}:()\n]", texto)
    for i in busqueda:
        if i in temp and i != "":
            temp[i] += 1
        elif i != "":
            temp[i] = 1
    return temp
def main():
    texto = str(leerArch()).lower()
    print("TEXTO:", texto)
    lis = extrae(texto)
    orden = sorted(lis.items(), key=lambda x: x[1], reverse=True)
    for i in orden:
        print(*i)
main()