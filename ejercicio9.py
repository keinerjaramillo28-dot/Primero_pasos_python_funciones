#*******************zona funcion***********************
def leer_datos():
    base_mayor = float(input("ingrese la base mayor del trapecio:"))
    base_menor = float(input("ingrese la base menor del trapecio:"))
    altura = float(input("ingrese la altura del trapecio"))
    return base_mayor, base_menor, altura
def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) / 2) * altura
def mostrar_resultado(area):
    print("el area del trapecio es:" + str (area))
    
#*************zona codigo*********************

base_mayor, base_menor, altura = leer_datos()
area = area_trapecio(base_mayor, base_menor, altura)
mostrar_resultado(area)
