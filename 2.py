from math import *

def nod(a, b):
    d = []
    m = min(a, b)
    for i in range(1, m + 1):
        if (a % i == 0) and (b % i == 0):
            d.append(i)
    return max(d)


w, p = input(), input()

if w.isdigit() and p.isdigit() and int(w) > 0 and int(p) > 0:
    w = int(w)
    p = int(p)
    if nod(w, p) == gcd(w, p):
        print('Наибольший общий делитель', nod(w, p))

else:
    print('ERROR')