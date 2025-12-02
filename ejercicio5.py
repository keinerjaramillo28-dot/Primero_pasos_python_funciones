#*****************zona funcion******************

def leer_radio():
    radio = float(input("ingrese el radio del circulo"))
    return radio
def cacular_area(radio):
    return 3.14 * radio**2
def mostrar_resultado(area):
    print("el area del circulo es:"+ str(area))



#************zona codigo*****************

radio = leer_radio()
area = cacular_area(radio)
mostrar_resultado(area)
                
        
