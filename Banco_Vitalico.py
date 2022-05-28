#1176
def ordena(lis,i, cont):
    temp = lis[:i]
    aux = []; aux2 = []
    for j in  range(i,len(lis)):
        if lis[j][0] < cont:
            if lis[j][1] == "R":
                aux.append(lis[j])
            else:
                aux2.append(lis[j])
        else:
            break
    lis = (temp+aux+aux2)
def proceso(lis, timpoMax,intervalo):
    cont = lis[0][0]
    larg = len(lis)
    for i in range(larg):
        if lis[i][0] < cont and lis[i][1] != "R":
            ordena(lis,i,cont)
        if cont + intervalo <= timpoMax:
            cont += intervalo
            print(cont)
        else:
            print("Mil disculpas, regrese mañana")
def main():
    while True:
        try:
            n ,m,p = map(int,input().split())
            lis = []
            for i in range(int(n)):
                x,y = map(str,input().split())
                lis.append([int(x),y])
            proceso(lis,m,p)
        except:
            break
main()
        
    
    