
#********zona funcion*********
def leer_datos():
    precio = float(input("digite el precio del articulo:"))
    return precio
def calcular_descuento(precio):
    descuento = precio * 0.10
    return descuento
def mostrar_resultado(descuento):
    print("el descuento es de:"+ str(descuento))
#********zona codigo*********
precio = leer_datos()
descuento = calcular_descuento(precio)
mostrar_resultado(descuento)

