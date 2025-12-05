
#********zona funcion*********
def leer_datos():
    longitud = float(input("digite la longitud del rectangulo:"))
    ancho = float(input("digite el ancho del rectangulo:"))
    return longitud, ancho
def calcular_area(longitud, ancho):
    area = longitud * ancho
    return area
def mostrar_resultado(area):
    print("el area del rectangulo es:"+ str(area))
#********zona codigo*********
longitud, ancho = leer_datos()
area = calcular_area(longitud, ancho)
mostrar_resultado(area)
