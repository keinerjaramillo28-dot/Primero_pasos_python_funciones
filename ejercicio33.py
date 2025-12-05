
#*******zona funcion******
def leer_datos():
    kilometros = float(input("digite la distancia en kilometros:"))
    return kilometros
def kilometros_a_millas(kilometros):
    millas = kilometros * 0.621371
    return millas
def mostrar_resultado(millas):
    print("la distancia en millas es:"+ str(millas))
#******zona codigo*****
kilometros = leer_datos()
millas = kilometros_a_millas(kilometros)
mostrar_resultado(millas)
