linha = input('').split()
x, y = linha #x o codigo do produto, y a quantidade do produto
x = int(x)
y = int(y)
total = 0
if x == 1:
    total = 4 * y
elif x == 2:
    total = 4.50 * y
elif x == 3:
    total = 5 * y
elif x == 4:
    total = 2 * y
elif x == 5:
    total = 1.50 * y
print('Total: R$ {:.2f}'.format(total))
