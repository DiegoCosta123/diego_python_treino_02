'''
   Estrutura de Repetição:
      - Estrutura de FOR:
'''

# s = 0

# for c in range(0, 5):
#    n = int(input('Digite um valor: '))
#    s += n

# print(f'A soma de todos os valores é: {s}')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# import time

# for cont in range(10, -1, -1):
#    print(cont, end=' ')
#    time.sleep(1)


# print('IIIIIIIUUUUUH... POPOPOPOu...POOU')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# for n in range(1, 51):
#    if n % 2 == 0:
#       print(n, end=' ')

# print('FIM!')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))

# for c in range(i, f + 1, p):
#    print(f'{c} -> Hello World!')

# print('FIM...')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input('Digite um número: '))

# for i in range(1, 11):
#    mult = n * i
#    print(f'{n} X {i} = {mult}')

# print('FIM...')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# print('\n')
# frase = str(input('Digite uma frase: ')).strip().upper()

# palavras = frase.split()
# juntos = ''.join(palavras)
# inverso = ''

# for letra in range(len(juntos) -1, -1, -1):
#    inverso += juntos[letra]

# print(f'Frase: {juntos}\nInverso: {inverso}')

# if inverso == juntos:
#    print('Temos um palíndromo!')
# else:
#    print('A frase digitada não é um palíndromo!')

# print('\n')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# import datetime

# atual = datetime.date.today().year

# totalMaior = 0
# totalMenor = 0

# for pessoas in range(1, 8):
#    nasc = int(input(f'Em que ano a pessoa nasceu? {pessoas}º: '))
#    idade = atual - nasc
   
#    if idade >= 21:
#       totalMaior += 1
#    else:
#       totalMenor += 1


# print(f'Ao todo tivemos {totalMaior} pessoas maiores de idade.')
# print(f'Ao todo tivemos {totalMenor} pessoas menores de idade.')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# for p in range(1, 6):
#    peso = float(input(f'Peso da {p}ª pessoa: '))

#    if p == 1:
#       maior = peso
#       menor = peso
   
#    else:
#       if peso > maior:
#          maior = peso
      
#       if peso < menor:
#          menor = peso


# print(f'\nO maior peso lido foi de {maior}kg')
# print(f'O menor peso lido foi de {menor}kg')


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# somaIdade = 0
# mediaIdade = 0

# maiorIdadeHomem = 0
# nomeVelho = 0

# totalMulher20 = 0

# for p in range(1, 5):
#    print('-=' * 30)
#    print('-' * 5, f' {p}ª PESSOA ', '-' * 5)

#    nome = str(input('Nome: ')).strip()
#    idade = int(input('Idade: '))
#    genero = str(input('Gênero [M / F]: ')).strip()

#    somaIdade += idade

#    if p == 1 and genero in 'Mm':
#       maiorIdadeHomem = idade
#       nomeVelho = nome
   
#    if genero in 'Mm' and idade > maiorIdadeHomem:
#       maiorIdadeHomem = idade
#       nomeVelho = nome
   
#    if genero in 'Ff' and idade < 20:
#       totalMulher20 += 1


# mediaIdade = somaIdade / 4

# print('\n')
# print(f'A média de idade do grupo é de {mediaIdade} anos.')
# print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
# print(f'Ao todo são {totalMulher20} mulheres com menos de 20 anos.')



#----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
   qualquer e mostre uma contagem até esse valor:
      - Ex: 
         - Digite um valor: 35
         - Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
'''

# numero = int(input('DIgite um número: '))

# for c in range(1, numero):
#    print(c, end=' ')

# print('ACABOU!')



#----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
   incremento, mostrando em seguida todos os valores no intervalo:
      - Ex: Digite o primeiro Valor: 3
      - Digite o último Valor: 10
      - Digite o incremento: 2
      - Contagem: 3 5 7 9 Acabou!
'''

# inicio = int(input('Início: '))
# fim = int(input('Final: '))
# incremento = int(input('Incremento: '))

# for cont in range(inicio, fim, incremento):
#    print(cont, end=" ")

# print('Acabou!')



#----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
48) Faça um programa que leia 7 números inteiros e no final mostre o somatório
entre eles.
'''

# num = int(input('Digite um número: '))

# soma = 0

# for c in range(1, num + 1):
#    print(c, end=' + ')
#    soma += c

# print(f'Resultado: {soma}')



#----------------------------------------------------------------------------------------------------------------------------------------------------------
'''
49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles
são pares e quantos são ímpares.
'''

# Meu Código:

# num = int(input('Digite um número: '))

# for c in range(1, num + 1):
#    print(c, end=' ')

#    if c % 2 == 0:
#       print('Par')
   
#    else:
#       print('Impar')


# Correção pelo ChatGPT:

# par = 0
# impar = 0

# for i in range(6):
#    num = int(input(f'Digite o {i + 1}º número: '))

#    if num % 2 == 0:
#       par += 1
   
#    else:
#       impar += 1


# print(f'Você digitou {par} números de pares e {impar} números ímpares.')


# Exercícios criado pelo ChatGPT:
'''
   - Exercício 1 — Positivos e Negativos Faça um programa que leia 7 números inteiros. Ao final, mostre quantos são positivos, quantos são negativos e quantos são iguais a zero.
'''

# positivo = 0
# negativo = 0
# igual = 0

# for i in range(7):
#    num = int(input(f'Digite o {i + 1}º número: '))

#    if num > 0:
#       positivo += 1
   
#    elif num == 0:
#       igual += 1
   
#    else:
#       negativo += 1

# print(f'Quantos são psitivos: {positivo}')
# print(f'Quantos são negativos: {negativo}')
# print(f'Quantos são iguais a zero: {igual}')



'''
Exercício 2 — Múltiplos de 3
Leia 10 números inteiros e informe quantos deles são múltiplos de 3 e quantos não são.

Dica: um número é múltiplo de 3 quando número % 3 == 0.
'''

# multiplo_tres = 0
# nao_multiplo = 0

# for i in range(10):
#    num = int(input(f'Digite o {i + 1}º número: '))

#    if num % 3 == 0:
#       multiplo_tres += 1
   
#    else:
#       nao_multiplo += 1


# print(f'Quantos são múltiplos de 3: {multiplo_tres}')
# print(f'quantos não são múltiplos de 3: {nao_multiplo}')



'''
   Exercício 3 — Idade por faixa
   Leia a idade de 8 pessoas e diga:
      - Quantas são menores de 18 anos
      - Quantas têm entre 18 e 59
      - E quantas são 60 ou mais
'''

# menor = 0
# entre = 0
# maior = 0

# for p in range(8):
#    idade = int(input(f'Pessoa {p + 1}º idade: '))

#    if idade < 18:
#       menor += 1
   
#    elif idade >= 18 and idade <= 59:
#       entre += 1
   
#    else:
#       maior += 1


# print(f'Quantas são menores de 18 anos: {menor}')
# print(f'Quantas têm entre 18 e 59: {entre}')
# print(f'Quantas são 60 ou mais: {maior}')



'''
Exercício 4 — Média dos números pares:
   - Leia 6 números inteiros e mostre a média apenas dos números pares digitados.
   - Se nenhum número par for digitado, mostre uma mensagem avisando isso.
'''

# soma = 0
# contagem = 0

# for i in range(6):
#    num = int(input(f'Digite o {i + 1}º número: '))

#    if  num % 2 == 0:
#       soma += num
#       contagem += 1
   

# if contagem > 0:
#    media = soma / contagem
#    print(f'A média dos números pares é: {media:.2f}')

# else:
#    print('Nenhum número par foi digitado!')



'''
Exercício 5 — Soma dos Ímpares:
   - Enunciado:
      Peça para o usuário digitar 5 números inteiros. Some apenas os números ímpares e mostre o resultado.
'''

# Meu código:

# soma = 0
# contagem = 0

# for i in range(6):
#    num = int(input(f'Digite o {i + 1}º número: '))

#    if  num % 2 != 0:
#       soma += num
#       contagem += 1
   

# if contagem > 0:
#    media = soma / contagem
#    print(f'A média dos números ímpares é: {media:.2f}')

# else:
#    print('Nenhum número ímpar foi digitado!')


# Correção pelo ChatGPT:

# soma = 0

# for i in range(5):
#    num = int(input(f'Digite o {i + 1}º número: '))

#    if num % 2 != 0:
#       soma += num

# print(f'A soma dos números ímpares é: {soma}')


#------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   Estrutura de Repetição:
      - Estrutura de WHILE:
'''

# Exemplo:

'''for c in range(1, 10):
   print(c)

print('FIM...')
'''

# c = 1

# while c < 10:
#    print(c)
#    c = c + 1

# print('FIM...')


# n = 1

# while n != 0:
#    n = int(input(f'Digite o {n}ª valor: '))

# print('FIM...')


# r = 'S'

# while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar [S/N]: ')).upper()

# print('FIM...')


# n = 1
# par = impar = 0

# while n != 0:
#    n = int(input('Digite um valor: '))

#    if n != 0:
#       if n % 2 == 0:
#          par += 1
#       else:
#          impar += 1


# print(f'Você digitou {par} números pares e {impar} números ímpares!')
# print('FIM...')



#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
- Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

# sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]

# while sexo not in 'MmFf':
#    sexo = str(input('Dados inválido. Por favor, informe seu sexo: ')).strip().upper()

# print(f'Sexo {sexo} registrado com sucesso.')


#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
- Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

# import random

# computador = random.randint(0, 10)
# print('Eu sou computador...  Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi? ')

# acertou = False
# palpites = 0

# while not acertou:
#    jogador = int(input('Qual é seu palpite? '))
#    palpites += 1

#    if jogador == computador:
#       acertou = True

#    else:
#       if jogador < computador:
#          print('Mais... Tente mais uma vez.')

#       elif jogador > computador:
#          print('Menos... Tente mais uma vez.')


# print(f'Acertou com {palpites} tentativas. Parabéns!')


#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
- Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
   [ 1 ] somar
   [ 2 ] multiplicar
   [ 3 ] maior
   [ 4 ] novos números
   [ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

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
#    [ 5 ] Sair de programa
#    ''')

#    opcao = int(input('>>>>> Qual é a sua opção? '))

#    if opcao == 1:
#       soma = n1 + n2
#       print(f'{n1} + {n2} = {soma}')
   
#    elif opcao == 2:
#       multiplicar = n1 * n2
#       print(f'{n1} x {n2} = {multiplicar}')
   
#    elif opcao == 3:
#       if n1 > n2:
#          maior = n1
#       else:
#          maior = n2
#       print(f'Entre {n1} e {n2}, o maior valor é {maior}.')
   
#    elif opcao == 4:
#       print('Informe os números novamente:')
#       n1 = int(input('Primeiro valor: '))
#       n2 = int(input('Segundo valor: '))
   
#    elif opcao == 5:
#       print('Finalizando...')
   
#    else:
#       print('Opção inválida. Tente novamente')
   
#    print('=-=' * 20)
#    time.sleep(2)

# print('Fim do programa! Volte sempre!')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
      5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# num = int(input('Digite um número para calcular seu Fatoria: '))

# c = num
# fat = 1

# print(f'Calculando {num}! -> ', end='')

# while c > 0:
#    print(f'{c}', end='')
#    print(' x ' if c > 1 else ' = ', end='')

#    fat *= c
#    c -= 1

# print(f'{fat}')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

# print('Gerador de P.A')
# print('-=' * 10)

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da P.A: '))

# termo = primeiro

# cont = 1

# while cont <= 10:
#    print(f'{termo} -> ', end='')
#    termo += razao
#    cont += 1

# print('FIM...')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 38) Escreva um programa que mostre na tela a seguinte contagem:
      - 6 7 8 9 10 11 Acabou!
'''

# cont = 1

# while cont <= 11:
#    print(f'{cont}', end=' -> ')
#    cont += 1

# print('FIM...')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 39) Faça um algoritmo que mostre na tela a seguinte contagem:
      - 10 9 8 7 6 5 4 3 Acabou!
'''

# cont = 10

# while cont >= 0:
#    print(f'{cont}', end=' -> ')
#    cont -= 1

# print('FIM...')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 41) Desenvolva um programa que mostre na tela a seguinte contagem:
      - 100 95 90 85 80 ... 0 Acabou!
'''

# cont = int(input('Contador: '))
# passo = int(input('Digite um número de passos: '))

# while cont >= 0:
#    print(f'{cont}', end=' -> ')
#    cont -= passo

# print('FIM...')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
      qualquer e mostre uma contagem até esse valor:
         - Ex: Digite um valor: 35
               Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
'''

# cont = 1
# fim = int(input('Digite um número final: '))

# while cont <= fim:
#    print(f'{cont}', end=' -> ')
#    cont += 1

# print('FIM...')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

# print('P.A')
# print('-=' * 30)

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da P.A: '))

# termo = primeiro
# cont = 1
# total = 0
# mais = 10

# while mais != 0:
#    total = total + mais

#    while cont <= total:
#       print(f'{termo} -> ', end='')
#       termo += razao
#       cont += 1
   
#    print('PAUSA.')
#    mais = int(input('Quantos termos você quer mostrar a mais? '))

# print(f'Progresso total com termos: {total}')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 43) Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1, marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
      - 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...
'''

# cont = 90

# while cont >= 0:
#    if cont % 9 == 0:
#       print(f'[{cont}]', end=' ')
#    else:
#       print(f'{cont}', end=' ')
#    cont -= 1

# print('FIM')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
      - Exemplo:
         - Digite o primeiro Valor: 3
         - Digite o último Valor: 10
         - Digite o incremento: 2
         - Contagem: 3 5 7 9 Acabou!
'''

# iniCont = int(input('DIgite o primeiro valor: '))
# finalCont = int(input('Digite o último valor: '))
# incrCont = int(input('DIgite o incremento: '))

# while iniCont <= finalCont:
#    print(f'{iniCont}', end=' -> ')
#    iniCont += incrCont

# print('FIM...')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 45) O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.
'''

# iniCont = int(input('DIgite o primeiro valor: '))
# finalCont = int(input('Digite o último valor: '))
# incrCont = int(input('DIgite o incremento: '))

# # Evita loop infinito
# if incrCont == 0:
#    incrCont = 1

# # Ajusta o sinal do incremento se necessário
# if iniCont > finalCont:
#    incrCont = -abs(incrCont) # '-abs()' -> garante que seja negativo

# else:
#    incrCont = abs(incrCont) # 'abs()' -> garante que seja positivo


# print('Contagem: ', end=' ')

# # Loop único, funciona para crescente ou decrescente
# num = iniCont

# while (incrCont > 0 and num <= finalCont) or (incrCont < 0 and num >= finalCont):
#    print(f'{num}', end=' -> ')
#    num += incrCont

# print('FIM...')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 46) Crie um programa que calcule e mostre na tela o resultado da soma entre:
      - 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.'''


# cont = 6
# soma = 0

# while cont <= 20:
#    print(f'{cont}', end=' + ')
#    soma += cont
#    cont += 2

# print(f'\nResultado: {soma}')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 47) Desenvolva um aplicativo que mostre na tela o resultado da expressão: 
      - 500 + 450 + 400 + 350 + 300 + ... + 50 + 0

'''

# cont = 500
# soma = 0

# while cont >= 0:
#    print(f'{cont}', end=' + ')
#    soma -= cont
#    cont -= 50


# print(f'Resultado: {soma}')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 48) Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
'''

# cont = 1
# soma = 0

# while cont <= 7:
#    num = int(input(f'Digite um número {cont}º: '))
#    soma += num
#    cont += 1

# print(f'Resultado: {soma}')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - 49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
'''

# cont = 1
# pares = 0
# impares = 0

# while cont <= 6:
#    num = int(input(f'Digite um número {cont}°: '))
   
#    if num % 2 == 0:
#       pares += 1
#    else:
#       impares += 1

#    cont += 1


# print(f'\nTotal de números pares: {pares}')
# print(f'Total de números impares: {impares}')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
      - Exemplo:
         - 0 – 1 – 1 – 2 – 3 – 5 – 8
'''

# print('\n', '-=' * 50)
# print('- Sequência de Fibonacci -')
# print('-=' * 50)

# n = int(input('Quantos termos você quer?: '))

# t1 = 0
# t2 = 1

# print('~' * 100)
# print(f'{t1} -> {t2}', end='')

# cont = 3

# while cont <= n:
#    t3 = t1 + t2
#    print(f' -> {t3}', end='')
#    t1 = t2
#    t2 = t3
#    cont += 1


# print('-> FIM...')
# print('~' * 100)



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

# num = cont = soma = 0
# num = int(input('Digite um número [999 para parar]: '))

# while num != 999:
#    soma += num
#    cont += 1
#    num = int(input('Digite um número [999 para parar]: '))

# print(f'Você digitou {cont} números a soma entre eles foi {soma}.')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercícios:
'''
   - Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

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

# print(f'Você digitou {quant} números, a soma de todos números foi {soma}, e a média foi {media}.')
# print(f'O maior valor foi {maior},  e o menor valor for {menor}.')



# #------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
   - Laços de Repetição Parte 03: Interrompendo repetições de While
'''
# num = 0
# soma = 0
# while True:
#    num = int(input('Digite um número: '))
#    if num == 999:
#       break
#    soma += num

# print(f'Resultado: {soma}')


# #------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

# soma = 0
# cont = 0

# while True:
#    valor = int(input('Digite um valor (999 para parar): '))
   
#    if valor == 999:
#       break

#    cont += 1
#    soma += valor

# print(f'Quantos valores digitados: {cont}\nSoma de todos os valores digitados: {soma}')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

# print('-=' * 30)
# print('                    - TABUADA -')
# print('-=' * 30)

# r = 's'

# while r == 's' or r == 'S':

#    num = int(input('Número de tabuada: '))
   
#    if num < 0:
#       break
   
#    else:
#       for c in range(1, 11):
#          resultado = num * c
#          print(f'{num} X {c} = {resultado}')
      

#    r = str(input('Quer continuar? [S/N]: '))


# print('- PROGRAMA TABUADA ENCERRADO -\nVolte sempre!')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

# import random

# v = 0

# while True:
#    jogador = int(input('Digite um número: '))
#    computador = random.randint(0, 10) # Computador escolhe vários números, porém tem limite de 0 até 10!

#    total = jogador + computador

#    tipo = ' '

#    while tipo not in 'PpIi':
#       tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
   
#    print(f'Jogador (Você): {jogador}  |  Computador: {computador}') # Número você escolhe, o computador támbem escolhe!
#    print(f'Total: {total} -> DEU PAR' if total % 2 == 0 else f'Total: {total} -> DEU IMPAR') # Mostrar um número total de Par ou Impar.

#    if tipo == 'P': # Par
#       if total % 2 == 0:
#          print('Você venceu!!')
#          v += 1
#       else:
#          print('Você perdeu!!')
#          break
   
#    elif tipo == 'I': # Impar
#       if total % 2 == 1:
#          print('Você venceu!!')
#          v += 2
#       else:
#          print('Você perdeu!!')
#          break
   
#    print('Vamos jogar novamente...')


# print(f'GAME OVER!\n- Você venceu {v}x')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
- Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
   - A) quantas pessoas tem mais de 18 anos.
   - B) quantos homens foram cadastrados.
   - C) quantas mulheres tem menos de 20 anos.
'''

# total18 = 0
# totalMasc = 0
# feminMenor20 = 0

# while True:
#    idade = int(input('Idade: '))
   
#    genero = ' '
#    while genero not in 'MF':
#       genero = str(input('Genero [M/F]: ')).strip().upper()[0]
   
#    if idade >= 18:
#       total18 += 1
   
#    if genero == 'M':
#       totalMasc += 1
   
#    if genero == 'F' and idade < 20:
#       feminMenor20 += 1

#    resp = ' '
#    while resp not in 'SN':
#       resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

#    if resp == 'N':
#       break


# print(f'Total de pessoas com mais de 18 anos: {total18}')
# print(f'Quantos homens foram cadastrados: {totalMasc}')
# print(f'Quantas mulheres tem menos de 20 anos: {feminMenor20}')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
- Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
   A) qual é o total gasto na compra.
   B) quantos produtos custam mais de R$1000.
   C) qual é o nome do produto mais barato.
'''

# print('{:-^50}'.format(' PRODUTO '))
# print('')

# total = 0
# totalMil = 0
# menor = 0
# cont = 0
# barato = ' '

# while True:
#    produto = str(input('- Nome do produto: '))
#    preco = float(input('- Preço: R$'))

#    total += preco

#    if preco > 1000:
#       totalMil += 1
   
#    if cont == 1 or preco < menor:
#       menor = preco
#       barato = produto

#    resp = ' '
#    while resp not in 'SN':
#       resp = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
#       print('')
   
#    if resp == 'N':
#       break


# print('{:-^50}'.format('FIM DA PROGRAMA'))
# print(f'O total da compra foi R${total:.2f}')
# print(f'Temos {totalMil} produtos custando mais de R$1000.00')
# print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
- Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
   - considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

# print('=' * 50)
# print('{:^50}'.format('BANCO CEV'))
# print('=' * 50)

# valor = int(input('Qual valor você quer sacar? R$'))
# total = valor

# ced = 50
# totCed = 0

# while True:
#    if total >= ced:
#       total -= ced
#       totCed += 1
   
#    else:
#       if total > 0:
#          print(f'Total de {totCed} cédulas de R${ced}')

#       if ced == 50:
#          ced = 20
      
#       elif ced == 20:
#          ced = 10
      
#       elif ced == 10:
#          ced = 1
      
#       totCed = 0

#       if total == 0:
#          break

# print('=' * 50)
# print('Volte sempre ao BANCO CEV! Tenha uma boa semana!')

