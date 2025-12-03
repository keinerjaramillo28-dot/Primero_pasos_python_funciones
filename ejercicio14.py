#**************zona funcion*****************
def leer_datos():
    pulgadas = int(input("digite cuantas pulgadas se convierten en centimetros"))
    return pulgadas
def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54
def mostrar_resultado(pulgadas):
    print("los centimetros equivalentes a pulgadas es:"+ str(centimetros))

#***********zona codigo*****************

pulgadas = leer_datos()
centimetros = pulgadas_a_centimetros(pulgadas)
mostrar_resultado(centimetros)
    