"""
Generador de contraseñas

"""

import random #importamos la clase random
import string #importamos la clase string

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase  # Minúsculas por defecto
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("¡Bienvenido al generador de contraseñas!")
    try:
        longitud = int(input("¿Cuál será la longitud de tu contraseña? (Recomendado: mínimo 8): "))
        incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
        incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
        incluir_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

        if longitud < 1:
            print("La longitud debe ser al menos 1.")
            return
        
        contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
        print("\nTu nueva contraseña segura es:")
        print(contraseña)
    except ValueError:
        print("Por favor, ingresa un número válido para la longitud.")

#__name__ es un atributo que tienen todas las clases de py
# si el código se ejecuta en la misma clase toma el valor de __main__
# si el archivo se importa toma el valor del archivo pero sin la extensión .py
# si esto se ejecutara en otra clase sería "programa"
if __name__ == "__main__":
    main()