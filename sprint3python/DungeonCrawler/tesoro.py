import random


class Tesoro:
    def __init__(self):
        self.beneficios = ["ataque", "defensa", "salud"]

    def encontrar_tesoro(self, heroe):
        num = random.randint(0, 2)
        beneficios = self.beneficios
        if num == 0:
            # mejora de ataque
            print(
                heroe.nombre
                + " ha encontrado una mejora de "
                + self.beneficios[0]
                + ", aumenta en 3 puntos"
            )
            heroe.ataque = heroe.ataque + 3

        if num == 1:
            # mejora de defensa
            print(
                heroe.nombre
                + " ha encontrado una mejora de "
                + self.beneficios[1]
                + ", aumenta en 3 puntos"
            )
            heroe.defensa = heroe.defensa + 3

        if num == 2:
            # Restaurar salud
            print(
                heroe.nombre
                + " ha encontrado una pocion de "
                + self.beneficios[2]
                + ", restaura todos sus puntos de vida !"
            )
            heroe.salud = heroe.saludMax
