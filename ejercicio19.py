#********zonaa funcion***********
def leer_datos():
    longitud = float(input("digite la longitud del prisma:"))
    altura = float(input("digite la altura del prisma:"))
    ancho = float(input("digite el ancho del prisma:"))
    return longitud, altura, ancho

def calcular_volumen(longitud, altura, ancho):
    volumen = longitud * altura * ancho
    return volumen
def mostrar_resultado(volumen):
    print("el volumen del prisma es:"+ str(volumen))

#*********zona codigo************

longitud, altura, ancho = leer_datos()
volumen = calcular_volumen(longitud, altura, ancho)
mostrar_resultado(volumen)
