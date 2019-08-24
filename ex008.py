# O programa le um valor em metros e o exibe convertido em centimetros e milimetros

metros = float(input('Entre com a distancia em metros: '))

centimetros = metros * 100
milimetros = metros * 1000
kilometros = metros / 1000.0

print('{} metros e {:.0f} centimetros'.format(metros, centimetros))
print('{} metros e {} milimetros'.format(metros, milimetros))
print('{} metros e {} kilometros'.format(metros, kilometros))