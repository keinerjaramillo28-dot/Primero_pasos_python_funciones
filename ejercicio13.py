#****************zona funcion**************
def leer_datos():
    longitud = float(input("digite la longitud de la piramide"))
    ancho = float(input("digite el ancho de la piramide"))
    altura = float(input("digite la altura de la piramide"))
    return longitud, ancho, altura
def volumen_piramide(longitud, ancho, altura):
    return longitud * ancho * altura
def mostrar_resultado(volumen):
    print("el volumen de la piramide es"+ str(volumen))

#***************zona codigo******************

longitud, ancho, altura = leer_datos()
volumen = volumen_piramide(longitud, ancho, altura)
mostrar_resultado(volumen)    
