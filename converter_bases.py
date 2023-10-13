val = int(input('Digite um número: '))

print('- 1 Binário\n - 2 Octal\n - 3 Hexadecimal')
op = int(input('Escolha uma base para converter: '))



if op == 1:
    print(f'{val} para binário = {bin(val) [2:]}')
elif op == 2:
    print(f'{val} para octal = {oct(val) [2:]}')
elif op == 3:
    print(f'{val} para hexadecimal = {hex(val) [2:]}')
else: print('Opção inválida')