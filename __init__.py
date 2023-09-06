from models.camion import *
from models.coche import *
from models.moto import *
from models.carrera import *

def turbo_decorator(vehicle):
    class TurboVehicle(vehicle):
        def __init__(self):
            super().__init__()

        def acelerar(self):
            self.velocidad_actual += 30

    return TurboVehicle

if __name__ == "__main__":
    # Crear vehículos y decorar algunos con Turbo
    vehiculo1 = Coche()
    vehiculo2 = Moto()
    vehiculo3 = Camion()
    vehiculo4 = turbo_decorator(Coche)()

    # Iniciar la carrera con los vehículos
    Carrera.carrera_vehiculos([vehiculo1, vehiculo2, vehiculo3, vehiculo4])
