#**********zona funcion********
def leer_datos():
    num1 = int(input("digite el primer numero:"))
    num2 = int(input("digite el segundo numero:"))
    return num1, num2
def resolver_producto(num1, num2):
    producto = num1 * num2
    return producto
def mostrar_resultado(producto):
    print ("el resultado del producto es:"+ str(producto))
    
#****zona codigo*******

num1, num2 = leer_datos()
producto = resolver_producto(num1, num2)
mostrar_resultado(producto)
    