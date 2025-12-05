#*******zona funcion******

def leer_datos():
    base = float(input("digite la base del triangulo:"))
    altura = float(input("digite la altura del triangulo:"))
    return base, altura
def calcular_area(base, altura):
    area = base * altura
    return area
def mostrar_resultado(area):
    print("el area del triangulo es:"+ str(area))
    
#******zona codigo*****

base, altura = leer_datos()
area = calcular_area(base, altura)
mostrar_resultado(area)
