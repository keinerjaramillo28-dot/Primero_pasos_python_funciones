#*************zona funcion**************

def leer_celsius():
    celsius = float(input("ingrese la tamperatura en grados celsius:"))
    return celsius
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 35
def mostrar_resultado(fahrenheit):
    print ("la temperatura en grado farenheit es:"+ str(fahrenheit))
    
    
#*************zona codigo**************

celsius = leer_celsius()
fahrenheit = celsius_a_fahrenheit(celsius)
mostrar_resultado(fahrenheit)

    