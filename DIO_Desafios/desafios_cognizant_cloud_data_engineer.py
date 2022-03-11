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