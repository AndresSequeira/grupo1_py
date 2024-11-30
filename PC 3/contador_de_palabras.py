def contar_palabras(texto):
    # Divide el texto en palabras usando el espacio como delimitador
    palabras = texto.split()
    return len(palabras)

def main():
    print("Contador de palabras en un texto")
    texto = input("Por favor, ingresa un texto: ")
    
    cantidad_palabras = contar_palabras(texto)
    print(f"El texto ingresado contiene {cantidad_palabras} palabras.")

if __name__ == "__main__":
    main()
