'''
AS-2
Sabendo-se que só irá existir um triângulo se, somente se, os seus lados obedeceram à
seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da
diferença dos outros dois lados e menor que a soma dos outros dois lados. Veja o resumo
da regra abaixo:

  Módulo
\/      \/

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

Desenvolva um algoritmo e uma app em Python que leia três valores numéricos reais
fornecidos pelo usuário e imprima se podem ser lados de um triângulo.
OBS: Para a app em Python, o módulo pode ser calculado pela função ABS(). Pesquise
sobre ela e use na solução. Pode usar a mesma função ao algoritmo também

ABS() serve para pegar o valor absoluto (módulo) de um número, é basicamente isso
'''
'''
#VARIAVEIS
valor_a = 0
valor_b = 0
valor_c = 0
a_modulo = 0
b_modulo = 0
c_modulo = 0

# PROGRAMA
valor_a <- leia("digite o valor A")
valor_b <- leia("digite o valor B")
valor_c <- leia("digite o valor C")

a_modulo = modulo(b - c)
b_modulo = modulo(a - c)
c_modulo = modulo(a - b)

se(a_modulo < a e a < b + c e
   b_modulo < b e b < a + c e
   c_modulo < c e c < a + b):
    
    imprima "valores validos! "
senao:
    imprima "valores invalidos! "
fimse
exit()
'''
a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))
c = int(input("Digite o valor c: "))

aABS = abs(b - c)
bABS = abs(a - c)
cABS = abs(a - b)

if( (aABS < a and a < (b + c)) and 
    (bABS < b and b < (a + c)) and 
    (cABS < c and c < (a + b)) ):

    print("Valores Validos! ")
else:
    print("Valores Invalidos! ")
exit()
