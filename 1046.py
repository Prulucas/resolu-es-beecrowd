a, b = list(map(int, input().split()))
dura = 0
if a < b:
    tempo = b - a
else:
    tempo = (24 - a) + b
print('O JOGO DUROU {} HORA(S)'.format(tempo))
