import math
a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorab = ((a + b) + abs(a-b))/2
maiorac = ((a + c) + abs(a-c))/2
maior = ((maiorab + maiorac) + abs(maiorab-maiorac))/2
print('{:.0f} eh o maior' .format(maior))