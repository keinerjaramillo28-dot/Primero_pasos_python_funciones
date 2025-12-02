#****************zona funion*******************
def leer_dato():
    radio = float(input("ingrese el radio del cono:"))
    altura = float(input("infrese la altura del cono:"))
    return radio, altura
def volumen_cono(radio, altura):
    return (1/3) * 3.14 * radio**2 * altura
def mostrar_resultado(volumen):
    print("el volumen del cono es:"+ str(volumen))
    
#*************zona codigo****************

radio, altura = leer_dato()
volumen = volumen_cono(radio, altura)
mostrar_resultado(volumen)


    
    