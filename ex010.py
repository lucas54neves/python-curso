reais = float(input('Quanto dinheiro voce tem na carteira? R$'))

dolares = reais / 3.27

print('Com R${:.2f} voce pode comprar US${:.2f}'.format(reais, dolares))