#2276
def main():
    n = int(input())
    for j in range(n):
        c = input()
        t = len(c)
        sw = True
        lista = []
        for ltr in c:
            if ltr != ' ':
                if ltr == '(' or ltr == '[':
                    lista.append(ltr)
                elif len(lista) == 0:
                    sw = False
                    break
                elif ltr == ')' or ltr == ']':
                    ch = lista.pop(len(lista) - 1)
                    if ch != '(' and ltr == ')':
                        sw = False
                        break
                    elif ch != '[' and ltr == ']':
                        sw = False
                        break
            else:
                sw = False
                break
        if sw and len(lista) == 0:
            print("Yes")
        else:
            print("No")
main()