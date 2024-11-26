# Almacenar la contraseña en una variable
contraseña_guardada = "MiContrasena"

# Pedir al usuario que introduzca la contraseña
contraseña_usuario = input("Introduce la contraseña: ")

# Verificar si coinciden (ignorando mayúsculas y minúsculas) , el Lower transforma la cadena a miniscula
if contraseña_guardada.lower() == contraseña_usuario.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
