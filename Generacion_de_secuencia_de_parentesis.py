#1051
import sys
def proceso(ltr, a,c , n):
    if a == n and c == n:
        print(ltr)
    if a < n:
        proceso(ltr+'(', a + 1, c, n)
    if a > c:
        proceso(ltr+')', a, c + 1, n)
def main():
    for entrada in sys.stdin:
        if entrada == '\n':
            break
        proceso('', 0, 0, int(entrada))
main()
    