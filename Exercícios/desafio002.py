'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

# import time

# for c in range(10, -1, -1):
#    time.sleep(1)
#    print(c)

# time.sleep(1)
# print('FELIZ ANO NOOOVOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!')



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# for c in range(2, 51, 2):
#    print(c, end=' ')

# print('FIM...')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

# soma = 0
# contador = 0

# for c in range(1, 501, 2):
#    if c % 3 == 0:
#       contador += 1
#       soma += c

# print(f'Somar de todos os {contador} valores impares é: {soma}')



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
 Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

# tabuada = int(input('Qual número de tabuada você quer?: '))

# for n in range(1, 11):
#    resultado = tabuada * n
#    print(f'{tabuada} X {n} = {resultado}')



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

# soma = 0
# cont = 0

# for c in range(1, 7):
#    num = int(input(f'Digite o {c}º valor: '))

#    if num % 2 == 0:
#       soma += num
#       cont += 1

# print(f'Você informou {cont} números PARES e a soma foi {soma}.')



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
# primeiroTermo = int(input('Primeiro Termo: '))
# razao = int(input('Razão: '))

# decimo = primeiroTermo + (10 - 1) * razao

# for i in range(primeiroTermo, decimo + razao, razao):
#    print(f'{i}', end=' -> ')

# print('ACABOOUUU!!!!!!')



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
- Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

# num = int(input('Digite um número: '))

# for c in range(1, num + 1):
#    if num % c == 0:
#       print('\033[33m', end=' ')
#    else:
#       print('\033[34m', end=' ')

#    print(f'{c}', end=' ')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Repetir:

Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

# soma = 0
# cont = 0

# for c in range(1, 501, 2):
#    if c % 3 == 0:
#       soma += c
#       cont += 1

# print(f'A soma de todos os {cont}x valores solicitados e resultado é: {soma} ')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Repetir:

- Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

'''

num = int(input('Digite um número: '))

for n in range(1, 11):
   resp = num * n
   print(f'{num} X {n} = {resp}')

print('\nFIM...')

