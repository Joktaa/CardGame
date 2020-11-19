from tkinter import *
from constantes import *
import jeux


def main():
    frameChoix = Frame(fenetre, width=1280, height=720, bg="#33ACFF")
    frameChoix.pack()

    def menu():
        frameChoix.pack_forget()
        frameMenu.pack()

    def switchJeuxFrameSolo(soloGame=True):
        frameChoix.pack_forget()
        jeux.jeux(soloGame)

    def switchJeuxFrame(soloGame=False):
        frameChoix.pack_forget()
        jeux.jeux(soloGame)

    bouton1Joueur = Button(
        frameChoix,
        text="1 Joueur",
        width=12,
        height=2,
        font=("arial", 20, "bold"),
        cursor="hand2",
        command=switchJeuxFrameSolo,
    )
    bouton1Joueur.place(x=410, y=200)

    bouton2Joueur = Button(
        frameChoix,
        text="2 Joueur",
        width=12,
        height=2,
        font=("arial", 20, "bold"),
        cursor="hand2",
        command=switchJeuxFrame,
    )
    bouton2Joueur.place(x=670, y=200)

    buttonQuit = Button(
        frameChoix, text="Menu", font="Arial 14", width=12, command=menu
    )
    buttonQuit.place(x=575, y=500)

    fenetre.mainloop()
