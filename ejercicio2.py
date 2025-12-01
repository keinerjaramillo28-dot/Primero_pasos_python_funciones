#***********zona funcion****************

def dafinir_pi():
    pi=3.14
    return pi
def definir_radio():
    radio=30
    return radio
def calcular_volumen(pi,radio):
    volumen =(radio**3 *pi)*4/3
    return volumen
def imprimir_datos(pi,radio):
    mensaje = "el numero pi es:"*pi
    mensaje = "el radio es" + radio
 
def imprimir_resultado(rsultado_volumen):
    print("el volumen de la esfera es:" + int(calcular_volumen))
    
    
#****************zona codigo*****************+

pi= definir_radio()    
radio = definir_radio()
volumen = calcular_volumen()
resultado = imprimir_resultado()

        