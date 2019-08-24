# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

media = (nota1 + nota2) / 2.0

print('A media entre {:.1f} e {:.1f} e igual a {:.1f}'.format(nota1, nota2, media))