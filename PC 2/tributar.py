# Preguntar al usuario su edad
edad = int(input("¿Cuál es tu edad? "))

# Preguntar al usuario sus ingresos mensuales
ingresos = float(input("¿Cuáles son tus ingresos mensuales en euros? "))

# Comprobar si debe tributar
if edad > 16 and ingresos >= 1000:
    print("Debes tributar.")
else:
    print("No tienes que tributar.")
