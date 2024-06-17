# Función para obtener temperatura diaria
def obtener_temperatura():
    temperatura = float(input("Introduce la temperatura diaria (en grados Celsius): "))
    return temperatura

# Función para obtener temperaturas diarias durante una semana
def obtener_temperaturas_semanales():
    temperaturas = []
    for _ in range(7):
        temperaturas.append(obtener_temperatura())
    return temperaturas

# Función para calcular el promedio de temperaturas
def calcular_promedio_temperaturas(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal para obtener y mostrar el promedio de temperaturas
def main():
    temperaturas_semanales = obtener_temperaturas_semanales()
    promedio_temperaturas = calcular_promedio_temperaturas(temperaturas_semanales)
    print(f"El promedio de temperaturas durante la semana es: {promedio_temperaturas:.2f} grados Celsius")

# Ejecutar la función principal
if __name__ == "__main__":
    main()