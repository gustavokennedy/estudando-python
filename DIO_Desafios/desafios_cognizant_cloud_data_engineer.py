## Desafios Iniciais
# Desafio 1
# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
#
# Entrada
# O arquivo de entrada contém 2 valores com uma casa decimal cada um.
#
# Saída
# Calcule e imprima a variável MEDIA conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

a = float(input())
b = float(input())

#TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
media = ( a * 3.5 + b * 7.5) / 11

#TODO: Complete com a variável que representa o resultado da média.
print(f'MEDIA = { media : .5f}')

###########################################################################################
# Desafio 2
# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo (soma de todos os lados) e apresente a mensagem:
#
# Perimetro = XX.X
#
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:
#
# Area = XX.X
#
# Fórmula da área de um trapézio: AREA = ((A + B) x C) / 2
#
# Entrada
# A entrada contém três valores reais.
#
# Saída
# O resultado deve ser apresentado com uma casa decimal.
lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

if a + b > c and a + c > b and b + c > a:
    #TODO Preencha a formula do perímeto do triangulo (soma de todos os lados).
    print(f"Perimetro = { a + b + c   :.1f}")
else:
    #TODO Preencha a formula da área do trapézio: AREA = ((A + B) x C) / 2
    print(f"Area = {((a + b) * c) / 2 :.1f}")

###########################################################################################
# Desafio 3
# Desafio
# Você terá o desafio de ler um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma loja, e informe-o expresso no formato horas:minutos:segundos.
#
# Entrada
# O arquivo de entrada contém um valor inteiro N.
#
# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
segundos = int(input())

minutos = int(segundos / 60) #TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = int(minutos / 60) #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))

###########################################################################################
# Desafio 4
# Desafio
# Crie um programa que leia 6 valores, os quais poderão ser negativos e/ou positivos. Em seguida, apresente a quantidade de valores positivos digitados.
#
# Entrada
# Você receberá seis valores, negativos e/ou positivos.
#
# Saída
# Exiba uma mensagem dizendo quantos valores positivos foram lidos. assim como é exibido abaixo no exemplo de saída. Não se esqueça de incluir na mensagem de saída o sufixo " valores positivos",

counter = 0
for number in range(6):
    number = float(input())
    if number > 0:
      counter = counter + 1
print('{} valores positivos'.format(counter))

###########################################################################################
# Desafio 5
# Desafio
# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Para cada X e Y, escreva uma mensagem para indicar se tais valores foram digitados em ordem crescente ou decrescente.
#
# Entrada
# A entrada é composta por vários casos de teste. Cada caso contém dois valores inteiros: X e Y. A leitura deve ser encerrada caso sejam fornecidos os mesmos valores para X e Y.
#
# Saída
# Caso os valores tenham sido digitados na ordem crescente, imprima “Crescente”. No contrário, “Decrescente”.

X, Y = map(int, input().split())
while (X != Y):
    floor = min(X, Y)
    top = max(X, Y)
    if ( X < Y):
        print("Crescente")
    elif (X>Y):
        print("Decrescente")
    X, Y = map(int, input().split())

###########################################################################################
# Desafio 6
# Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.
#
# Entrada
# O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.
#
# Saída
# Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

x = int(input())
y = int(input())

if x > y:
    a = y
    b = x

if x <= y:
    a = x
    b = y
a = a + 1
while a < b:
    if a % 5 == 2 or a % 5 == 3:
        print(a)
    a = a + 1

###########################################################################################
# Desafio 7
# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.
#
# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.
#
# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

n = int(input())
for i in range(n):
    num = int(input())
    sum = 0

    for j in range(1, (num + 1)):
        if num % j == 0:
            sum += 1

    if sum != (2):
        print('{} nao eh primo'.format(num))

    else:
        print('{} eh primo'.format(num))

###########################################################################################
# Desafio 8
# Desafio
# Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.
#
# Entrada
# A entrada contém um valor inteiro (V<=50).
#
# Saída
# Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.
X = list()
for i in range(10):
    if i == 0:
        value = int(input())
        aux = value
        X.insert(i,value)
    else:
        aux = aux * 2
        X.insert(i,aux)

for i in range(10):
    print('N[{0}] = {1}'.format(i,X[i]))

###########################################################################################
# Desafio 9
# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
#
# Entrada
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.
#
# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.
test_cases = int(input())

for i in range(test_cases):
    line = input()
    number_a = line.split()[0]
    number_b = line.split()[1]
    if (number_b != number_a[len(number_a)-len(number_b):] or len(number_b)>len(number_a)):
        print('nao encaixa')
        continue
    print('encaixa')