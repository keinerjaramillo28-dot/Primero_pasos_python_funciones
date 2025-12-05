#*******zona funcion*******

def leer_datos():
    radio = float(input("digite el radio del circulo:"))
    return radio
def calcular_circunferencia(radio):
    circunferencia = 2 * 3.14 * radio
    return circunferencia
def mostrar_resultado(circunferencia):
    print("la circunferencia del circulo es:"+ str(circunferencia))
#*******zona codigo********
radio = leer_datos()
circunferencia = calcular_circunferencia(radio)
mostrar_resultado(circunferencia)
