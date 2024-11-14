class Monstruo:
    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def __str__(self):
        print("!!!!!!!!!!!!!!")
        print("Monstruo: " + str(self.nombre))
        print("Ataque: " + str(self.ataque))
        print("Defensa: " + str(self.defensa))
        print("Salud: " + str(self.salud))
        return "!!!!!!!!!!!!!!"

    def atacar(self, heroe):
        print("El monstruo: " + self.nombre + " ataca a " + heroe.nombre)

        if self.ataque > heroe.defensa:
            heroe.salud = heroe.salud - (self.ataque - heroe.defensa)
            print(
                heroe.nombre
                + " recibe "
                + str(self.ataque - heroe.defensa)
                + " puntos de daño"
            )
            print("Salud actual: " + str(heroe.salud))
        else:
            print("El heroe ha bloqueado el ataque")

    def esta_vivo(self):
        if self.salud == 0 or self.salud < 0:
            return False
        else:
            return True
