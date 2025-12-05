#Escribe un programa que pida un número y determine si es par o impar usando el operador de módulo (%)

def leer_datos():
    num = int(input("digite un numero:"))
    return num

def determinar_par_impar(num):
    if num % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado
def mostrar_resultado(resultado):
    print("el numero es:"+ str(resultado))
#*******zona codigo********
num = leer_datos()
resultado = determinar_par_impar(num)
mostrar_resultado(resultado)
