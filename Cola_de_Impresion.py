#1383
from collections import deque
from queue import PriorityQueue
def main():
    dato = 0
    n = int(input())
    for j in range(n):
        colaS = deque([])
        colaPrior = PriorityQueue()
        resp = 0
        tam , p = map(int, input().split())
        temp = list(map(int, input().split()))
        [colaPrior.put(-i) for i in temp]
        [colaS.append(i) for i in temp]
        tam -= 1
        while True:
            m = -colaPrior.get()
            dato = colaS[0]
            while dato != m:
                colaS.popleft()
                colaS.append(dato)
                dato = colaS[0]
                if p != 0:
                    p -= 1
                else:
                    p = tam
            colaS.popleft()
            resp += 1
            tam -= 1
            if p == 0:
                break
            else:
                p -= 1
        print(resp)
main()