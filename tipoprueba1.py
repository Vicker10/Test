import os

datos = {"entradas" : []}
entradas_disponibles = 500

def validar_num_entero(mensaje:str):
    while True:
        try:
            num = int(input(mensaje))
            if num < 0:
                print("⚠️ DEBE INGRESAR UN NUMERO POSITIVO")
                continue
            return num
        except ValueError:
            print("❌ ERROR, DEBE INGRESAR UN NUMERO ENTERO POSITIVO")

def valida_texto_vacio(mensaje:str):
    while True:
        texto = input(mensaje)
        if len(texto) == 0:
            print("⚠️ EL TEXTO NO DEBE ESTAR VACÍO")
            continue
        return texto

def valida_tipo_entrada(mensaje:str) :
    while True:
        tipo = valida_texto_vacio(mensaje).upper()
        if tipo == "G" or tipo == "V":
            return tipo
        else:
            print("❌ debe ingresar GENERAL (G) o VIP (V)")
            continue

            
def Validar_CodigoNum(codigo_confirmacion:str):
    codigo = "1234567890"
    for i in codigo_confirmacion:
        for j in codigo:
            if i == j :
                return True
    return False

def Validar_CodigoLetra(codigo_confirmacion:str):
    codigo = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for i in codigo_confirmacion:
        for j in codigo:
            if i == j:
                return True
    return False

def validar_codigosEspacios(codigo_entrada:str):
    codigo = " "
    for i in codigo_entrada:
        for j in codigo:
            if i == j:
                return False
    return True

def valida_codigo_fortificados(mensaje:str):
    while True:
        codigo_entrada = valida_texto_vacio(mensaje)
        if Validar_CodigoLetra(codigo_entrada) == False:
            print("⚠️ DEBE CONTENER AL MENOS UNA MAYÚSCULA")
            continue
        elif Validar_CodigoNum(codigo_entrada) == False: 
            print("⚠️ DEBE CONTENER AL MENOS UN NÚMERO")
            continue
        elif validar_codigosEspacios(codigo_entrada) == False:
            print("⚠️ NO DEBE CONTENER ESPACIOS")
            continue
        if len(codigo_entrada) < 6 :
            print("DEBE CONTENER al menos 6 DIGITOS ALFANUMERICOS")
            continue
        break
    return codigo_entrada



def nombre_repetido(nombre:str):
    nombre2 = nombre.capitalize()
    for i in datos["entradas"]:
        if i["nombre"] == nombre2:
            return True
    return False


def comprar_entrada_fortificados():
    while True:
        nombre_comprador = valida_texto_vacio("INGRESE SU NOMBRE: ").capitalize()
        if nombre_repetido(nombre_comprador) == True:
            print("EL NOMBRE YA SE ENCUENTRA REGISTRADO, VUELVE A INTENTARLO")
            continue

        tipo_entrada = valida_tipo_entrada("INGRESE TIPO DE ENTRADA GENERAL O VIP (G o V): ")
        codigo_confirmacion = valida_codigo_fortificados("INGRESE SU CODIGO DE CONFIRMACIÓN: ")

        nuevo_usuario = {
            "nombre" : nombre_comprador,
            "tipo_entrada" : tipo_entrada,
            "codigo" : codigo_confirmacion
        }

        datos["entradas"].append(nuevo_usuario)
        print("COMPRA EXITOSA ✅")
        return datos
    
def tipo_entrada_iluminados(mensaje:str):
    while True:
        tipo = valida_texto_vacio(mensaje).upper()
        if tipo == "CV" or tipo == "PAL":
            return tipo
        else:
            print("❌ debe ingresar CANCHA VIP (CV) o PALCO (PAL)")
            continue

def Validar_CodigoLetra_iluminados(codigo_confirmacion:str):
    codigo = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    contador = 0
    for i in codigo_confirmacion:
        for j in codigo:
            if i == j:
                contador += 1
                if contador == 3:
                    return True
    return False

def valida_codigo_iluminados(mensaje:str):
    while True:
        codigo_entrada = valida_texto_vacio(mensaje)
        if Validar_CodigoLetra_iluminados(codigo_entrada) == False:
            print("⚠️ DEBE CONTENER AL MENOS 3 LETRAS MAYÚSCULAS")
            continue
        elif Validar_CodigoNum(codigo_entrada) == False: 
            print("⚠️ DEBE CONTENER AL MENOS UN NÚMERO")
            continue
        elif validar_codigosEspacios(codigo_entrada) == False:
            print("⚠️ NO DEBE CONTENER ESPACIOS")
            continue
        if len(codigo_entrada) < 5 :
            print("DEBE CONTENER al menos 5 DIGITOS ALFANUMERICOS")
            continue
        break
    return codigo_entrada

def comprar_entrada_iluminados():
    while True:
        nombre_comprador = valida_texto_vacio("INGRESE SU NOMBRE: ").capitalize()
        if nombre_repetido(nombre_comprador) == True:
            print("EL NOMBRE YA SE ENCUENTRA REGISTRADO, VUELVE A INTENTARLO")
            continue
        tipo_entrada = tipo_entrada_iluminados("INGRESE TIPO DE ENTRADA CANCHA VIP (CV) o PALCO (PAL): ")
        codigo_confirmacion = valida_codigo_iluminados("INGRESE SU CODIGO DE CONFIRMACIÓN: ")
        nuevo_usuario = {
            "nombre" : nombre_comprador,
            "tipo_entrada" : tipo_entrada,
            "codigo" : codigo_confirmacion
        }

        datos["entradas"].append(nuevo_usuario)
        print("COMPRA EXITOSA ✅")
        return datos
    

while True:
    os.system("cls")
    print("*** TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE ***")
    print("[1] - Comprar entrada a “los Fortificados”.")
    print("[2] - Comprar entrada a “los Iluminados”.")
    print("[3] - Stock de entradas para ambos conciertos.")
    print("[4] - Salir")

    opc = validar_num_entero("INGRESE UNA OPCION 1 - 4: ")

    if opc == 1 :
        comprar_entrada_fortificados()
        entradas_disponibles -= 1
        input("PRESIONE ENTER PARA VOLVER AL MENÚ")

    elif opc == 2 :
        comprar_entrada_iluminados()
        entradas_disponibles -= 1
        input("PRESIONE ENTER PARA VOLVER AL MENÚ")

    elif opc == 3 :
        print(f"EL STOCK DE ENTRADAS PARA AMBOS CONCIERTOS ES DE: {entradas_disponibles}")
        input("PRESIONE ENTER PARA VOLVER AL MENÚ")

    elif opc == 4 :
        print("Salir")
        break

    else: 
        print("❌ ERROR, DEBE INGRESAR UNA OPCION VALIDA DEL 1 AL 4")
        