#********zona funcion*********

def leer_datos():
    num1 = int(input("digite el primer numero:"))
    num2 = int(input("digite el segundo numero:"))
    return num1, num2
def hacer_resta(num1, num2):
    resta = num1 - num2
    return resta
def mostrar_resultado(resta):
    print("el resultado del resultado es:"+ str(resta))
    
#********zona codigo********

num1, num2 = leer_datos()
resta = hacer_resta(num1, num2)
mostrar_resultado(resta)

    