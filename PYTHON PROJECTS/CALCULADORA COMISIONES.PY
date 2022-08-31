nombre = input("Cual es tu nombre: ")
ventas = input("Cuanto vendiste: ")
ventas =float(ventas)
print(type (ventas))
comision = ventas*13/100
comision_final = round(comision,2)
print(f" {nombre} tus ventas fueron de ${ventas} por lo que tu comision sera de ${comision_final}")
mi_texto = "Esto es una prueba para los metodos de cadenas"
mitexto2 = mi_texto

#Invertir string con index
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase_index = frase[::-1]  #  [argument1 start : argument2 end : argument3 paso ]
print(frase_index)