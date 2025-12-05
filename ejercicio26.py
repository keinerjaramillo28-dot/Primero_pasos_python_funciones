#**********zona funcion*********
def leer_datos():
    num1 = int(input("digite el primer numero:"))
    num2 = int(input("digite el segundo numero:"))
    return num1, num2
def determinar_residuo(num1, num2):
    residuo = num1 / num2
    return residuo
def mostrar_resultado(residuo):
    print("es residuo de la division es:"+ str(residuo))
    
#******zona codigo********

num1, num2 = leer_datos()
residuo = determinar_residuo(num1, num2)
mostrar_resultado(residuo)
