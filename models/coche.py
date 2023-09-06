from models.vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self):
        super().__init__(150, 50)

    def activar_turbo(self):
        self.velocidad_maxima += 20
