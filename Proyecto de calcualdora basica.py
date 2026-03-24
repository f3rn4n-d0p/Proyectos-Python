#Titulo
print("===Calcualdora Básica===")
#Los números al usuario
numero1=float(input("Ingresa el primer número: "))
numero2=float(input("Ingresa el segundo número: "))

#Opciones
print("Elige una operación:")

print("1 Sumar")

print("2 Restar")

print("3 Multiplicar")

print("4 Potencia")

print("5 Dividir")

opcion=input("Opción (1-4):")

if opcion=="1":
    resultado=numero1+numero2
    print(f"Resultado: {numero1}+{numero2}={resultado}")
elif opcion=="2":
    resultado= numero1-numero2
    print(f"Resultado: {numero1}-{numero2}={resultado}")
elif opcion=="3":
    resultado= numero1*numero2
    print(f"Resultado: {numero1}*{numero2}={resultado}")
elif opcion=="4":
    resultado=numero1**numero2
    print(f"Resultado: {numero1}**numero2}={resultado}")
elif opcion=="5":
    if numero2 != 0:
        resultado= numero1/numero2
        print(f"Resultado: {numero1}/{numero2}={resultado}")
    else:
        print("Error no se puede Dividir por cero")
else:
    print("Opción no valida")
    
