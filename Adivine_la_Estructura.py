#1046
from collections import deque
from queue import PriorityQueue
import sys
def main():
    n = 1; c = 0; d=0; ele = 0
    sw1 = False; sw2 = False; sw3 = False
    for linea in sys.stdin:
        if str(linea) == "\n":
            break
        else:
            sw1 = True
            sw2 = True
            sw3 = True
            p = []
            q = deque([])
            pq = PriorityQueue()
            n = int(linea)
            while n > 0:
                c, d = map(int, input().split())
                if c == 1:
                    p.append(d)
                    q.append(d)
                    pq.put(d)
                else:
                    if len(p) >0 and sw1:
                        ele = p[-1]
                        p.pop()
                        if d != ele:
                            sw1 = False
                    else:
                        sw1 = False
                        
                    if len(q)>0 and sw2:
                        ele = q[0]
                        q.popleft()
                        if d != ele:
                            sw2 = False
                    else:
                        sw2 = False
                    if not pq.empty() and sw3:
                        ele = pq.queue[-1]
                        pq.queue.pop()
                        if d != ele:
                            sw3 = False
                    else:
                        sw3 = False
                n -= 1
            if sw1 and not sw2 and not sw3:
                print("stack")
            elif not sw1 and sw2 and not sw3:
                print("queue")
            elif not sw1 and not sw2 and sw3:
                print("priority queue")
            elif not sw1 and not sw2 and not sw3:
                print("impossible")
            else:
                print("not sure")
main()
                
            
            