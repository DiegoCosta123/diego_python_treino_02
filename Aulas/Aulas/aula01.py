# nome = input('Digite seu nome?: ')

# if nome == 'Gustavo':
#    print('Que nome top!!!!!!!')
# elif nome == 'Fulano' or nome == 'Pedro' or nome == 'Guilherme' or nome == 'Matheus':
#    print('Seu nome é bem popular no Unifeso!')
# else:
#    print('Ok.')


# print(f'Tenha uma boa noite, {nome}!')


#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   Exercícios Condição:

   26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
   na tela uma das mensagens abaixo:
   - O primeiro valor é o maior
   - O segundo valor é o maior
   - Não existe valor maior, os dois são iguais
'''

# num01 = int(input('1° Valor: '))
# num02 = int(input('2° Valor: '))

# if num01 > num02:
#    print('O primeiro valor é o maior.')

# elif num01 < num02:
#    print('O segundo valor é maior')

# else:
#    print('Não existe valor maior, os dois são iguais.')

# print('FIM...')



#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
   mostrando uma mensagem no final, de acordo com a média atingida:
   - Média até 4.9: REPROVADO
   - Média entre 5.0 e 6.9: RECUPERAÇÃO
   - Média 7.0 ou superior: APROVADO
'''

# n1 = float(input('Nota 1ª: '))
# n2 = float(input('Note 2ª: '))

# media = (n1 + n2) / 2

# if media <= 4.9:
#    print(f'Média: {media:.2f} -> REPROVADO')

# elif media >= 5.0 and media < 7.0:
#    print(f'Média: {media:.2f} -> RECUPERAÇÃO')

# else:
#    print(f'Média: {media:.2f} -> APROVADO')



#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
   de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
   em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
   ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

# valorCasa = float(input('Digite o valor da casa: R$'))
# salario = float(input('Digite o salario do comprador: R$'))
# anos = float(input('Quantos anos deseja pagar: '))

# totalMeses = anos * 12
# prestacao = valorCasa / totalMeses

# limite = salario * 0.30

# print(f"\nPrestação mensal: R$ {prestacao:.2f}")
# print(f"Limite de 30% do salário: R$ {limite:.2f}")

# if prestacao <= limite:
#    print("Empréstimo APROVADO!")

# else:
#    print("Empréstimo NEGADO!")



#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
   peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
   indivíduo dentro de certas faixas.
      Exemplo:
         - abaixo de 18.5: Abaixo do peso
         - entre 18.5 e 25: Peso ideal
         - entre 25 e 30: Sobrepeso
         - entre 30 e 40: Obesidade
         - acima de 40: Obseidade mórbida
'''

# peso = float(input('Peso: '))
# altura = float(input('Altura: '))

# imc = peso / (altura ** 2)

# if imc <= 18.5:
#    print(f'IMC: {imc:.2f} -> Abaixo do peso')

# elif imc >= 18.5 and imc < 25:
#    print(f'IMC: {imc:.2f} -> Peso ideal')

# elif imc >= 25 and imc < 30:
#    print(f'IMC: {imc:.2f} -> Sobrepeso')

# elif imc >= 30 and imc < 40:
#    print(f'IMC: {imc:.2f} -> Obesidade')

# else:
#    print(f'IMC: {imc:.2f} -> Obseidade mórbida')



#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
   aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
   carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
   que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
   quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
   tabela a seguir:
      - Carros populares (aluguel de R$90 por dia):
         - Até 100Km percorridos: R$0,20 por Km
         - Acima de 100Km percorridos: R$0,10 por Km
      
      - Carros de luxo (aluguel de R$150 por dia):
         - Até 200Km percorridos: R$0,30 por Km
         - Acima de 200Km percorridos: R$0,25 por Km
'''

# tipoCarro = str(input('Digite o tipo de carro [Popular / Luxo]: '))
# dias = int(input('Digite a quantidade de dias de aluguel: '))
# km = float(input('Digite a quantidade de km percorridos: '))

# # Carro Popular:
# if tipoCarro == 'Popular':
#    preco_dia = 90

#    if km <= 100:
#       preco_km = km * 0.20
#    else:
#       preco_km = km * 0.10

# # Carro Luxo:
# else:
#    preco_dia = 150

#    if km == 200:
#       preco_km = km * 0.30
#    else:
#       preco_km = km * 0.25


# total = (dias * preco_dia) + preco_km

# print(f'O valor total a pagar: R${total:.2f}')



#------------------------------------------------------------------------------------------------------------------------------------------------------



