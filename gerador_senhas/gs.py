import random
import string

tamanho = int(input('Digite o tamanho da senha (int): '))

chars = string.ascii_letters + string.digits + '!@#$%¨&*'
# chars = string.ascii_lowercase + string.digits + '!@#$%¨&*' para letras minusculas

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))