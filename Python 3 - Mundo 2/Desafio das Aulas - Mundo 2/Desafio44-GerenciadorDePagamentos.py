'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''
print('======= LOJAS =======')
preco = float(input('\nPreço das compras: R$ '))
print('''\nFORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('\nQual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('\nSua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('\nSua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
