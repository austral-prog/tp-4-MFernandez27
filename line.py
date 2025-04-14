import math
def line():

    y1 =float(input("Ingrese el coeficiente A:"))
    y2 =float(input("Ingrese el coeficiente B:"))
    X1 =float(input("Ingrese el coeficiente X1:"))
    X2 =float(input("Ingrese el coeficiente X2:"))
    a2 = (y1*X1) + y2
    a4 = (y1*X2) + y2
    distancia =  math.sqrt(((X2-X1)**2) + ((a4-a2)**2))

    print(f"El coeficiente A de su ecuación de la recta es: {y1}")
    print(f"El coeficiente B de su ecuación de la recta es: {y2}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    print(f"Para la siguiente ecuación: \n\t Y = {y1}X + {y2}") #FORMULA
    print(f"Dados los siguientes puntos: \n\tP1 = ({X1}, {a2})")
    print(f"\tP2 = ({X2}, {a4})")
    print(f"\nLa distancia entre ellos es: {distancia} ")
