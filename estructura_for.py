# 1. Mostrar los números ascendentes desde el 1 al 10

for i in range(1, 11):
    print(i)

# # 2. Mostrar los números descendentes desde el 10 al 1

for i in range(10, 0, -1):
    print(i)

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número
# ingresado.

numero = int(input("Ingrese un numero: "))

for i in range(0, numero +1):
    print(i)

# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
# ejemplo si se ingresa el numero 5:
# 5 x 0 = 0
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 …

num = int(input("ingrese un numero: "))

for i in range(11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
# número 0. Mostrar la suma y el promedio de todos los números

acumulador_numeros = 0

for i in range(1, 11):
    numerazo = int(input("Ingrese un numero: "))
    print(numerazo)
    
    acumulador_numeros = acumulador_numeros + numerazo

    if numerazo == 0:
        if i == 1:
            print("No se ingresaron numeros para calcular")
        else:
            promedio = acumulador_numeros / (i-1)
            print(f"Promedio: {promedio}")
            print(f"Suma de los numeros: {acumulador_numeros}")
        break   
    if i == 10:
        promedio = (acumulador_numeros / i)
        print(f"Promedio: {promedio}")
        print(f"Suma de los numeros: {acumulador_numeros}")


# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

for i in range(1, 11):
    if i % 3 == 0:
        print(i)

# 7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)

for i in range(2, 51, 2):
    print(i)

# Realizar un programa que permita mostrar una pirámide de números. 
# Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
# 1
# 12
# 123
# 1234
# 12345

numeron = int(input("Ingrese un numero: "))

numero_2 = ""

for i in range(1, numeron + 1):
    numero_2 = ""
    for j in range(1, i + 1):
        numero_2 += str(j)


    print (numero_2)

# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
# el número ingresado. Mostrar la cantidad de divisores encontrados.

# 10.Ingresar un número. Determinar si el número es primo o no.

num_2 = int(input("Ingrese un numero: "))

cont_divisores = 0

for i in range(1, num_2 +1):
     if num_2 % i == 0:
         print(i)
         cont_divisores += 1


if cont_divisores == 2:
    print("El numero es primo")
else:
    print("El numero no es primo")

print(f"Cantidad divisores: {cont_divisores}")

# 11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
# número ingresado. Informar cuántos números primos se encontraron.

numerin = int(input("Ingrese un numero: "))

cont_primos = 0

for i in range(2, numerin +1):
     
    cont_divisores = 0

    for j in range(1, i +1):

        if i % j == 0:
            cont_divisores += 1


    if cont_divisores == 2:
        print(i)
        cont_primos += 1

print(f"Cantidad de numeros primos: {cont_primos}")











