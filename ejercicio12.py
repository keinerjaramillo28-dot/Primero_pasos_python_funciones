#*****************zona funcion****************

def leer_datos():
    lado = float(input("digite el lado"))
    return lado
def area_cuadrado(lado):
    return lado ** 2
def mostrar_resultado(area):
    print("el area del cuadrado es:"+ str(area))
    
#****************zona codigo*************

lado = leer_datos()
area = area_cuadrado(lado)
mostrar_resultado(area)
    
