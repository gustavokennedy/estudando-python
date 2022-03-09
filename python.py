# -*- coding: utf-8 -*-

# a = int(input('Entre com valor A: '))
# b = int(input('Entre com valor B: '))
# soma = a + b
# subtracao = a - b
# print('Soma: {}. \nSubtração: {} '.format(soma, subtracao))

# if a > b:
#   print('')


# # Média Notas
# a = int(input('Primeiro bim:'))
# if a > 10:
#    a = int(input('Você digitou errado. Informe de 0 a 10 novamente: '))
# b = int(input('Segundo bim:'))
# if b > 10:
#    b = int(input('Você digitou errado. Informe de 0 a 10 novamente: '))
# c = int(input('Terceiro bim:'))
# if c > 10:
#    c = int(input('Você digitou errado. Informe de 0 a 10 novamente: '))
# d = int(input('Quarto bim:'))
# if d > 10:
#    d = int(input('Você digitou errado. Informe de 0 a 10 novamente: '))
# media = (a + b + c + d) / 4
# print('Média: {}'.format(media))

#Laços de Repetição

# # Número Primo
# a = int(input('informe o numero: '))

# div = 0
# for x in range(1, a+1):
#   resto = a % x
#   print(x, resto)
#   if resto == 0:
#       div = div + 1

# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

# for num in range(101):
#   div = 0
#   for x in range(1, num+1):
#     resto = num % x
#     print(x, resto)
#     if resto == 0:
#       div += 1
#     if div == 2:
#       print(num)

# a = 0
# while a < 10:
#   print(a)
#   a += 1

# Segurança da Informação com Python - DIO

# PING
import os ## Importa o módulo OS

print("#" * 60) ## Mostra # para identação

ip_ou_host = input("Digite o IP ou Host: ") ## Cria variável para receber IP ou Host
print("-" * 60) ## Mostra # para identação
os.system('ping -n 6 {}'.format(ip_ou_host)) ## Chamamos system do módulo OS para fazer o PING
print("-" * 60) ## Mostra # para identação