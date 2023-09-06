import time
class Carrera:

    def carrera_vehiculos(vehiculos):
        distancia_carrera = 100  # Distancia de la carrera en kilómetros
        ganador = None

        print("Comienza la carrera!")
        time.sleep(1)

        while ganador is None:
            for vehiculo in vehiculos:
                if vehiculo.gasolina_actual <= 0:
                    continue

                # Aplicar aceleración y consumo de gasolina
                vehiculo.acelerar()
                vehiculo.gasolina_actual -= 5

                # Comprobar si ha llegado a la meta
                if vehiculo.velocidad_actual >= distancia_carrera:
                    ganador = vehiculo
                    break

                print(f"{type(vehiculo).__name__}: {vehiculo}")
                time.sleep(0.1)

        print(f"{type(ganador).__name__} ha ganado la carrera!")