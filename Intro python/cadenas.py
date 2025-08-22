#Ingresa 3 notas y obten su promedio. Si es mayor a 40 aprueba si no reprueba

# nota1 = float(input("Ingrese su nota: "))
# nota2 = float(input("Ingrese su nota: "))
# nota3 = float(input("Ingrese su nota: "))
# promedio = (nota1 + nota2 + nota3)/3
# if promedio > 4.0:
#     print(f"A pasado el ramo con un promedio {promedio:.2}")
# else:
#     print(f"A reprobado el ramo con un promedio {promedio:.2}")

#Ingrese 2 numeros, sumarlos, restarlos, multiplicarlos y debe mostrar cada resultado

lista = []
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
lista.append(numero1)
lista.append(numero2)

sum = lista[0] + lista[1]
print(f"La suma es {sum}")

res = lista[0] - lista[1]
print(f"La resta es {res}")

mult = lista[0] * lista[1]
print(f"La multiplicacion es {mult}")

