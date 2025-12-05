#*****zona funcion*****
def leer_datos():
    num1 = float(input("digite el primer numero:"))
    num2 = float(input("digite el segundo numero:"))
    return num1, num2
def mostrar_mayor(num1, num2):
    if num1 > num2:
        mayor = num1
    else:
        mayor = num2
        return mayor
def mostrar_resultado(mayor):
    print("el numero mayor es: " + str(mayor))
#********zona codigo********
num1, num2 = leer_datos()
mayor = mostrar_mayor(num1, num2)
mostrar_resultado(mayor)
