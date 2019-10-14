#Comentario uma linha
if True:
    print("Nao e falso")
else:
    print("E falso")
   
'''
Comentario grande
i = 0 e a atribuicao do valor
0 para a variavel i
'''
i = 0
while i < 10:
    print("I:{}".format(i))
    i += 1

# Multiplas atribuicoes na mesma linha
numero1,numero2,numero3 = 2.0, 3, 34
print(numero1)

# continuacao da linha
acc = numero1 + numero2 + \
        numero3

print(acc)

# remover referencia a numero
print(i)
del i
print(i)
