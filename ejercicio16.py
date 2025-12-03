#*************zona funcion**************
def leer_lado():
    lado = float(input("digite la longitud del lado del cubo"))
    return lado
def cacular_volumen(lado):
    volumen = lado ** 3
    return volumen
def mostrar_resultado(volumen):
    print("el volumen del cubo es:"+ str(volumen))


#****************zona codigo**************
lado = leer_lado()
volumen = cacular_volumen(lado)
mostrar_resultado(volumen)
