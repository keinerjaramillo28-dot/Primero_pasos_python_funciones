#**************zona funcion****************

def leer_datos():
    kilometros = int(input("digite cuantos kilometros se convierten en millas"))
    return kilometros
def kilometros_a_millas(kilometros):
    return kilometros * 0.621
def mostrar_resultado(millas):
    print("la distancia equivalente en millas es:" + str(millas))
    
#*************zona codigo**************

kilometros = leer_datos()
millas = kilometros_a_millas(kilometros)
mostrar_resultado(millas)
    