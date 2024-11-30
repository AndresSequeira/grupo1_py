# Solicitar las dimensiones del rectángulo al usuario
largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))

# Calcular el área y el perímetro
area = largo * ancho
perimetro = 2 * (largo + ancho)

# Mostrar los resultados
print(f"\nEl área del rectángulo es: {area:.2f}")
print(f"El perímetro del rectángulo es: {perimetro:.2f}")