#********zona funcion********

def leer_datos():
    litros = float(input("digite la cantidad de litros a galones:"))
    return litros
def litros_a_galones(litros):
    galones = litros * 0.26
    return galones
def mostrar_resultado(galones):
    print("la cantida de galones es:"+ str(galones))
    
#*******zona codigo********

litros = leer_datos()
galones = litros_a_galones(litros)
mostrar_resultado(galones)

    