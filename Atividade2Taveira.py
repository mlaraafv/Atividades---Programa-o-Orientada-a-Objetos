def printDecimal(b):
    print('in dec', b,  end=" ")


def printOctal(b):
    print('in oct=', oct(b), end=" ")


def printHexadecimal(b):
    print('in hex=', hex(b), end=" ")


def printBinario(b):
    print('in bin=', bin(b), end=" ")


def imprimirTabela():
    a = 0
    while a < 256:
        printDecimal(a), printOctal(a), printHexadecimal(a), printBinario(a)
        print("\n")
        print("------------------------------------------------------- ")
        a += 1


imprimirTabela()
