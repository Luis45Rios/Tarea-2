"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones 
en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta."""
n1=float(input("introduce un numero:"))
n2=float(input("introduce otro numero:"))
 
print("que quieres simar?")
print("[1]sumar dos numero:")
print("[2]restar dos numeros:")
print("[3]multiplicar dos numeros:")
 
opcion=input("introduce una opcion")
if opcion=="1":
    print("la suma de",n1,"+",n2,"es",n1+n2)
elif opcion=="2":
    print("la resta de",n1,"-",n2,"es",n1-n2)
elif opcion=="3":
    print("la multiplicacion de",n1,"*",n2,"es",n1*n2)
else:
    print("esta opcion no existe")