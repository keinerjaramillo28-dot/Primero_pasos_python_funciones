#***************zona funcion**************
def leer_datos():
    longitud = float(input("ingrese la longitud del prisma rectangular"))
    ancho = float(input("ingrese el ancho del prisma rectangular"))
    altura = float(input("ingrese la altura del prisma rectangular"))
    return longitud, ancho, altura
def volumen_prisma(longitud, ancho, altura):
    return longitud* ancho* altura
def mostrar_resultado(volumen):
    print("el volumen del trapecio rectangular es:" + str(volumen))


#************zona codigo*****************

longitud, ancho, altura = leer_datos()
volumen = volumen_prisma(longitud, ancho, altura)
mostrar_resultado(volumen)
   