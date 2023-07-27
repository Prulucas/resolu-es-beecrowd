a,b,c = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis

# Converte o valor para os tipos necessários
a = float(a)
b = float(b)
c = float(c)
tri = (a * c)/2
cir = 3.14159 * (c ** 2)
tra = ((a + b) * c)/2
quad = b ** 2
ret = a * b
print('TRIANGULO: {:.3f}' .format(tri))
print('CIRCULO: {:.3f}' .format(cir))
print('TRAPEZIO: {:.3f}' .format(tra))
print('QUADRADO: {:.3f}' .format(quad))
print('RETANGULO: {:.3f}' .format(ret))