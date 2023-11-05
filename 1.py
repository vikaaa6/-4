from math import *

print('Введите величину угла в градусах')
n = input()

if n.isdigit():
    n = int(n)
    r = radians(n)
    print('Синус угла равен', sin(r))
    print('Косинус угла равен', cos(r))
    print('Тангенс угла равен', tan(r))
    
else:
    print('ERROR')

    