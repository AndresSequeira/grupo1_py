# Solicitar las calificaciones al usuario
calificaciones = input("Introduce las calificaciones de los exámenes separadas por espacios: ")

# Convertir la entrada en una lista de números
lista_calificaciones = list(map(float, calificaciones.split()))

# Calcular el promedio
if lista_calificaciones:  # Verificar que la lista no esté vacía
    promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    # Mostrar el resultado
    print(f"\nEl promedio de las calificaciones {lista_calificaciones} es: {promedio:.2f}")
else:
    print("\nNo se ingresaron calificaciones.")