def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def main():
    print("Conversor de unidades de temperatura")
    try:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        
        fahrenheit = celsius_a_fahrenheit(celsius)
        kelvin = celsius_a_kelvin(celsius)
        
        print(f"\nLa temperatura en grados Fahrenheit es: {fahrenheit:.2f} °F")
        print(f"La temperatura en grados Kelvin es: {kelvin:.2f} K")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
