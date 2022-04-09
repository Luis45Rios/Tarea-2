"""Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'"""
num1 =int(5)
num2 = int(10)

def relacion(num1,num2):
    if num1 > num2:
        print(1)
    if num1 < num2:
        print(-1)
    elif num1 == num2:
        print(0)
print(relacion)