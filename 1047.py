a, b, c, d = list(map(int, input().split()))
if a < c:
    h = c - a
    if b < d:
        m = d - b
    if b > d:
        h = h - 1
        m = (60 - b) + d
    if b == d:
        m = 0
if a > c:
    h = (24 - a) + c
    if b < d:
        m = d - b
    if b > d:
        h = h - 1
        m = (60 - b) + d
    if b == d:
        m = 0
if a == c:
    if b < d:
        m = d - b
        h = 0
    if b > d:
        m = (60 - b) + d
        h = 23
    if b == d:
        h = 24
        m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))
