#***********zona funcion**********

def definir_altura():
    altura_+= 12
    return altura_
def definir_base():
    base_+=15
    return base
def calcular_area(base,altura):
    area=(base*altura)/2
    return area
def imprimir_dato (base, altura_):
    mensaje = "la base es:" +base
    mensaje = "la altura es:"+ base
def imprimir_resultado(resultado_area):
    print("el area del triangulo es:"+ str (resultado_area)) 


#************zona codigo***********
base = definir_base()
altura = definir_altura()
area = calcular_area(base,altura)
resultado = imprimir_resultado(area)