from tkinter import *

# Info fenetre
ecran_width = 1280
ecran_height = 720
ecran_titre = "PyreStone"

# Couleur fenetre
bg_color = [222, 222, 222]

# Font
arial14 = "Arial 14"

# Type d'effet
effets = ["Attaquer", "Soigner", "Defendre", "Piocher", "Defausser"]

# Cible
ciblesFR = ["Une carte", "Toute les carte"]

# Element
element = ["fire", "water", "wind"]
elementFr = ["Feu", "Eau", "Vent"]

# Monstre
monster = [
    "bat",
    "shroom",
    "slime",
    "snake",
    "wolf",
    "warrior",
    "worm",
    "ent",
    "dragon",
    "swordcat",
    "skeleton",
    "bear",
]
monsterSize = [
    (210, 210),
    (250, 250),
    (340, 340),
    (280, 280),
    (225, 225),
    (180, 180),
    (200, 200),
    (165, 165),
    (160, 160),
    (220, 220),
    (220, 220),
    (180, 180),
]
monsterFR = [
    "Chauve-souris",
    "Shroom",
    "Slime",
    "Serpent",
    "Loup",
    "Guerrier",
    "Ver",
    "Ent",
    "Dragon",
    "Mouschataire",
    "Squelette",
    "Ours",
]

# Fenetre
fenetre = Tk()
fenetre.title(ecran_titre)
screen_x = int(fenetre.winfo_screenwidth())
screen_y = int(fenetre.winfo_screenheight())
posX = (screen_x // 2) - (ecran_width // 2)
posY = (screen_y // 2) - (ecran_height // 2) - 25
geo = f"{ecran_width}x{ecran_height}+{posX}+{posY}"
fenetre.resizable(False, False)
fenetre.geometry(geo)

# Frame Menu
frameMenu = Frame(fenetre, width=1280, height=720, bg="#33ACFF")
