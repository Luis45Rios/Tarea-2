"""6) Realiza una función separar() que tome una lista de números enteros y devuelva dos 
listas ordenadas. La primera con los números pares, y la segunda con los números impares:"""
def separar(lista1):
    lista_pares=[]
    lista_impares=[]
    for i in lista1:
        if i%2==0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    lista_pares.sort()
    lista_impares.sort()
    print("Lista pares:",lista_pares,"\n","Lista impares:",lista_impares)

separar([-12, 84, 13, 20, -33, 101, 9])

