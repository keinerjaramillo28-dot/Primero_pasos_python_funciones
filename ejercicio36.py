#******zona funcion******
def leer_datos():
    num1 = int(input("digite el primer numero entero:"))
    num2 = int(input("digite el segundo numero entero:"))
    return num1, num2
def calcular_cociente(num1, num2):
    cociente = num1 // num2
    return cociente
def mostrar_resultado(cociente):
    print("el cociente de la division entera es:"+ str(cociente))
#*******zona codigo********
num1, num2 = leer_datos()
cociente = calcular_cociente(num1, num2)
mostrar_resultado(cociente)
