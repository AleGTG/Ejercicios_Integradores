# UTN Technologies, una reconocida software factory se encuentra en la búsqueda
# de ideas para su próximo desarrollo en Python, que promete revolucionar el
# mercado.
# Las posibles aplicaciones son las siguientes:
# ● Inteligencia artificial (IA),
# ● Realidad virtual/aumentada (RV/RA),
# ● Internet de las cosas (IOT)
# Para ello, la empresa realiza entre sus empleados una encuesta, con el
# propósito de conocer ciertas métricas.
# A) Los datos a ingresar por cada empleado encuestado son:
# ● nombre del empleado
# ● edad (no menor a 18)
# ● género (Masculino - Femenino - Otro)
# ● tecnologia (IA, RV/RA, IOT)
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# 1. Cantidad de empleados de género masculino que votaron por IOT o IA,
# cuya edad esté entre 25 y 50 años inclusive.
# 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
# género no sea Femenino o su edad se encuentre entre los 33 y 40.
# 3. Nombre y tecnología que votó, de los empleados de género masculino con
# mayor edad de ese género.


cont_empleados = 0
cont_masculino = 0
edad_mayor = 0
nombre_mayor = ""
tecnologia_mayor = ""
contador_blucle = 0

bandera = True

while bandera == True:
    encuesta = str(input("Desea ingresar una compra? (si/no): "))
    while encuesta != "si" and encuesta != "no":
        encuesta = str(input("Dato invalido!! Desea ingresar una encuesta? (si/no): "))
    if encuesta == "si":
        nombre = str(input("Ingrese su nombre: "))

        edad = int(input("Ingrese su edad: "))
        while edad < 18 or edad > 100:
            edad = int(input("vlor invalido!! Ingrese su edad (18-100): "))
        
        genero = str(input("Ingrese su genero: "))
        while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
            genero = str(input("Dato invalido!!! ingrese su genero (Masculino - Femenino - Otro): "))
        
        tecnologia = str(input("Ingrese Su tecnologia (IA, RV/RA, IOT): "))
        while tecnologia != "IA" and tecnologia!= "RV/RA" and tecnologia != "IOT":
            tecnologia = str(input("Dato invalido!!! Ingrese Su tecnologia (IA, RV/RA, IOT): "))

        if genero == "Masculino" and (tecnologia == "IA" or tecnologia == "IOT") and (edad <= 25 or edad <= 50):
            cont_masculino += 1

        if tecnologia != "IA" and (genero != "Femenino" or edad <= 33 or edad <= 40):
            cont_empleados += 1

        if genero == "Masculino" and edad > edad_mayor:
            edad_mayor = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia

        contador_blucle += 1

        if contador_blucle == 10:
            print("Fin del programa!!!")
            bandera = False
    else:
        print("Fin del programa!!!")
        bandera = False

empleados_no_ia = (cont_empleados / contador_blucle) * 100

print("\n/////////////////////////////////////////////////")

print(f"\n La cantidad de empleados Masculinos que votaron por IA o IOT son: {cont_masculino}")
print(f"\n Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40 {empleados_no_ia} %")
print(f"\n El empleado que con mayor edad que voto es: {nombre_mayor}, su edad es: {edad_mayor} y la tecnologia que voto es: {tecnologia_mayor}")


        

        



