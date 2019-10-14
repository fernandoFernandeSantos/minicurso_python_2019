
a = 21
b = 10
c = 0

if ( a == b ):
   print("Linha 1 - a e igual a b")
else:
   print("Linha 1 - a nao e igual a b")

if ( a != b ):
   print("Linha 2 - a nao e igual a b")
else:
   print("Linha 2 - a e igual a b")

if ( a <> b ):
   print("Linha 3 - a nao e igual a b")
else:
   print("Linha 3 - a e igual a b")

if ( a < b ):
   print("Linha 4 - a e menor que b") 
else:
   print("Linha 4 - a nao e menor que b")

if ( a > b ):
   print("Linha 5 - a e maior que b")
else:
   print("Linha 5 - a nao e maior que b")

a = 5
b = 20
if ( a <= b ):
   print("Linha 6 - a e menor ou igual a b")
else:
   print("Linha 6 - a maior que b")

if ( b >= a ):
   print("Linha 7 - b maior ou igual a b")
else:
   print("Linha 7 - b menor que b")
   
# and, or e not
falso = False
verdadeiro = True

print("Linha 8 - falso or verdadeiro {}".format(falso or verdadeiro))
print("Linha 9 - falso and verdadeiro {}".format(falso and verdadeiro))
print("Linha 10 - falso or not verdadeiro {}".format(falso or not verdadeiro)) 

