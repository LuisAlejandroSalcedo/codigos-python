__author__ = "Luis Salcedo"

def DecimalAHexadecimal(): # Esta sera nuestra función principal
    decimal = int(input("Introduzca un numero positivo para convertirlo a hexadecimal: ")) # Pedimos los decimales al usuario
    hexadecimal = "" # En esta variable almacenaremos el valor hexadecimal
    while decimal != 0: 
        # Cambiamos los digitos por los hexadecimales
        rem = CambiarDigitos(decimal % 16)
        # Llenamos la varibale "hexadecimal" con los nuevos valores
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)
    print("Resultado: " + hexadecimal) # Mostramos el resultado

def CambiarDigitos(digitos): # Esta funcion traduce los digitos a sus respectivos hexadecimales
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

DecimalAHexadecimal()
