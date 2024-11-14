import heroe
import Mazmorra


def main():

    nombre = input("Cual es tu Ego? ")
    player = heroe.Heroe(nombre, 5, 5, 50, 50)

    dungeon = Mazmorra.Dungeon(player)
    dungeon.jugar()


if __name__ == "__main__":
    main()
