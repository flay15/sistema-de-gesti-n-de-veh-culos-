class Vehiculo:
    def __init__(self, matricula, marca, modelo, año, color):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Matricula: {self.matricula}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Color: {self.color}"


class SistemaGestionVehiculos:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo con matrícula {vehiculo.matricula} agregado correctamente.")

    def eliminar_vehiculo(self, matricula):
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo:
            self.vehiculos.remove(vehiculo)
            print(f"Vehículo con matrícula {matricula} eliminado correctamente.")
        else:
            print(f"No se encontró un vehículo con matrícula {matricula}.")

    def listar_vehiculos(self):
        if self.vehiculos:
            print("Lista de vehículos:")
            for vehiculo in self.vehiculos:
                print(vehiculo)
        else:
            print("No hay vehículos registrados.")

    def buscar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                return vehiculo
        return None


def menu():
    sistema = SistemaGestionVehiculos()

    while True:
        print("\nSistema de Gestión de Vehículos")
        print("1. Agregar vehículo")
        print("2. Eliminar vehículo")
        print("3. Listar vehículos")
        print("4. Buscar vehículo por matrícula")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matricula = input("Ingrese la matrícula del vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = input("Ingrese el año del vehículo: ")
            color = input("Ingrese el color del vehículo: ")

            vehiculo = Vehiculo(matricula, marca, modelo, año, color)
            sistema.agregar_vehiculo(vehiculo)

        elif opcion == "2":
            matricula = input("Ingrese la matrícula del vehículo a eliminar: ")
            sistema.eliminar_vehiculo(matricula)

        elif opcion == "3":
            sistema.listar_vehiculos()

        elif opcion == "4":
            matricula = input("Ingrese la matrícula del vehículo a buscar: ")
            vehiculo = sistema.buscar_vehiculo(matricula)
            if vehiculo:
                print(vehiculo)
            else:
                print(f"No se encontró un vehículo con matrícula {matricula}.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
