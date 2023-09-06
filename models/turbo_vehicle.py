
def turbo_decorator(vehicle):
    class TurboVehicle(vehicle):
        def __init__(self):
            super().__init__()

        def acelerar(self):
            self.velocidad_actual += 30

    return TurboVehicle