from tkinter import *
from constantes import *


def main():
    def activeInstructionFrame():
        frameInstruction.pack()

    def retourMenu():
        frameInstruction.pack_forget()
        frameMenu.pack()

    # Frame instruction
    frameInstruction = Frame(fenetre, width=1280, height=720, bg="#33ACFF")
    activeInstructionFrame()

    stat_joueur = "JOUEUR\n - Vie, il faut enlever tous les points de vie de l'adversaire\n - Mana, permet d’acheter des cartes, on en gagne à chaque tour\n - Bouclier, permet de se défendre\n - Main, les cartes que le joueur possède"
    stat_carte = "CARTE\n - Vie, à zéro, la carte meurt\n - Attaque, la force des actions disponibles (cf.Actions)\n - Coût, en mana pour jouer la carte.\n - Effet, l’action que la carte réalise (cf.Actions)\n - Cible, sur qui l’effet est dirigé\n - Élément, définit les forces et faiblesses (Feu > Vent > Eau > Feu)"

    action_joueur = "JOUEUR\n - Détruire carte: détruit une carte de la main du joueur\nactuel\n - Jouer la carte: pose la carte dans le jeu, dépense du mana\n - Finir tour: passe le tour à l’autre joueur"
    action_carte = "CARTE\n - Attaquer: enlève de la vie à la cible\n - Soigner: Ajoute de la vie à la cible\n - Défendre: Ajoute du bouclier au joueur\n - Piocher: Pioche une carte\n - Défausser: Défausse une carte dans la main adverse."

    deroulement = "Le jeu se joue à un ou deux en tour par tour. Lors d’un tour, le joueur\nréalise ses actions (cf.Actions), puis ses cartes jouent leurs actions,\nc’est ensuite à l’autre joueur de jouer.\nLa partie se termine lorsque l’un des joueurs n’a plus de vie."

    # ==========STATS==========
    stat_canvas = Canvas(frameInstruction, bg="#33ACFF", width=650, height=400,)
    stat_canvas.place(x=15, y=15)

    stat_label = Label(
        stat_canvas, text="Les statistiques", font=("Arial", 25), bg="#33ACFF"
    )
    stat_label.place(x=10, y=15)

    stat_joueur_label = Label(
        stat_canvas, text=stat_joueur, font=("Arial", 15), bg="#33ACFF", justify="left"
    )
    stat_joueur_label.place(x=25, y=60)

    stat_carte_label = Label(
        stat_canvas, text=stat_carte, font=("Arial", 15), bg="#33ACFF", justify="left"
    )
    stat_carte_label.place(x=25, y=200)

    # ==========ACTIONS==========
    action_canvas = Canvas(frameInstruction, bg="#33ACFF", width=575, height=400,)
    action_canvas.place(x=690, y=15)

    action_label = Label(
        action_canvas, text="Les actions", font=("Arial", 25), bg="#33ACFF"
    )
    action_label.place(x=10, y=15)

    action_joueur_label = Label(
        action_canvas,
        text=action_joueur,
        font=("Arial", 15),
        bg="#33ACFF",
        justify="left",
    )
    action_joueur_label.place(x=25, y=60)

    action_carte_label = Label(
        action_canvas,
        text=action_carte,
        font=("Arial", 15),
        bg="#33ACFF",
        justify="left",
    )
    action_carte_label.place(x=25, y=200)

    # ==========DEROULEMENT==========
    deroulement_canvas = Canvas(frameInstruction, bg="#33ACFF", width=650, height=200,)
    deroulement_canvas.place(x=350, y=450)

    deroulement_label = Label(
        deroulement_canvas,
        text="Deroulement d'une partie",
        font=("Arial", 25),
        bg="#33ACFF",
    )
    deroulement_label.place(x=10, y=15)

    deroulement_text_label = Label(
        deroulement_canvas,
        text=deroulement,
        font=("Arial", 15),
        bg="#33ACFF",
        justify="left",
    )
    deroulement_text_label.place(x=25, y=60)

    # Bouton menu
    buttonMenu = Button(
        frameInstruction,
        text="Menu",
        width=16,
        cursor="hand2",
        font="Arial 12",
        command=retourMenu,
    )
    buttonMenu.place(x=1100, y=680)

    fenetre.mainloop()
