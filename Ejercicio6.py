"""6) Utilizando la función range() y la conversión a listas genera las siguientes listas 
dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto)."""

lista1 = list(range(11))
print(lista1)

lista2 = list(range(-10,1))
print(lista2)

lista3 = []
for n in range(1,21):
    if (n%2==0):
        lista3.append(n)
print(lista3)

lista4 = list(range(-21,0,2))
print(lista4)

lista5 = []
for n in range(5,51,5):
    print(n, end=", ")
print(lista5)