
#********zona funcion********
def leer_datos():
    dinero = float(input("digite la cantidad de dinero en la cuenta:"))
    return dinero
def calcular_interes(dinero):
    interes = dinero * 0.05
    return interes
def mostrar_resultado(interes):
    print("el interes ganado es de:"+ str(interes))
#********zona codigo********
dinero = leer_datos()
interes = calcular_interes(dinero)
mostrar_resultado(interes)
