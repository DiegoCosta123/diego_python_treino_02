'''for c in range(1, 11):
   print(c)

print('FIM...')
'''


'''
r = 'S'
while r == 'S':
   n = int(input('Digite um valor: '))
   r = str(input('Quer continuar? [ S / N ]: '))

print('FIM...')
'''


'''
num = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
   resultado = num * c
   print(f'{num} X {c} = {resultado}')

print('FIM...')

'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
- Tabuda:

r = 's'
while r == 's' or r == 'S':

   num = int(input('Número de tabuada: '))   
   
   for c in range(1, 11):
      resultado = num * c
      print(f'{num} X {c} = {resultado}')
   
   r = str(input('Quer continuar? [S/N]: '))


print('FIM...')
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# n = 1

# par = impar = 0

# while n != 0:
#    n = int(input('Digite um número: '))

#    if n != 0:
#       if n % 2 == 0:
#          par += 1
#       else:
#          impar += 1


# print(f'Você digitou {par} números de Par e {impar} números de Impar.')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# n = 0
# while True:
#    n = int(input('Digite um número: '))
#    if n == 999:
#       break
   
#    n += 1


# print('FIM!')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# n = str(input('Seu nome: '))
# id = int(input('Sua idade: '))

# print('-=' * 20)
# print('- DOCUMENTO -')
# print('-=' * 20)

# print('Nome: %nome' %(n))
# print('Idade: %idade' %(id))

# print('-=' * 20)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


# num = int(input('Escolhe um número: '))

# for c in range(1, 11):
#    mult = num * c
#    print(f'{num} X {c} = {mult}')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Teste Tabuada com While:

# resp = 'S'

# while resp == 'S':
#    tabuada = int(input('Escolhe um número: '))

#    for c in range(1, 11):
#       resultado = tabuada * c
#       print(f'{tabuada} x {c} = {resultado}')
   
#    resp = str(input('Quer continuar? [S/N]: ')).upper()

# print('Fim da Tabuada! Volte sempre!')

