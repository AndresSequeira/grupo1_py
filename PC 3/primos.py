def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def buscar_primos_en_rango(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

def main():
    print("Buscador de números primos en un rango")
    try:
        inicio = int(input("Ingresa el número inicial: "))
        fin = int(input("Ingresa el número final: "))
        
        if inicio > fin:
            print("El número inicial debe ser menor o igual al número final.")
            return
        
        primos = buscar_primos_en_rango(inicio, fin)
        if primos:
            print(f"Los números primos en el rango {inicio} a {fin} son:")
            print(primos)
        else:
            print(f"No hay números primos en el rango {inicio} a {fin}.")
    except ValueError:
        print("Por favor, ingresa números enteros válidos.")

if __name__ == "__main__":
    main()
