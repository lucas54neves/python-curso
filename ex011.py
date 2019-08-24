# Cada 2m^2 de parede precisa de 1l de tinta para ser pintado

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
custo = area / 2.0

print('Sua parede tem a dimensao de {}x{} e sua area e de {} m^2.'.format(largura, altura, area))
print('Para pintar essa parede, voce precisa de {} l de tinta.'.format(custo))