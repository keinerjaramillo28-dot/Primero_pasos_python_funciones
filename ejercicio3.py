#*************zona funcion***************

def definir_ancho():
    ancho = 16
    return ancho
def definir_longitud():
    longitud = 20
    return longitud
def calcular_area(ancho, longitud):
    area = (ancho * longitud)
    return area
def imprimir_datos(ancho, longitud):
    mensaje = "el ancho es:" + ancho
    mensaje = "la longitud es:" + longitud
def imprimir_resultado(resultado_area):
    print("el area del rectangulo es:"+ str(resultado_area))
    
    
#**************zona codigo*******************

ancho = definir_ancho()
longitud = definir_longitud()
area = calcular_area(ancho, longitud)
resultado = imprimir_resultado(area)        
        