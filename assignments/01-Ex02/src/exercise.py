"""
Programa que reciba un número entero y calcule la suma: 1^2 + 2^2 + 3^2 +...+"numero^2". 
Donde "numero" es el valor que el usuario proporcionó. 
Finalmente se imprime el resultado de la suma en pantalla.
"""

def main():
    numero = int(input())
    suma = 0

    for i in range(1, numero + 1):
        suma += i ** 2

    print(suma)

if __name__=='__main__':
    main()
