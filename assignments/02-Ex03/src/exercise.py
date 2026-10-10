"""
Escribe un programa que sume los números enteros (positivos y negativos) que el usuario teclee 
y se detenga hasta que el usuario teclee un cero.
"""

def main():
    suma = 0
    numero = int(input())

    while numero != 0:
        suma += numero
        numero = int(input())
    
    print(suma)

if __name__=='__main__':
    main()
