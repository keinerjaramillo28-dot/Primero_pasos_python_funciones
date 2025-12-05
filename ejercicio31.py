
#********zona funcion********
def leer_datos():
    horas = float(input("digite la cantidad de horas a minutos:"))
    return horas
def horas_a_minutos(horas):
    minutos = horas * 60
    return minutos
def mostrar_resultado(minutos):
    print("la cantidad de minutos es:"+ str(minutos))
    
#********zona codigo********
horas = leer_datos()
minutos = horas_a_minutos(horas)
mostrar_resultado(minutos)
