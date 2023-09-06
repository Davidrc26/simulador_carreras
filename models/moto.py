from models.vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self):
        super().__init__(120, 30)