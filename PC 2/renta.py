# Preguntar al usuario su renta anual
renta = float(input("Introduce tu renta anual en dolares: "))

# Determinar el tipo impositivo según la renta
if renta < 10000:
    tipo_impositivo = 5
elif 10000 <= renta < 20000:
    tipo_impositivo = 15
elif 20000 <= renta < 35000:
    tipo_impositivo = 20
elif 35000 <= renta < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

# Mostrar el resultado
print(f"Tu tipo impositivo es del {tipo_impositivo}%.")
