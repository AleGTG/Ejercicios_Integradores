# Consigna
# Una cadena de supermercados desea desarrollar un sistema para registrar la venta diaria
# de productos en distintas sucursales. Se sabe que se realizarán 25 ventas.
# Por cada venta se deben ingresar los siguientes datos:
# ● Tipo de producto (alimento, limpieza, perfumería)
# ● Cantidad de unidades vendidas (entre 1 y 20)
# ● Precio unitario (mayor a 0)
# ● Forma de pago (efectivo, tarjeta, transferencia)
# Se debe validar cada dato ingresado.
# Consideraciones:
# ● Si la cantidad total de unidades vendidas supera las 200, se aplica un descuento
# del 10% sobre el total bruto.
# ● Si supera las 400 unidades, el descuento será del 20%.
# ● Las ventas pagadas en efectivo tienen un 5% de descuento adicional sobre el
# subtotal de esa venta.
# Se pide:
# 1- Calcular el importe total bruto sin descuentos.
# 2- Calcular el importe total final con todos los descuentos aplicados.
# 3- Informar la venta más cara hecha con tarjeta.
# 4- Calcular el promedio de precio unitario de todas las ventas.
# 5- Informar cuál fue la forma de pago más utilizada.

#NOTA aqui hay funciones por estuve practicando un poco de todo

def generar_menu_opciones (op1, op2, op3):
    return f'''
    1-● {op1}
    2-● {op2}
    3-● {op3}
    '''

def validar_ingreso_rango(min, max, mensaje)->int:
    opciones = int(input(mensaje + f"({min}-{max})"))
    while opciones < min or opciones > max:
        opciones = int(input(f"ERROR!!!: {mensaje}"))
    return opciones

def validar_si_o_no (mensaje:str)->str:
    '''
    docu
    '''
    mensaje = str(input(mensaje))
    while mensaje != "si" and mensaje != "no":
        mensaje = str(input(f"Dato invalido!! {mensaje}"))
    return mensaje

def validar_numero_mayor (numero:int, mensaje:str):
    precio = int(input(f"{mensaje}: "))
    while precio <= numero:
        precio = int(input(f"Error!!! {mensaje}: "))
    return precio

def verificar_string (dato:str, string:str, num_1:float, num_2:float)->float:
    if string == dato:
        return num_1
    else:
        return num_2


def calcular_rango_descuentos (numero_1:int, numero_2:int, descuento:int, descuento_max:int, descuento_min:int, min:int, max:int)->float:
    if numero_1 > max:
        descuento = numero_2 * descuento_max
        return descuento
    elif numero_1 > min:
        descuento = numero_2 * descuento_min
        return descuento
    else:
        return descuento

def multiplicar_numeros (numero_1:int, numero_2:int):
    resultado = numero_1 * numero_2
    return resultado
    


def ejecutar_menu():

    total_bruto = 0
    total_final = 0

    total_unidades = 0

    acumulador_precios = 0

    contador_efectivo = 0
    contador_tarjeta = 0
    contador_transferencia = 0

    venta_mas_cara_tarjeta = 0

    contador_ventas = 0

    ingreso_ventas = validar_si_o_no("Desea ingresar una venta? (si/no): ")

    cantidad_ventas = validar_ingreso_rango(1, 25, "Ingrese la cantidad de ventas")

    while ingreso_ventas == "si":

        precio = validar_numero_mayor(0, "Ingrese el precio")

        cantidad_unidades = validar_ingreso_rango(1, 20, "Ingrese la cantidad de unidades: ")


        print(generar_menu_opciones("Tipo de producto ALIMENTO",
                                    "Tipo de producto LIMPIEZA",
                                    "Tipo de Producto PERFUMERIA"))
        
        validar_ingreso_rango(1, 3, "INGRESE UN TIPO DE PRODUCTO: ")

        print(generar_menu_opciones("Metodo de pago EFECTIVO",
                                    "Metodo de pago TARJETA",
                                    "Metodo de pago TRANSFERENCIA"))
        
        opc_tipo_pago = validar_ingreso_rango(1, 3, "Ingrese el metodo de pago: ")

        subtotal = multiplicar_numeros(cantidad_unidades, precio)

        total_bruto += subtotal

        total_unidades += cantidad_unidades

        acumulador_precios += precio

        if opc_tipo_pago == 1:
            opc_tipo_pago = "EFECTIVO"
            tipo_pago = verificar_string("EFECTIVO", opc_tipo_pago, 0.05, 0.0,)
            descuento_efectivo = multiplicar_numeros(subtotal, tipo_pago)
            subtotal -= descuento_efectivo
            contador_efectivo += 1

        elif opc_tipo_pago == 2:
            opc_tipo_pago = "TARJETA"
            contador_tarjeta += 1

            if subtotal > venta_mas_cara_tarjeta:
                venta_mas_cara_tarjeta = subtotal
        else:
            opc_tipo_pago = "TRANSFERENCIA"
            contador_transferencia += 1

        total_final += subtotal

        contador_ventas += 1
        ingreso_ventas = validar_si_o_no("Desea continuar ejecutando el programa? (si/no): ")

        if ingreso_ventas == "no":
            print("Programa terminado!!!")
           

        if contador_ventas == cantidad_ventas:
            print("Programa terminado!!!")
            ingreso_ventas = "no"

    descuento_general = calcular_rango_descuentos(total_unidades, total_bruto, 0, 0.20, 0.10, 200, 400)

    total_final -= descuento_general

    promedio = acumulador_precios / contador_ventas

    if contador_efectivo > contador_tarjeta and contador_efectivo > contador_transferencia:
        forma_mas_usada = "EFECTIVO"
    elif contador_tarjeta > contador_transferencia:
        forma_mas_usada = "TARJETA"
    else:
        forma_mas_usada = "TRANSFERENCIA"

    print("\n//////////// RESULTADOS ////////////")

    print(f"Total bruto: {total_bruto}")

    print(f"Total final: {total_final}")

    print(f"Venta más cara con tarjeta: {venta_mas_cara_tarjeta}")

    print(f"Promedio precios unitarios: {promedio}")

    print(f"Forma de pago más usada: {forma_mas_usada}")

ejecutar_menu()


        
        



        