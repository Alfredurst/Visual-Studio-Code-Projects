nombre = input("Cual es tu nombre: ")
ventas = input("Cuanto vendiste: ")
ventas =float(ventas)
print(type (ventas))
comision = ventas*13/100
comision_final = round(comision,2)
print(f" {nombre} tus ventas fueron de ${ventas} por lo que tu comision sera de ${comision_final}")