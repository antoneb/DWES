import tesoro
import monstruo


class Dungeon:
    def __init__(self, heroe):

        # creamos unos monstruos con sus stats
        ene1 = monstruo.Monstruo("Goblin", 2, 2, 10)
        ene2 = monstruo.Monstruo("Esqueleto", 4, 4, 10)
        ene3 = monstruo.Monstruo("Mantícora", 6, 6, 10)

        # creamos los diferentes niveles del juego, cada uno con su enemigo
        self.malos = [ene1, ene2, ene3]

        self.heroe = heroe

        self.tesoro = tesoro.Tesoro()

    def jugar(self):

        # nivel = enemigo al que nos enfrentamos
        nivel = 1

        print(self.heroe.nombre + " entra en la mazmorra !")
        print(str(self.heroe))

        while nivel <= len(self.malos) and self.heroe.salud > 0:
            # mientras haya malos en la mazmorra y nuestro heroe siga con vida, jugamos: "subimos de nivel"
            print("te encuentras con un " + (self.malos[(nivel - 1)].nombre))
            print(nivel)
            self.enfrentar_enemigo(self.malos[(nivel - 1)])
            nivel = nivel + 1

        # salimos del bucle -> mazmorra completada o heroe muerto
        if nivel >= len(self.malos):
            print("Enhorabuena, completaste la mazmorra!")
        else:
            print("Suerte a la proxima!")

    def enfrentar_enemigo(self, enemigo):

        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print(self.heroe)
            print(enemigo)
            print("Que deseas hacer ?")
            print("(1) Atacar")
            print("(2) Defender")
            print("(3) Curarse")
            accion = int(input("Accion: "))

            if accion == 1:
                # atacar
                self.heroe.atacar(enemigo)
                enemigo.atacar(self.heroe)

            elif accion == 2:
                # defender
                self.heroe.defenderse()
                enemigo.atacar(self.heroe)
                self.heroe.reset_defensa()

            elif accion == 3:
                # curar
                self.heroe.curarse()
                enemigo.atacar(self.heroe)
            else:
                print("accion no válida")

        # salimos del bucle ->  monstruo muerto OR heroe muerto OR opcion invalida

        if enemigo.esta_vivo():
            print(
                self.heroe.nombre
                + " ha sido engullido por la oscuridad de la mazmorra !"
            )

        elif self.heroe.esta_vivo():
            print(self.heroe.nombre + " ha derrotado al " + enemigo.nombre + " !")
            print(self.heroe.nombre + " encuentra un tesoro!")
            self.buscar_tesoro()

        else:
            print("Vuelve a iniciar el juego")

    def buscar_tesoro(self):
        tesoro.Tesoro.encontrar_tesoro(self.tesoro, self.heroe)
