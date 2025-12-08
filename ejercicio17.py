#*******zona funcion************
def leer_datos():
    libras = float(input("digite las libras a pasar a kilogramos:"))
    return libras
def libras_a_klg(libras):
    return libras * 0.45
def mostrar_resultado(klg):
    print("el resultado en kilogramos es:"+ str(klg))

#*********zona codigo***************

libras = leer_datos()
klg = libras_a_klg(libras)
mostrar_resultado(klg)

