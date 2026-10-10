"""
Programa que lea un valor n y que muestre en la pantalla n caracteres que alternan entre # y %.
Los caracteres se deben mostrar uno en cada renglón.
Observe que el primer caracter que se debe mostrar siempre es #
"""

def main():
    n = int(input("Ingrese un valor n: "))
    for i in range(n):
        if i % 2 == 0:
            print("#")
        else:
            print("%")

if __name__=='__main__':
    main()
