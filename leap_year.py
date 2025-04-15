def leap_year():
	ano = int(input("Ingrese un año: "))
	if ((ano%4 == 0) and (ano%100 != 0)) or ((ano%400 == 0) and (ano%100 == 0)):
		print(f"El año {ano} es bisiesto")
	else:
		print(f"El año {ano} no es bisiesto")







