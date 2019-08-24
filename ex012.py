preco = float(input('Qual o preco do produto? R$'))

novo_preco = preco * 0.95

print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(preco, novo_preco))