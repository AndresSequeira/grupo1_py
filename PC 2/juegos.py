# Preguntar la edad del cliente
edad = int(input("¿Cuál es tu edad? "))

# Determinar el precio de la entrada
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10

# Mostrar el precio
if precio == 0:
    print("La entrada es gratuita.")
else:
    print(f"El precio de la entrada es {precio}€.")
