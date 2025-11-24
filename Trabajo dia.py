# --------- Zona Funcion ---------------

def capturar_hora():
    hora = int (input("escriba la hora " ))
    if hora >= 0 and hora < 12:
        print(" Buenos Dias ")
    elif hora >= 12 and hora < 18:
        print(" Buenas Tardes ")
    elif hora >= 18 and hora < 24 :
        print (" Buenas Noches ")
    else:
        print (" Hora incorrecta ")

def capturar_nombre():
    nombre_usuario = input (" Escriba su nombre completo: ")
    return nombre_usuario

def tomar_rol():
    rol_usuario = input("Digite su Rol: ")
    return rol_usuario


def hacer_saludo(nombre_usuario , rol_usuario):
    mensaje = " Hola " + nombre_usuario + " Su rol es: " + rol_usuario
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)

#----------zona Codigo ---------------


hora = capturar_hora()
nombre_usuario = capturar_nombre()
rol_usuario = tomar_rol()
mensaje = hacer_saludo(nombre_usuario , rol_usuario) 
imprimir_mensaje(mensaje)