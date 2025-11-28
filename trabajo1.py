#************* zona de funcion **********

def tomar_numero():
    dar_numero = int(input("digite un numero: "))
    return dar_numero
def validar_numero(dato_numero):

    if dato_numero > 0:
        mensaje = "POSITIVO"
    elif dato_numero == 0:
        mensaje = "nagativo"
    else:
        mensaje = "negaivo"
    return mensaje

def hacer_mensaje(dato_mensaje):
    print ( "El numero es: " + dato_mensaje)



 #***************+zona codigo*****************

    dato_numero = tomar_numero()
    dato_mensaje = validar_numero(dato_numero)
    hacer_mensaje(dato_mensaje)
