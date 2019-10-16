
numero = input("Entre o numero para verificar: ")
numero = int(numero)
if numero > 1:
    for i in range(2, numero//2):
        if numero % i == 0:
            print("{} nao e primo".format(numero))
            break
    else:
        print("{} e primo".format(numero))
else:
    print("Nao e primo")
