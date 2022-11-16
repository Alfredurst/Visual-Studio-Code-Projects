edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print ("Puedes conducir")
elif edad < 18 and tiene_licencia == False:
    print ("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad >= 18 and tiene_licencia == False:
    print ("No puedes conducir. Necesitas contar con una licencia")


# imprime numeros de la lista

numero = [1,2,3,4,5,6]
for saludo in numero:
    print (f"hola {saludo}")


# suma numeros de la lista

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print (suma_numeros)



# suma numeros impares y pares por separado

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero%2 == 1:
        suma_impares = suma_impares+numero
    else:
        suma_pares = suma_pares+numero
print (suma_impares)
print (suma_pares)


# imprime numeros del 10 al 0

numero = 10
while numero >=0:
    print (numero)
    numero -=1


    
