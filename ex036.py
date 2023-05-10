Casa = float(input('Qual o Valor da Casa: R$  '))
Salario = float(input(' Salario do comprador: R$ '))
anos = int(input(' Quantos anos de financiamento? '))
prestação = Casa / (anos * 12)
minimo = Salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(Casa, anos, end=''))
print(' A prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Enprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO! ')