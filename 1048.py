sal = float(input())

if 0 < sal <= 400:
    reajus = ((sal*15) / 100)
    novosal = sal + reajus
    por = 15
elif sal <= 800:
    reajus = ((sal*12) / 100)
    novosal = sal + reajus
    por = 12
elif sal <= 1200:
    reajus = ((sal*10) / 100)
    novosal = sal + reajus
    por = 10
elif sal <= 2000:
    reajus = ((sal*7) / 100)
    novosal = sal + reajus
    por = 7
elif sal > 2000:
    reajus = ((sal*4) / 100)
    novosal = sal + reajus
    por = 4

print('Novo salario: {:.2f}'.format(novosal))
print('Reajuste ganho: {:.2f}'.format(reajus))
print('Em percentual: {} %'.format(por))
