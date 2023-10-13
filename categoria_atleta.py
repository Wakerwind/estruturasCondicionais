from datetime import date

ano = date.today().year

nasc = int(input('Digite seu ano de nascimento: '))

idade = ano-nasc

if idade <= 9:
    print('Mirim')

elif idade <= 14:
    print('Infantil')

elif idade <= 19:
    print('junior')

elif idade <= 25:
    print('Sênior')

else: print('Master')


