import random
import time

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, velocidad_maxima, capacidad_gasolina):
        self.velocidad_maxima = velocidad_maxima
        self.capacidad_gasolina = capacidad_gasolina
        self.velocidad_actual = 0
        self.gasolina_actual = capacidad_gasolina

    def acelerar(self):
        self.velocidad_actual += 10

    def frenar(self):
        self.velocidad_actual -= 10

    def repostar_gasolina(self):
        self.gasolina_actual = self.capacidad_gasolina

    def __str__(self):
        return f"Velocidad: {self.velocidad_actual} km/h, Gasolina: {self.gasolina_actual} litros"






