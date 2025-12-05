#****zona funcion*****
def leer_datos():
    num1 = float(input("digite el primer numero:"))
    num2 = float(input("digite el segundo numero:"))
    return num1, num2
def calcular_promedio(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio
def mostrar_resultado(promedio):
    print("el promedio de los dos numeros es: " + str(promedio))
#********zona codigo********
num1, num2 = leer_datos()
promedio = calcular_promedio(num1, num2)
mostrar_resultado(promedio)
