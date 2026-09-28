#ejercicio 4
#obtener el radio de un circulo para calcular el area

import math 

pi = math.pi
numero = input('Ingrese el perimetro del circulo:' )
numero = int(numero)

radio = numero**2 * pi
resultado = f"{radio:.2f}"
print(resultado)