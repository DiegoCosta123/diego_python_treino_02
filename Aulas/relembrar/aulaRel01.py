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
# Exercícios 63 - Sequência de Fibonacci:



