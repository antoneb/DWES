from operaciones import *

operando1 = int(input("Introduce el primer operando: "))
operando2 = int(input("Introduce el segundo operando: "))


print("¿ Que operacion deseas hacer ?")
print ("(1) Sumar")
print ("(2) Restar")
print ("(3) Multiplicar")
print ("(4) Dividir")

respuesta = int(input("Respuesta: "))

if respuesta == 1:
    print(suma(operando1,operando2))
elif respuesta == 2:
    print(resta(operando1,operando2))
elif respuesta == 3:
    print(multi(operando1,operando2))
elif respuesta == 4:
    print(divi(operando1,operando2))