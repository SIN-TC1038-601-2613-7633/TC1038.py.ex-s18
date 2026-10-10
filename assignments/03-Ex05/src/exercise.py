"""
Los padres de un niño le regalarán $10 cuando cumpla n años, y 
cada cumpleaños doblarán la cantidad que le darán hasta que el obsequio exceda $1000.

Escribe un programa que lea el valor n, es decir, la edad en la que iniciará el regalo de $10 
y muestre como salida la edad que tendrá el niño cuando reciba el último obsequio 
y la cantidad de dinero que recibirá en ese año.

"""

def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    regalo = 10

    while regalo <= 1000:
        n += 1
        regalo *= 2

    print(n, regalo)

if __name__=='__main__':
    main()
