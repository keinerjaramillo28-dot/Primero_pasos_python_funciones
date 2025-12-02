#****************zona funcion****************

def leer_datos():
    dolares = float(input("ingrese la cantidad de dolares"))
    tasa = float(input("ingrese el valor de la tasa de cambio"))
    return dolares, tasa
def dolares_a_euros(dolares, tasa):
    return dolares * tasa
def mostrar_resultado(euros):
    print("la cantidad equivalentes en euros es:" + str(euros))
    
    
#*****************zona codigo*********************

dolares, tasa = leer_datos()
resultado = dolares_a_euros(dolares, tasa)
mostrar_resultado(resultado)


