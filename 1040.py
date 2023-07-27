linha = input('').split()
a, b, c, d = linha
a = float(a)
b = float(b)
c = float(c)
d = float(d)
media = ((a * 2) + (b * 3) + (c * 4) + d) / 10
final = 0
print('Media: {:.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exam = float(input(''))
    print('Nota do exame: {:.1f}'.format(exam))
    final = (media + exam) / 2
    print('Aluno aprovado.' if final >= 5 else 'Aluno reprovado.')
    print('Media final: {:.1f}'.format(final))
