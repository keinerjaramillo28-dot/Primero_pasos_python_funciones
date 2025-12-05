#*********zona funcion*******
def leer_datos():
    num = int(input("digite un numero:"))
    return num
def calcular_cuadrado(num):
    cuadrado = num * 4
    return cuadrado
def mostrar_resultado(cuadrado):
    print("el resultado del cucdrado es:"+ str(cuadrado))
    
#*******zona codigo********

num = leer_datos()
cuadrado = calcular_cuadrado(num)
mostrar_resultado(cuadrado)
