preco = float(input('Digite o valor da casa: '))
sal = float(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos a casa vai ser paga? '))


prestacao = preco / (anos*12)

if prestacao <= sal*0.30:

    print('Emprestimo aprovado  com prestação de: R$ ', prestacao)

else:
    print('Emprestimo negado, sua prestação excede 30% do seu salário!')






