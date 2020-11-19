from tkinter import *
from constantes import *
import editeur_carte as edit
import choixJoueur as choix
import instruction

# Frame Menu
frameMenu.pack()


def switchEditeurFrame():
    frameMenu.pack_forget()
    edit.editeur()


def switchJeuxFrame():
    frameMenu.pack_forget()
    choix.main()


def switchInstructionFrame():
    frameMenu.pack_forget()
    instruction.main()


def quitter():
    fenetre.destroy()


# BOUTONS
jouer = Button(
    frameMenu,
    text="Jouer",
    bg="#084AC4",
    fg="#FFF",
    width=10,
    height=2,
    font=("arial", 25, "bold"),
    activebackground="#073C9E",
    activeforeground="#FFF",
    cursor="hand2",
    command=switchJeuxFrame,
)
jouer.place(x=550, y=75)

editeur_carte = Button(
    frameMenu,
    text="Editeur Carte",
    bg="#C408A8",
    fg="#FFF",
    width=10,
    height=2,
    font=("arial", 25, "bold"),
    activebackground="#A2088B",
    activeforeground="#FFF",
    cursor="hand2",
    command=switchEditeurFrame,
)
editeur_carte.place(x=550, y=225)

aide = Button(
    frameMenu,
    text="Aide",
    bg="#33C408",
    fg="#FFF",
    width=10,
    height=2,
    font=("arial", 25, "bold"),
    activebackground="#2D9F0D",
    activeforeground="#FFF",
    cursor="hand2",
    command=switchInstructionFrame,
)
aide.place(x=550, y=375)

quitter = Button(
    frameMenu,
    text="Quitter",
    bg="#C44408",
    fg="#FFF",
    width=10,
    height=2,
    font=("arial", 25, "bold"),
    activebackground="#A73A07",
    activeforeground="#FFF",
    cursor="hand2",
    command=quitter,
)
quitter.place(x=550, y=525)

fenetre.mainloop()
