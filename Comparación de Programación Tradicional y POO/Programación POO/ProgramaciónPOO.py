# Clase para representar la información diaria del clima
class Clima:
    def __init__(self):
        self.temperaturas = []

    # Método para agregar temperatura diaria
    def agregar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    # Método para calcular el promedio de temperaturas
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para obtener temperaturas diarias durante una semana
    def obtener_temperaturas_semanales(self):
        for _ in range(7):
            temperatura = float(input("Introduce la temperatura diaria (en grados Celsius): "))
            self.agregar_temperatura(temperatura)

    # Método para mostrar el promedio de temperaturas
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio de temperaturas durante la semana es: {promedio:.2f} grados Celsius")

# Clase principal para ejecutar la aplicación
class ClimaApp:
    def __init__(self):
        self.clima = Clima()

    # Método para ejecutar la aplicación
    def ejecutar(self):
        self.clima.obtener_temperaturas_semanales()
        self.clima.mostrar_promedio()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = ClimaApp()
    app.ejecutar()