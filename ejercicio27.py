#****zona funcion********

def leer_datos():
    num = int(input("ingrese un numero:"))
    return num
def calcular_raiz(num):
    raiz = num ** 0.5
    return raiz
def mostrar_resultado(raiz):
    print("el resultado de la raiz es:"+ str(raiz))
    
#*******zona codigo*******

num = leer_datos()
raiz = calcular_raiz(num)
mostrar_resultado(raiz)
