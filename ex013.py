salario_antigo = float(input('Qual e o salario do funcionario? R$'))

salario_novo = salario_antigo * 1.15

print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario_antigo, salario_novo))