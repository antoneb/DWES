class Heroe:
    def __init__(self, nombre, ataque, defensa, salud, saludMax):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.saludMax = saludMax
        self.cura = 10

    def __str__(self):
        print("+++++++++++++++++++++")
        print("Heroe: " + str(self.nombre))
        print("Ataque: " + str(self.ataque))
        print("Defensa: " + str(self.defensa))
        print("Salud: " + str(self.salud) + "/" + str(self.saludMax))
        print("Curacion:" + str(self.cura))
        return "+++++++++++++++++++++"
       

    def atacar(self, maloso):
        print(self.nombre + " ataca a " + maloso.nombre)

        if self.ataque > maloso.defensa:
            maloso.salud = maloso.salud - (self.ataque - maloso.defensa)
            print(
                str(maloso.nombre)
                + " recibe "
                + str((self.ataque - maloso.defensa))
                + " puntos de daño"
            )
            print("Salud actual de " + str(maloso.nombre) + ": " + str(maloso.salud))
        else:
            print("El enemigo ha bloqueado el ataque")

    def curarse(self):
        if (self.salud + self.cura) > self.saludMax:
            self.salud = self.saludMax
            print(self.nombre + " se curó por completo!")
        else:
            self.salud = self.salud + self.cura
            print(self.nombre + " se curó " + self.cura + " puntos de salud !")

    def defenderse(self):
        print("Defensa aumentada en 5 puntos para el siguiente ataque")
        self.defensa = self.defensa + 5

    def reset_defensa(self):
        self.defensa = self.defensa - 5
        print("La Defensa de " + self.nombre + " vuelve a la normalidad")

    def esta_vivo(self):
        if self.salud == 0 or self.salud<0:
            return False
        else:
            return True
