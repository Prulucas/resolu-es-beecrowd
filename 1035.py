x = input().split()
a, b, c, d = x
a = int(a)
b = int(b)
c = int(c)
d = int(d)
soma1 = c + d
soma2 = a + b
if b > c and d > a and soma1 > soma2 and soma1 > 0 and soma2 > 0 and a % 2 == 0:
        print("Valores aceitos")
else:
    print("Valores nao aceitos")
