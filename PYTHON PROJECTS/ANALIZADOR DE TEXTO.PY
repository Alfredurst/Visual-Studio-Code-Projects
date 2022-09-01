texto = input("Ingrese un texto: ").lower()
letras = []
#print(f"Tu texto es: {texto} Las letras a buscar son: {letras}" )

#convierte cadena en lista
#letras_lista = list(letras)

#agrega los input a la variable letras la cual se creo como una lista en blanco
letras.append(input("Ingresa la primer letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercer letra: ").lower())
#extrae cada elemento de la lista "letras"
letra1 = letras[0]
letra2 = letras[1]
letra3 = letras[2]
#metodo split sin parametro para separar palabras
texto_separado = texto.split()
texto_invertido = texto[::-1]
print (f"El numero de palabras en tu texto es de: {len(texto_separado)} palabras")
print (f"La primer letra de tu texto es: {texto[0]} \nLa ultima letra de tu texto es: {texto[-1]} ")
print (f"La letra {letra1} aparece {texto.count(letra1)} veces\nLa letra {letra2} aparece {texto.count(letra2)} veces\nLa letra {letra3} aparece {texto.count(letra3)} veces ")
print (f"Tu texto inverido queda asi: {texto_invertido}")
# busca la palabra python en el texto y en base a las keys en el diccionario muestra el contenido
tiene_python = texto_separado.count("python")
python_check = tiene_python>0
dic1 = {False:"El texto no contiene la palabra python",True: "El texto si contiene la palabra python"}
print (dic1[python_check])
# invierte orden de lista de las palabras del texto
texto_separado.reverse()
texto_inver = " ".join(texto_separado)
print(texto_inver)

