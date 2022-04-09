"""3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:"""

"""Paso 1: Hacer na variable"""
def numeroPar(num):
    num = range(1, 102)
    if num >= 2:
        return num % 2
    print(num)
print(numeroPar)