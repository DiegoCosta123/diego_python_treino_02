# i = int(input('Digite um número início: '))
# f = int(input('Digite um número final: '))
# p = int(input('Digite um número de passos: '))

# for c in range(i, f, p):
#    print(f'-> {c}')

# print('FIM!!')


#----------------------------------------------------------------------------------------------------------------------------------------------------
# 46)

# import time

# for c in range(10, 0, -1):
#    print(f'{c}', end=' ')
#    time.sleep(0.5)

# print('IIIUUUUUUUUUUUU....')
# time.sleep(1)
# print('POPPOPOPOPOPOPOPOPOPOPOUu...')
# time.sleep(1)
# print('POOOOOUUUU')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# 47)

# for c in range(1, 51):
#    if c % 2 == 0:
#       print(c)

# print('FIM...')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# 48)

# soma = 0
# cont = 0

# for c in range(1, 501, 2):
#    if c % 3 == 0:
#       print(f'{c}', end=' ')
#       soma += c
#       cont += 1

# print(f'\nA soma todos os {cont} valores solicitados impares: {soma}')


#----------------------------------------------------------------------------------------------------------------------------------------------------
# 49)

# num = int(input('Escolhe um número: '))

# for c in range(1, 11):
#    mult = num * c
#    print(f'{num} X {c} = {mult}')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# 50)

# soma = 0
# cont = 0

# for c in range(1, 7):
#    num = int(input(f'Digite o {c}º valor: '))
#    if num % 2 == 0:
#       soma += num
#       cont += 1

# print(f'A soma de todos {cont} números de pares é: {soma}')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Relembre: Estrutura de Repetição While

# print('Repetição de FOR:')

# for c in range(1, 11):
#    print(c, end=' ')

# print('FIM')
# print('=-' * 20)


# print('Repetição de WHILE:')

# c = 1

# while c < 11:
#    print(c, end=' ')
#    c += 1

# print('FIM')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# resp = 'S'

# while resp == 'S':
#    cont = int(input('Digite un valor: '))
#    resp = str(input('Quer continuar? [s/n]: ')).upper()


# print('FIM!')



#----------------------------------------------------------------------------------------------------------------------------------------------------

# n = 1
# par = 0
# impar = 0

# while n != 0:
#    n = int(input('Digite um valor: '))

#    if n != 0:
#       if n % 2 == 0:
#          par += 1
#       else:
#          impar += 1
      

# print(f'Você digitou {par} números de pares e {impar} números de impares!')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 57:

# genero = str(input('Informe seu gênero [M/F]: ')).strip().upper()[0]

# while genero not in 'MmFf':
#    genero = str(input('Dados inválidos. Por favor, informe seu gênero: ')).strip().upper()[0]

# print(f'Gênero {genero} registrado com sucesso.')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 58:

# import random

# computador = random.randint(0, 10)

# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10!')
# print('Será que você consegue adivinhar qual foi?')

# acertou = False
# palpite = 0

# while not acertou:
#    jogador = int(input('Qual é seu palpite?: '))
#    palpite += 1

#    if jogador == computador:
#       acertou = True
   
#    else:
#       if jogador < computador:
#          print('Mais... Tente mais uma vez.')
#       elif jogador > computador:
#          print('Menos... Tente mais uma vez.')

# print(f'Acertou com {palpite} tentativas. Parabéns!')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 59:

# import time

# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# opcao = 0

# while opcao != 5:
#    print('''
#    [ 1 ] Somar
#    [ 2 ] Multiplicar
#    [ 3 ] Maior
#    [ 4 ] Novos números
#    [ 5 ] Sair do programa
#    ''')

#    opcao = int(input('Qual é a sua opção?: '))

#    if opcao == 1:
#       soma = n1 + n2
#       print(f'Soma: {n1} + {n2} = {soma}')
   
#    elif opcao == 2:
#       multiplicar = n1 * n2
#       print(f'Multiplicar: {n1} x {n2} = {multiplicar}')
   
#    elif opcao == 3:
#       if n1 > n2:
#          maior = n1
#       else:
#          maior = n2

#       print(f'Entre {n1} e {n2} o maior valor é {maior}!')
   
#    elif opcao == 4:
#       print('Informe os números novamente:')
#       n1 = int(input('Primeiro valor: '))
#       n2 = int(input('Segundo valor: '))
   
#    elif opcao == 5:
#       print('Finalizando...')
   
#    else:
#       print('Opção inválida. Tente novamente!')
   
#    print('=-=' * 50)
#    time.sleep(2)

# print('Fim do programa! Volte sempre!')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 60 - Fatorial:

# n = int(input('Dogite um número para calcular seu Fatorial: '))

# c = n
# f = 1

# print(f'Calculando {n}! = ', end='')

# while c > 0:
#    print(f'{c}', end='')
#    print(' x ' if c > 1 else ' = ', end='')
   
#    f *= c
#    c -= 1

# print(f'{f}')

#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 61 - Progressão Aritmética:

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da P.A: '))

# termo = primeiro
# cont = 1
# total = 0
# mais = 10

# while mais != 0:
#    total = total + mais

#    while cont <= total:
#       print(f'{termo}', end='')
#       print(' -> ' if cont < total else ' ', end='')
      
#       termo += razao
#       cont += 1

#    print('- PAUSA -')
#    mais = int(input('Quantos termos você quer mostrar a mais?: '))

# print(f'Progressão finalizada com {total} termos mostrados.')
# print('FIM')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 64 - Maior e Menor valores:

# resp = 'S'
# soma = 0
# quant = 0
# media = 0
# maior = 0
# menor = 0

# while resp in 'Ss':
#    num = int(input('Digite um número: '))

#    soma += num
#    quant += 1

#    if quant == 1:
#       maior = menor = num
   
#    else:
#       if num > maior:
#          maior = num
      
#       if num < menor:
#          menor = num

#    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]


# media = soma / quant

# print(f'Você digitou {quant} números e a média foi {media}')
# print(f'Maior número de valor é: {maior}')
# print(f'Menor número de valor é: {menor}')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Parte 3 - While Break:

# n = 0
# s = 0

# while True:
#    n = int(input('Digite um valor: '))

#    if n == 999:
#       break
#    s += n

# print(f'Resultado de todos os valores: {s}')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 66:

# s = 0
# quants = 0

# while True:
#    n = int(input('Digite um valor: '))

#    if n == 999:
#       break
   
#    quants += 1
#    s += n

# print(f'Quantos números foram digitados: {quants}')
# print(f'A soma de todos os valores: {s}')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 67 - Tabuada:

# r = 'S'

# while r in 'Ss':
#    num = int(input('Escolhe um número de tabuada: '))

#    if num < 0:
#       break

#    else:
#       for c in range(1, 11):
#          mult = num * c
#          print(f'{num} x {c} = {mult}')
         
#    r = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]

# print('Programa tabuada encerrado. Volte sempre!')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 68 - Jogo: Par ou Impar:

# import random

# v = 0

# while True:
#    jogador = int(input('-> Diga um valor: '))
#    computador = random.randint(0, 10)

#    total = jogador + computador
#    tipo = ' '

#    while tipo not in 'PI':
#       tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
   
#    print(f'\nJogador: {jogador}\nComputador: {computador}\nTotal: {total} ', end='')
#    print('-> PAR' if total % 2 == 0 else '-> IMPAR')

#    if tipo == 'P':
#       if total % 2 == 0:
#          print('---- Você VENCEU!! ----')
#          v += 1
#       else:
#          print('---- Você PERDEU. ----')
#          break
   
#    elif tipo == 'I':
#       if total % 2 == 1:
#          print('---- Você VENCEU!! ----')
#          v += 1
#       else:
#          print('---- Você PERDEU. ----')
#          break
   
#    print('\nVamos jogar novamente...')

# print(f'\nGAME OVER! Você venceu {v} vezes.')



#----------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios 69 - Análise de Dados do grupo:

# tot18 = 0 # Quantidade de pessoas com mais de 18 anos.
# totH = 0 # Quantidade dos homens com cadastrados.
# totM20 = 0 # Quantidade das mulheres com menos de 20 anos.

# while True:
#    idade = int(input('Idade: '))
   
#    genero = ' '
#    while genero not in 'MF':
#       genero = str(input('Gênero [M/F]: ')).strip().upper()[0]
   
#    if idade >= 18:
#       tot18 += 1
   
#    if genero == 'M':
#       totH += 1
   
#    if genero == 'F' and idade < 20:
#       totM20 += 1

#    resp = ' '
#    while resp not in 'SN':
#       resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
   
#    if resp == 'N':
#       break


# print(f'\n- Total de pessoas com mais de 18 anos: {tot18}')
# print(f'- Ao todo temos {totH} homens cadastrados.')
# print(f'- E temos {totM20} mulheres com menos de 20 anos.')
# print('\nPrograma encerrado.')



#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
- Exercícios 70 - Estatísticas em Produtos:
   - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
   No final, mostre:
      - A) Qual é o total gasto na compra.
      - B) Quantos produtos custam mais de R$1000,00.
      - C) Qual é o nome do produto mais barato.
'''

# total = 0
# totMil = 0
# menor = 0
# cont = 0
# barato = ''

# while True:
#    produto = str(input('Nome do produto: '))
#    preco = float(input('Preço: R$'))

#    total += preco
#    cont += 1

#    if preco > 1000:
#       totMil += 1

#    if cont == 1 or preco < menor:
#       menor = preco
#       barato = produto

#    resp = ' '
#    while resp not in 'SN':
#       resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
   
#    if resp == 'N':
#       break


# print('{:-^40}'.format(' FIM PROGRAMA '))
# print(f'-> O total do valor de gasto: R${total:.2f}') 
# print(f'-> Temos {int(totMil)} produtos custando mais de R$1000.00')
# print(f'-> O produto mais barato foi {barato} que custa R${menor:.2f}\n')



#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
 - Exercícios 71 - FINAL: Simulador de Caixa Eletrônico
'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor

ced = 50 # ced = Cédulas
totCed = 0 # totCed = Total de cédulas

while True:
   if total >= ced:
      total -= ced
      totCed += 1
   
   else:
      if totCed > 0:
         print(f'Total de {totCed} cédulas de R${ced}')
      
      if ced == 50:
         ced = 20
      elif ced == 20:
         ced = 10
      elif ced == 10:
         ced = 5
      elif ced == 5:
         ced = 1
      
      totCed = 0

      if total == 0:
         break

print('=' * 30)
print('Programa encerrado. Volte sempre ao BANCO CEV! Tenha uma boa tarde!')

