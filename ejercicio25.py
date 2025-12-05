#********zona funcion*********

def leer_datos():
    num1 = int(input("digite el primer numero:"))
    num2 = int(input("digite el segundo numero:"))
    return num1, num2
def calcular_division(num1, num2):
    division = num1 / num2
    return division
def mostrar_resultado(division):
    print("el resultado de la division es:"+ str(division))
    
#*******zona codigo********

num1, num2 = leer_datos()
division = calcular_division(num1, num2)
mostrar_resultado(division)
