#******************zona funcion*****************
def leer_datos():
    base = float(input("ingrese la base del paralelogramo"))
    altura = float(input("ingrese la altura del paralelogramo"))
    return base, altura
def area_paralelogramo(base, altura):
    return base * altura
def mostrar_resultado(area):
    print("el area del paralelogramo es:"+ str(area))

#***************zona codigo****************

base, altura = leer_datos()
area = area_paralelogramo(base, altura)
mostrar_resultado(area)
    