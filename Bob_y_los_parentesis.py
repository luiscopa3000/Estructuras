#1233
def main():
    n = int(input())
    for i in range(n):
        c = input()
        sw = True
        val = []
        for letr in c:
            if letr != ' ':
                if letr == '(' or letr == '[':
                    val.append(letr)
                elif len(val) == 0:
                    sw = False
                    break
                elif letr == ')' or letr == ']':
                    ch = val.pop(len(val) - 1)
                    if ch != '(' and letr == ')':
                        sw = False
                        break
                    elif ch != '[' and letr == ']':
                        sw = False
                        break
        if sw and len(val) == 0:
            print("Yes")
        else:
            print("No")
main()