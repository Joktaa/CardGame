from tkinter import *
import random
from PIL import Image as Img, ImageTk as ImgTk

# Class joueur
class joueur:
    def __init__(self, window, xpos, ypos, vie, mana, deck, text):
        self.mana = mana
        self.maxMana = mana
        self.vie = vie
        self.bouclier = 0
        self.xpos, self.ypos = xpos, ypos
        self.canvas = Canvas(window, width=170, height=200)
        self.outline = self.canvas.create_rectangle(
            3, 3, 170, 200, width=3, outline="black"
        )
        self.window = window
        self.windowCanvas = window.create_window(
            self.xpos, self.ypos, window=self.canvas
        )
        self.nbrCarte = 0
        self.deck = deck
        self.restCarteDeck = len(self.deck)
        self.main = []
        self.manaText = self.canvas.create_text(
            10,
            20,
            text=f"Mana : {self.mana}",
            font="Arial 14",
            anchor="w",
            fill="black",
        )
        self.vieText = self.canvas.create_text(
            10, 50, text=f"Vie : {self.vie}", font="Arial 14", anchor="w", fill="black"
        )
        self.bouclierText = self.canvas.create_text(
            10,
            80,
            text=f"Bouclier : {self.bouclier}",
            font="Arial 14",
            anchor="w",
            fill="black",
        )
        # self.nbrCarteText = self.canvas.create_text(
        #     10,
        #     110,
        #     text=f"Nombre carte : {self.nbrCarte}",
        #     font="Arial 14",
        #     anchor="w",
        #     fill="black",
        # )
        # self.restCarteDeckText = self.canvas.create_text(
        #     10,
        #     140,
        #     text=f"Carte restante : {self.restCarteDeck}",
        #     font="Arial 14",
        #     anchor="w",
        #     fill="black",
        # )
        self.text = self.canvas.create_text(
            10, 180, text=text, font="Arial 14", anchor="w", fill="black"
        )

    def changerMana(self, nbr):
        self.mana += nbr
        self.canvas.itemconfig(self.manaText, text=f"Mana : {self.mana}")

    def changerMaxMana(self, nbr):
        self.maxMana += nbr

    def changerVie(self, nbr):
        if self.bouclier > 0:
            if self.bouclier + nbr >= 0:
                self.changerBouclier(nbr)
            else:
                self.vie += self.bouclier + nbr
                self.changerBouclier(-self.bouclier)
        else:
            self.vie += nbr
        self.canvas.itemconfig(self.vieText, text=f"Vie : {self.vie}")

    def changerBouclier(self, nbr):
        self.bouclier += nbr
        self.canvas.itemconfig(self.bouclierText, text=f"Bouclier : {self.bouclier}")

    # def changerNbrCarte(self, nbr):
    #     self.nbrCarte += nbr
    #     self.canvas.itemconfig(
    #         self.nbrCarteText, text=f"Nombre carte : {self.nbrCarte}"
    #     )

    # def changerRestCarteDeck(self, nbr):
    #     self.restCarteDeck += nbr
    #     self.canvas.itemconfig(
    #         self.restCarteDeckText, text=f"Carte restante : {self.restCarteDeck}"
    #     )

    def reloadDeck(self):
        # print(f"Longueur du deck de {tour} = {len(cardDeck)}")
        for i, card in enumerate(self.main):
            targetXPos = 40 + (155 * (i + 1)) + int(240 * 0.6) / 2
            xpos = card.xpos
            # print(
            #     f"position théorique : {targetXPos}, position réel : {xpos}, index = {i}, déplacement de {targetXPos - xpos}px"
            # )
            if xpos != targetXPos:
                card.move(targetXPos - xpos, 0)
                # print(f"xpos finale: {card.xpos}")
