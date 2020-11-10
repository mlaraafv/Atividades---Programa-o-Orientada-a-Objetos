def printDecimal(b):
    print('\t', b,  end=" ")


def printOctal(b):
    print('\t', oct(b), end=" ")


def printHexadecimal(b):
    print('\t', hex(b), end=" ")


def printBinario(b):
    print('\t  ', bin(b), end=" ")


def imprimirTabela():
    print("Decimal Octal Hexadecimal Binario")
    print("------- ----- ----------- -------- ")
    a = 0
    while a < 256:
        printDecimal(a), printOctal(a), printHexadecimal(a), printBinario(a)
        print("\n")

        a += 1


imprimirTabela()
