x = input('').split()
a, b, c = x
a = float(a)
b = float(b)
c = float(c)

if a == 0.0 or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    delta = (b ** 2) - (4 * a * c)
    r1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    r2 = (- b - (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
