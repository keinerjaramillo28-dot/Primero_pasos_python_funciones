#*********zona funcion**********
def leer_datos():
    num1 = int(input("digite el primer numero:"))
    num2 = int(input("digite el segundo numero:"))
    return num1, num2
def hacer_suma(num1, num2):
    suma = num1 + num2
    return suma
def mostrar_resultado(suma):
    print("el resultado de la suma es:"+ str(suma))
    
#*********zona codigo*************

num1, num2 = leer_datos()
suma = hacer_suma(num1, num2)
mostrar_resultado(suma)
        