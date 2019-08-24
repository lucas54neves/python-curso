# 60 reais por dia e 15 centavos por km rodado
km_percorridos = float(input('Qual a quantidade de Km percorridos? '))
dias = float(input('Qual a quantidade de dias? '))

custo = (dias * 60) + (km_percorridos * 0.15)

print('O total a pagar e de R${:.2f}'.format(custo))