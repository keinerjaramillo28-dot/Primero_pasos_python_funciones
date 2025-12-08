#************zona funcion**************
def leer_datos():
    lado = float(input("digite el lado del hexagono:"))
    return lado
def area_hexagono(lado):
    area = (3*(3)/2 * lado **2)
    return area
def mostrar_resultado(area):
    print("el arae del hexagono es:"+ str(area))

#********zona codigo**********

lado = leer_datos()
area = area_hexagono(lado)
mostrar_resultado(area)    