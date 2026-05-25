# Enunciado/s:
# Tabla de Posiciones de Torneo de Ping-Pong
# Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
# Los datos que se cargarán son:
# Nombre del jugador
# Edad (validar)
# Cantidad de puntos (validar-número entero positivo, hasta 60).
# Número de partidos ganados (validar-número entero positivo, hasta 35).
# Tipo de saque ("plano", "liftado", "cortado")
# Categoría ("elite", "experto", "avanzado")
# Se necesita saber
# Tema A:
# 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
# inclusive.
# 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
# 3-Porcentaje de jugadores de categoría "experto".
# 4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
# 5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”

jugador_menor = ""
edad_menor = 0
cont_elite = 0
categoria_menor = ""
cont_edad_avanzada = 0
cont_plano = 0
cont_liftado = 0
cont_cortado = 0
cont_cargas = 0
cont_experto = 0
cont_avanzado = 0

bandera = True

while bandera == True:
    carga = str(input("Desea cargar un jugador? (si/no): "))
    while carga != "si" and carga != "no":
        carga = str(input("Dato invalido!! Desea cargar un jugador? (si/no): "))
        
    if carga == "si":

        nombre = input("Ingrese el nombre del juagador: ")

        edad = int(input("Ingrese su edad: "))
        while edad < 18 or edad > 100:
            edad = int(input("Valor invalido!! Ingrese su edad (18-100): "))

        puntos = int(input("Ingrese la cantidad de puntos (max 60): "))
        while puntos > 60 or puntos < 0:
            puntos = int(input("Error limite de puntos superado! Ingrese la cantidad de puntos (max 60): "))

        partidos = int(input("Ingrese la cantidad de partidos ganados (max 35): "))
        while partidos > 35 or partidos < 0:
                partidos = int(input("Valor invalido!!! Ingrese la cantidad de partidos ganados (max 35): "))

        tipo_saque = input("Ingres el tipo de saque (plano, liftado, cortado): ")
        while tipo_saque != "Plano" and tipo_saque != "Liftado" and tipo_saque != "Cortado":
            tipo_saque = input("Error!!! Ingres el tipo de saque (plano, liftado, cortado)")
        
        categoria = input("Ingrese la categoria (Elite, Experto, Avanzado): ")
        while categoria != "Elite" and categoria != "Experto" and categoria != "Avanzado":
            categoria = input("Error!! Ingrese la categoria (Elite, Experto, Avanzado): ")

        if categoria == "Elite":
            if tipo_saque == "Plano":
                if edad <= 19 or edad <= 25:
                    cont_elite += 1
                cont_plano += 1
            elif tipo_saque == "Liftado":
                cont_liftado += 1
            else:
                cont_cortado += 1

        if categoria == "Experto":
            cont_experto += 1

        if puntos > 50 and (jugador_menor == "" or edad < edad_menor):
            edad_menor = edad
            jugador_menor = nombre
            categoria_menor = categoria
    
        if categoria == "Avanzado":
            cont_edad_avanzada = cont_edad_avanzada + edad
            cont_avanzado += 1

        cont_cargas += 1

    else:
        print("Fin del la carga de jugadores!!!")
        bandera = False

if cont_plano > cont_liftado and cont_plano > cont_cortado:
    mayor_saque = "Plano"
elif cont_liftado > cont_cortado:
    mayor_saque = "Liftado"
else:
    mayor_saque = "Cortado"

if cont_cargas > 0:
    porcentaje_experto = (cont_experto / cont_cargas) * 100
    
else:
    porcentaje_experto = 0

if cont_avanzado == 0:
    print("No es posible hacer el promedio de edad avanzada")
    promedio_edad_avanzada = 0
else:
    promedio_edad_avanzada = (cont_edad_avanzada / cont_avanzado)

print(f"\n Cantidad de jugadores de la categoría elite con tipo de saque “plano”, cuya edad esté entre 19 y 25 años: {cont_elite} ")
print(f"\n El nombre del jugador con menor edad mas de 50 puntos es: {jugador_menor}, la cetegoria es: {categoria_menor} y su edad es: {edad_menor}")
print(f"\n El porcentaje de juagdores con la categoria Experto es: {porcentaje_experto} %")
print(f"\n El promedio de edad de la categoria Avanzado es: {promedio_edad_avanzada}")
print(f"\n El tipo de saque mas usado cuya categoria sea Elite es: {mayor_saque}")
        



    


