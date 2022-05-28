#1148
from queue import PriorityQueue
def main():
    n = int(input())
    res = 0; dato = 0
    pq = PriorityQueue()
    while n != 0:
        res = 0
        lst = list(map(int, input().split()))
        [pq.put(i) for i in lst]
        while pq.qsize() > 1:
            dato = pq.get()
            dato += pq.get()
            pq.put(dato)
            res += dato
        pq.queue.pop()
        print(res)
        n = int(input())
     
main()