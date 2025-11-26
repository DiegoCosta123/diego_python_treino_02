'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

# casa = float(input('Valor da casa: R$'))
# salario = float(input('Salário do comprador: R$'))
# anos = int(input('Quantos anos de financiamento?: '))

# prestacao = casa / (anos * 12)
# minimo = salario * 30 / 100

# print(f'- Para pagar uma casa de R${casa:.2f} em {anos} anos.\n- A prestação será de R${prestacao:.2f}.')
# print(f'- COMPARANDO: Tem que pagar R${prestacao:.2f} e o mínimo é de R${minimo:.2f}.')

# if prestacao <= minimo:
#    print('Empréstimo pode ser CONCEDIDO!')

# else:
#    print('Empréstimo NEGADO.')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
IMPORTANTES:
   - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
      - 1 para binário
      - 2 para octal
      - 3 para hexadecimal.

'''

# num = int(input('Digite um número inteiro: \033[0;35m'))
# print(''' \033[m
# - Escolha uma das bases para conversão:
# [ 1 ] Converter para BINÁRIO
# [ 2 ] Converter para OCTAL
# [ 3 ] Converter para HEXADECIMAL
# ''')

# opcao = int(input('Sua opção: \033[0;35m'))
# print('\033[m')

# if opcao == 1:
#    print(f'Número: {num} -> Binário: {bin(num)[2:]}')

# elif opcao == 2:
#    print(f'Número: {num} -> Octal: {oct(num)[2:]}')

# elif opcao == 3:
#    print(f'Número: {num} -> Hexadecimal: {hex(num)[2:]}')

# else:
#    print('\033[0;31mOpção inválida. Tente novamente.\033[0m')

# print('FIM...')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
   – O primeiro valor é maior
   – O segundo valor é maior
   – Não existe valor maior, os dois são iguais
'''

# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))

# if n1 > n2:
#    print('PRIMEIRO é maior.')

# elif n1 == n2:
#    print('Os números são iguais.')

# else:
#    print('SEGUNDO é maior.')

# print('FIM.')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

# import datetime

# atual = datetime.date.today().year
# anoNascimento = int(input('Qual ano você nasceu?: '))

# idade = atual - anoNascimento

# print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {atual}.')

# if idade == 18:
#    print('Você tem que se alistar IMEDIATAMENTE.')

# elif idade > 18:
#    saldo = idade - 18
#    print(f'Você já deveria ter se alistado há {saldo} anos.')

# elif idade < 18:
#    saldo = 18 - idade
#    print(f'Ainda faltam {saldo} anos para o alistamento.')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
   – Média abaixo de 5.0: REPROVADO
   – Média entre 5.0 e 6.9: RECUPERAÇÃO
   – Média 7.0 ou superior: APROVADO
'''

# n1 = float(input('Nota 1: '))
# n2 = float(input('Nota 2: '))

# media = (n1 + n2) / 2

# if media < 5.0:
#    print(f'Média: {media:.1f} -> REPROVADO')

# elif media >= 5.0 and media < 6.9:
#    print(f'Media: {media:.1f} -> RECUPERAÇÃO')

# else:
#    print(f'Media: {media:.1f} -> APROVADO')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
   – Até 9 anos: MIRIM
   – Até 14 anos: INFANTIL
   – Até 19 anos: JÚNIOR
   – Até 25 anos: SÊNIOR
   – Acima de 25 anos: MASTER
'''

# import datetime

# atual = datetime.date.today().year
# anoNascimento = int(input('Qual ano você nasceu?: '))

# idade = atual - anoNascimento

# if idade <= 9:
#    print(f'Idade: {idade} -> MIRIM')

# elif idade <= 14:
#    print(f'Idade: {idade} -> INFANTIL')

# elif idade <= 19:
#    print(f'Idade: {idade} -> JÚNIOR')

# elif idade <= 25:
#    print(f'Idade: {idade} -> SÊNIOR')

# else:
#    print(f'Idade: {idade} -> MASTER')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
   – EQUILÁTERO: todos os lados iguais
   – ISÓSCELES: dois lados iguais, um diferente
   – ESCALENO: todos os lados diferentes
'''

# r1 = float(input('Primeiro segmento: '))
# r2 = float(input('Segundo segmento: '))
# r3 = float(input('Terceiro segmento: '))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos acima PODEM FORMAR um triângulo.')

#    if r1 == r2 == r3:
#       print('- EQUILÁTERO')
   
#    elif r1 == r2 or r1  == r3 or r2 == r3:
#       print('- ISÓSCELES')
   
#    else:
#       print('- ESCALENO')

# else:
#    print('Os segmentos acima NÃO PODE FORMAR um triângulo.')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
   – à vista dinheiro/cheque: 10% de desconto
   – à vista no cartão: 5% de desconto
   – em até 2x no cartão: preço formal 
   – 3x ou mais no cartão: 20% de juros
'''

# print('{:=^100}'.format(' LOJAS FULANOS '))

# preco = float(input('Preço das compras: R$'))

# print('''
# - FORMAS DE PAGAMENTO -
# [ 1 ] à vista dinheiro/cheque
# [ 2 ] à vista no cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão
# ''')

# opcao = int(input('Qual é a opção?: '))

# if opcao == 1:
#    total = preco - (preco * 10 / 100)

# elif opcao == 2:
#    total = preco - (preco * 5 / 100)

# elif opcao == 3:
#    total = preco
#    parcela = total / 2
#    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')

# elif opcao == 4:
#    total = preco + (preco * 20 / 100)
#    parcTotal = int(input('Quantas parcelas?: '))
#    parcela = total / parcTotal
#    print(f'Sua compra será parcelada em {parcTotal}X de R${parcela:.2f} COM JUROS.')

# else:
#    total = 0
#    print('OPÇÃO INVÁLIDO! Tenta novamente!')


# print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

import random
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua opção?: '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POOOO!!!!!!!!!!!!!!!')

print("-=" * 12)
print(f'Computador: Jogou -> {itens[computador]}')
print(f'Jogador: Jogou -> {itens[jogador]}')
print("-=" * 12)

if computador == 0: # Computador jogou PEDRA
   if jogador == 0:
      print('EMPATE')

   elif jogador == 1:
      print('JOGADOR VENCE')

   elif jogador == 2:
      print('COMPUTADOR VENCE')

   else:
      print('JOGADA INVÁLIDA')

elif computador == 1: # Computador jogou PAPEL
   if jogador == 0:
      print('COMPUTADOR VENCE')

   elif jogador == 1:
      print('EMPATE')

   elif jogador == 2:
      print('COMPUTADOR VENCE')

   else:
      print('JOGADA INVÁLIDA')

elif computador == 2: # Computador jogou TESOURA
   if jogador == 0:
      print('JOGADOR VENCE')

   elif jogador == 1:
      print('COMPUTADOR VENCE')

   elif jogador == 2:
      print('EMPATE')

   else:
      print('JOGADA INVÁLIDA')


