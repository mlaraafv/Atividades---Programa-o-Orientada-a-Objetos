def decimal(b):
    print('in dec', b,  end=" ")


def octal(b):
    print('in oct=', oct(b), end=" ")


def hexadecimal(b):
    print('in hex=', hex(b), end=" ")


def binario(b):
    print('in bin=', bin(b), end=" ")


def tabela():
    a = 0
    while a < 226:
        decimal(a), octal(a), hexadecimal(a), binario(a)
        print("\n")
        print("------------------------------------------------------- ")
        a += 1


tabela()
