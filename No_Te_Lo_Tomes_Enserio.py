#1986
def main():
    t=int(input())
    for i in range(t):
        cadena=str(input()); lista=[]
        for j in range(0,len(cadena),1):
            if cadena[j]!=" ":
                if j!=0:
                    lista.append(cadena.count(cadena[j]))
                    if lista[j-1]!=lista[j]:
                        break
                else:
                    lista.append(cadena.count(cadena[j]))
            else:
                lista.append(lista[j-1])
        if j+1==len(cadena):
            print("No te lo tomes enserio")
        else:
            print("Meh")
main()