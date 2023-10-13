from random import choice

opcoes = ['pedra','papel','tesoura']

print('Pedra, Papel, Tesoura')

jogador  = False

while (jogador in opcoes) == False:

    jogador = input('Escolha uma opção: ').lower()

computador = choice(opcoes)

print('Computador jogou: ',computador)
print('Jogador jogou: ',jogador)

if computador == 'pedra':

    if jogador == 'papel':
        print('Jogador ganhou!')

    elif jogador == 'tesoura':
        print('Jogador perdeu!')

    else:
        print('Empate!')

elif computador == 'papel':

    if jogador == 'tesoura':
        print('Jogador ganhou!')

    elif jogador == 'pedra':
        print('Jogador Perdeu!')

    else:
        print('Empate!')

else:

    if jogador == 'pedra':
        print('Jogador ganhou!')

    elif jogador == 'papel':
        print('Jogador Perdeu!')

    else:
        print('Empate!')

