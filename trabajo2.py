#*************zona funcion**************+
def dar_letra():
    while True:
     print("digite la letra'A' para actualizar sistema")
     print("digite la letra 'B' para eliminar catalogo")
     print("digite la letra 'C' para crear productos")
     print("digite la letra 'D' para salir del programa")
     letra = str (input ("seleccione opcion"))
     return letra

def validar_letra(dato_let):

   if dato_let=='D' or dato_let== 'd':
      mensaje = "finalizando con exito."
   elif dato_let == 'A' or dato_let =='a':
      mensaje = "actualizando sistema........."

   elif dato_let =='B' or dato_let =='b':
      mensaje = "eliminando catalogo........"
   elif dato_let == 'C' or dato_let == 'c':
      mensaje = "creando producto........."

   return mensaje

def dar_mensaje(dato_mensaje):
   print("se esta " + dar_mensaje)

def mensaje_alt():
   print("el do-while ha terminado")

#*************zona codigo****************      

dato_let = dar_letra()
dato_mensaje = validar_letra(dato_let)
dar_mensaje (dar_mensaje)
mensaje_alt()
      
      
           