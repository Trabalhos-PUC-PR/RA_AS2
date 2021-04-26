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
a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))
c = int(input("Digite o valor c: "))

aABS = abs(b - c)
bABS = abs(a - c)
cABS = abs(a - b)

def regra(abs, prim, seg, terc):
    if(abs < prim and prim < (seg + terc)):
        print(prim,"é um número válido! ")
    else:
        print(prim,"não é um número válido! ")
        
regra(aABS, a, b, c)
regra(bABS, b, a, c)
regra(cABS, c, a, b)
exit()