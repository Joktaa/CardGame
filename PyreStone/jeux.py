from tkinter import *
import random
from PIL import Image as Img, ImageTk as ImgTk
from joueur import *
from constantes import *
from math import ceil
import json

card_selected = False
canChange = True
solo = False
tour = "j1"

########################################################################################################################################
def jeux(soloGame=False):
    # Var
    global card_selected, canChange, tour, solo

    if soloGame:
        solo = True
    else:
        solo = False

    # Classe carte
    class card:
        selected = False

        def __init__(
            self,
            window,
            xpos,
            ypos,
            element,
            monster,
            monsterSize,
            name,
            cost,
            life,
            attack,
            effet,
            cible,
            scale,
            joueur,
        ):
            self.joueur = joueur
            self.scale = scale
            if joueur == "j1":
                self.xpos, self.ypos = xpos, 610 if not ypos else ypos
            else:
                self.xpos, self.ypos = xpos, 110 if not ypos else ypos
            self.canvas = Canvas(
                window, width=int(240 * self.scale), height=int(348 * self.scale)
            )
            self.window = window
            self.windowCanvas = window.create_window(
                self.xpos, self.ypos, window=self.canvas
            )
            self.life = life
            self.attack = attack
            self.cost = cost
            self.name = name
            self.element = element
            self.monster = monster
            self.effet = effet
            self.cible = cible
            # Image element
            self.imageElement = Img.open(f"images/card_element/card_element_{element}.png")
            self.imageElement = self.imageElement.resize(
                (int(240 * self.scale), int(348 * self.scale)), Img.ANTIALIAS
            )
            self.imageElement = ImgTk.PhotoImage(self.imageElement)
            self.elementImage = self.canvas.create_image(
                int(120 * self.scale + 2),
                int(174 * self.scale + 2),
                image=self.imageElement,
            )
            # Image monstre redimentionné
            self.imageMonster = Img.open(f"images/monster/{monster}_{element}.png")
            self.imageMonster = self.imageMonster.resize(
                (int(monsterSize[0] * self.scale), int(monsterSize[1] * self.scale)),
                Img.ANTIALIAS,
            )
            self.imageMonster = ImgTk.PhotoImage(self.imageMonster)
            self.monsterImage = self.canvas.create_image(
                int(120 * self.scale + 2),
                int(249 * self.scale + 2),
                image=self.imageMonster,
                anchor="s",
            )
            # Vie de la carte
            if self.life >= 100:
                self.vieText = self.canvas.create_text(
                    int(214 * self.scale + 1),
                    int(323 * self.scale + 3),
                    text=self.life,
                    font="Arial 14",
                    anchor="center",
                    fill="black",
                )
                self.vieText3 = self.canvas.create_text(
                    int(216 * self.scale + 1),
                    int(325 * self.scale + 3),
                    text=self.life,
                    font="Arial 14",
                    anchor="center",
                    fill="black",
                )
                self.vieText2 = self.canvas.create_text(
                    int(215 * self.scale + 1),
                    int(324 * self.scale + 3),
                    text=self.life,
                    font="Arial 14",
                    anchor="center",
                    fill="white",
                )
            else:
                self.vieText = self.canvas.create_text(
                    int(214 * self.scale + 3),
                    int(323 * self.scale + 3),
                    text=self.life,
                    font="Arial 14",
                    anchor="center",
                    fill="black",
                )
                self.vieText3 = self.canvas.create_text(
                    int(216 * self.scale + 3),
                    int(325 * self.scale + 3),
                    text=self.life,
                    font="Arial 14",
                    anchor="center",
                    fill="black",
                )
                self.vieText2 = self.canvas.create_text(
                    int(215 * self.scale + 3),
                    int(324 * self.scale + 3),
                    text=self.life,
                    font="Arial 14",
                    anchor="center",
                    fill="white",
                )
            # Attaque de la carte
            self.attaqueText = self.canvas.create_text(
                int(23 * self.scale + 2),
                int(323 * self.scale + 3),
                text=self.attack,
                font="Arial 16",
                anchor="center",
                fill="black",
            )
            self.attaqueText3 = self.canvas.create_text(
                int(25 * self.scale + 2),
                int(325 * self.scale + 3),
                text=self.attack,
                font="Arial 16",
                anchor="center",
                fill="black",
            )
            self.attaqueText2 = self.canvas.create_text(
                int(24 * self.scale + 2),
                int(324 * self.scale + 3),
                text=self.attack,
                font="Arial 16",
                anchor="center",
                fill="white",
            )
            self.nameText = self.canvas.create_text(
                int(28 * self.scale + 2),
                int(67 * self.scale + 3),
                text=name,
                font="Arial 10",
                anchor="w",
            )
            self.costText = self.canvas.create_text(
                int(119 * self.scale + 2),
                int(30 * self.scale + 2),
                text=cost,
                font="Arial 13",
                fill="white",
            )

            # Effet de la carte
            self.labelEffet = self.canvas.create_text(
                72, 165, text=self.effet, font="Arial 12", anchor="center", fill="black"
            )

            # Cible de la carte
            self.labelCible = self.canvas.create_text(
                72, 185, text=self.cible, font="Arial 10", anchor="center", fill="black"
            )

            self.canvas.bind("<Button-1>", self.start)
            self.outline = None

        def set_selection(self):
            if self.selected:
                self.outline = self.canvas.create_rectangle(
                    3,
                    3,
                    int(240 * self.scale),
                    int(348 * self.scale),
                    outline="yellow",
                    width=6,
                )
            else:
                if self.outline:
                    return self.canvas.delete(self.outline)

        def start(self, event):
            global card_selected, tour
            if (not self in joueur1.main) and (not self in joueur2.main):
                if self.joueur == tour:
                    if self.joueur == "j1":
                        main = cardJ1
                    else:
                        main = cardJ2

                    if self.selected:
                        self.selected = False
                        card_selected = False
                        self.set_selection()
                    else:
                        for card in main:
                            if card.selected:
                                card.selected = False
                                card_selected = False
                                card.set_selection()

                        self.selected = True
                        card_selected = True
                        self.set_selection()

        def move(self, x, y):
            self.window.move(self.windowCanvas, x, y)
            self.xpos = self.xpos + x
            self.ypos = self.ypos + y

        def moveTo(self, x, y, time=0):
            targetX = x - self.xpos
            targetY = y - self.ypos
            if time:
                for i in range(time):
                    self.window.after(1, self.move(targetX / time, targetY / time))
                    self.window.update()
            else:
                self.move(targetX, targetY)

        def delete(self):
            self.window.delete(self.windowCanvas)

        def changerVie(self, nbr):
            self.life += nbr
            self.canvas.itemconfig(self.vieText, text=self.life)
            self.canvas.itemconfig(self.vieText2, text=self.life)
            self.canvas.itemconfig(self.vieText3, text=self.life)
            if self.life <= 0:
                if self.joueur == "j1":
                    joueur1.main.remove(self)
                    self.delete()
                    joueur1.reloadDeck()
                else:
                    joueur2.main.remove(self)
                    self.delete()
                    joueur2.reloadDeck()

        def changerAttaque(self, nbr):
            self.attack += nbr
            self.canvas.itemconfig(self.attaqueText, text=self.attack)
            self.canvas.itemconfig(self.attaqueText2, text=self.attack)
            self.canvas.itemconfig(self.attaqueText3, text=self.attack)

        def changerEffet(self, effet):
            self.effet = effet
            self.canvas.itemconfig(self.labelEffet, text=effet)

        # METHODE
        def attaquer(self, cible):
            if isinstance(cible, joueur):
                cible.changerVie(-self.attack)
            else:
                cible.changerVie(-self.boost(cible))

        def soigner(self, cible):
            cible.changerVie(self.attack)

        def defendre(self, cible):
            if isinstance(cible, joueur):
                cible.changerBouclier(self.attack)

        def defausser(self, cible):
            pass

        def agit(self, joueur, joueurEnnemi):
            if self.cible == "Une carte":
                tempX, tempY = self.xpos, self.ypos

                # ATTAQUER
                if self.effet == "Attaquer":
                    if len(joueurEnnemi.main) > 0:
                        target = random.choice(joueurEnnemi.main)
                    else:
                        target = joueurEnnemi
                    self.moveTo(target.xpos, target.ypos, 30)
                    self.attaquer(target)

                # SOIGNER
                elif self.effet == "Soigner":
                    if len(joueur.main) > 1:
                        target = random.choice(joueur.main)
                    else:
                        target = joueur
                    self.moveTo(target.xpos, target.ypos, 30)
                    self.soigner(target)

                # DEFENDRE
                elif self.effet == "Defendre":
                    target = joueur
                    self.moveTo(target.xpos, target.ypos, 30)
                    self.defendre(target)

                # PIOCHER
                elif self.effet == "Piocher":
                    piocher(self.joueur)
                    self.changerEffet("Attaquer")

                # DEFAUSSER
                elif self.effet == "Defausser":
                    if self.joueur == "j1":
                        joueur = "j2"
                        main = cardJ2
                    else:
                        joueur = "j1"
                        main = cardJ1
                    deleteCarte(joueur, random.randint(0, len(main) - 1))
                    self.changerEffet("Attaquer")

                self.moveTo(tempX, tempY, 40)

            elif self.cible == "Toute les carte":
                tempX, tempY = self.xpos, self.ypos

                # ATTAQUER
                if self.effet == "Attaquer":
                    if len(joueurEnnemi.main) > 0:
                        target = joueurEnnemi.main
                        if self.joueur == "j1":
                            self.moveTo(600, 110, 30)
                        else:
                            self.moveTo(600, 610, 30)

                        for cible in target:
                            self.attaquer(cible)
                    else:
                        target = joueurEnnemi
                        self.moveTo(target.xpos, target.ypos, 30)
                        self.attaquer(target)

                # SOIGNER
                elif self.effet == "Soigner":
                    if len(joueur.main) > 1:
                        target = joueur.main
                        if self.joueur == "j1":
                            self.moveTo(600, 610, 30)
                        else:
                            self.moveTo(600, 110, 30)

                        for cible in target:
                            self.soigner(cible)
                    else:
                        target = joueur
                        self.moveTo(target.xpos, target.ypos, 30)
                        self.soigner(target)

                # DEFENDRE
                elif self.effet == "Defendre":
                    target = joueur
                    self.moveTo(target.xpos, target.ypos, 30)
                    self.defendre(target)

                # PIOCHER
                elif self.effet == "Piocher":
                    piocher(self.joueur)
                    self.changerEffet("Attaquer")
                
                # DEFAUSSER
                elif self.effet == "Defausser":
                    if self.joueur == "j1":
                        joueur = "j2"
                        main = cardJ2
                    else:
                        joueur = "j1"
                        main = cardJ1

                    for i in range(len(main)):
                        deleteCarte(joueur, 0)
                    self.changerEffet("Attaquer")

                self.moveTo(tempX, tempY, 40)

        def boost(self, cible):
            if self.element == cible.element:
                return self.attack

            elif self.element == "fire":
                if cible.element == "wind":
                    return ceil(self.attack * 1.5)
                elif cible.element == "water":
                    return ceil(self.attack * 0.5)

            elif self.element == "wind":
                if cible.element == "water":
                    return ceil(self.attack * 1.5)
                elif cible.element == "fire":
                    return ceil(self.attack * 0.5)

            elif self.element == "water":
                if cible.element == "fire":
                    return ceil(self.attack * 1.5)
                elif cible.element == "wind":
                    return ceil(self.attack * 0.5)
#######################################################################################################################################
    def activeJeuxFrame():
        frameJeux.pack()

    def desactiveJeuxFrame():
        frameJeux.pack_forget()
        frameMenu.pack()

    def menu():
        desactiveJeuxFrame()

    def endGame(joueur):
        for widget in frameJeux.winfo_children():
            widget.destroy()

        frameJeux.config(bg="#33ACFF")
        
        gagnant = Label(
            frameJeux, text=f"BRAVO !! Le joueur {joueur} a gagné", font=("arial", 20, "bold"), bg="gray"
        )
        gagnant.place(x=460, y=100)

        menuButton = Button(
            frameJeux,
            text="Retour Menu",
            anchor="center",
            bg="#C44408",
            fg="#FFF",
            width=16,
            height=1,
            font=("arial", 22, "bold"),
            activebackground="#A73A07",
            activeforeground="#FFF",
            cursor="hand2",
            command=menu,
        )
        menuButton.place(x=500, y=550)

    def passerTour():
        global tour, canChange
        if canChange:
            canChange = False
            joueurJeux()
            if tour == "j1":
                tour = "j2"
                if joueur2.maxMana < 10:
                    joueur2.changerMaxMana(1)
                    joueur2.changerMana(-joueur2.mana + joueur2.maxMana)
                else:
                    joueur2.changerMana(-joueur2.mana + joueur2.maxMana)
                for card in cardJ1:
                    card.selected = False
                    card.set_selection()
                    for i in range(10):
                        canvas.after(2, card.move(0, 25))
                        canvas.update()
                canvas.move(BlockJ1, 0, 250)
                for block in emplacementJ1:
                    canvas.move(block, 0, 250)
                for card in joueur1.main:
                    card.move(0, 250)
                for block in emplacementJ2:
                    canvas.move(block, 0, 250)
                for card in joueur2.main:
                    card.move(0, 250)
                canvas.move(BlockJ2, 0, 250)
                for card in cardJ2:
                    for i in range(10):
                        canvas.after(2, card.move(0, 25))
                        canvas.update()
                canvas.after(200, reloadDeck())
                piocher()
                if solo:
                    return jouerIA()
            else:
                tour = "j1"
                if joueur1.maxMana < 10:
                    joueur1.changerMaxMana(1)
                    joueur1.changerMana(-joueur1.mana + joueur1.maxMana)
                else:
                    joueur1.changerMana(-joueur1.mana + joueur1.maxMana)
                for card in cardJ2:
                    card.selected = False
                    card.set_selection()
                    for i in range(10):
                        canvas.after(2, card.move(0, -25))
                        canvas.update()
                canvas.move(BlockJ2, 0, -250)
                for block in emplacementJ2:
                    canvas.move(block, 0, -250)
                for card in joueur2.main:
                    card.move(0, -250)
                for block in emplacementJ1:
                    canvas.move(block, 0, -250)
                for card in joueur1.main:
                    card.move(0, -250)
                canvas.move(BlockJ1, 0, -250)
                for card in cardJ1:
                    for i in range(10):
                        canvas.after(2, card.move(0, -25))
                        canvas.update()
                canvas.after(200, reloadDeck())
                piocher()
            canChange = True

    def jouerIA():
        global canChange
        for card in cardJ2:
            if len(joueur2.main) < 6:
                if card.cost <= joueur2.mana:
                    card.selected = True
                    card.set_selection()
                    jouerCarte()
        canChange = True
        return passerTour()

    def joueurJeux():
        global tour
        if tour == "j1":
            joueur = joueur1
            joueurEnnemi = joueur2
        else:
            joueur = joueur2
            joueurEnnemi = joueur1

        if len(joueur.main) > 0:
            for card in joueur.main:
                card.agit(joueur, joueurEnnemi)
                if joueur1.vie <= 0:
                    endGame("2")
                elif joueur2.vie <= 0:
                    endGame("1")                    


    def piocher(joueur=None):
        global tour
        if not joueur:
            if tour == "j1":
                cardDeck = cardJ1
            else:
                cardDeck = cardJ2
        else:
            if joueur == "j1":
                cardDeck = cardJ1
            elif joueur == "j2":
                cardDeck = cardJ2

        if len(cardDeck) < 7:
            with open("cartes.json", "r") as cartes:
                carte_list = json.load(cartes)
            carte = random.choice(carte_list)
            cardDeck.append(
                card(
                    canvas,
                    150 * (len(cardDeck) + 1.9),
                    0 if joueur == "j1" and tour == "j1" else -140 if joueur == "j2" and tour == "j1" else 0,
                    carte["element"],
                    carte["monstre"],
                    carte["size"],
                    carte["nom"],
                    carte["cout"],
                    carte["vie"],
                    carte["attaque"],
                    carte["effet"],
                    carte["cible"],
                    0.6,
                    tour if not joueur else joueur,
                )
            )
        else:
            deleteCarte(tour if not joueur else joueur, 0)
            reloadDeck(0 if not joueur else joueur)
            piocher(tour if not joueur else joueur)
        setTextInfo("Pioche !")


    def reloadDeck(joueur=None):
        global tour
        if not joueur:
            if tour == "j1":
                cardDeck = cardJ1
            else:
                cardDeck = cardJ2
        else:
            if joueur == "j1":
                cardDeck = cardJ1
            elif joueur == "j2":
                cardDeck = cardJ2

        # print(f"Longueur du deck de {tour} = {len(cardDeck)}")
        for i, card in enumerate(cardDeck):
            targetXPos = 150 * (i + 1.9)
            xpos = card.xpos
            # print(
            #     f"position théorique : {targetXPos}, position réel : {xpos}, index = {i}, déplacement de {targetXPos - xpos}px"
            # )
            if xpos != targetXPos:
                card.move(targetXPos - xpos, 0)
                # print(f"xpos finale: {card.xpos}")


    def deleteCarte(joueur=-1, index=-1):
        if joueur == -1 and index == -1:
            if tour == "j1":
                cardDeck = cardJ1
            else:
                cardDeck = cardJ2

            for i, card in enumerate(cardDeck):
                if card.selected:
                    card.delete()
                    cardDeck.pop(i)
                    return reloadDeck()
            return setTextInfo("Aucune sélection !")
        else:
            if joueur == "j1":
                cardDeck = cardJ1
            else:
                cardDeck = cardJ2

            if len(cardDeck) > 0:
                cardDeck[index].delete()
                cardDeck.pop(index)
                return reloadDeck()
            else:
                return setTextInfo("Pas de cartes !")
            

    def jouerCarte():
        global card_selected, tour
        if tour == "j1":
            cardDeck = cardJ1
            joueur = joueur1
            joueurEnnemi = joueur2
        else:
            cardDeck = cardJ2
            joueur = joueur2
            joueurEnnemi = joueur1

        for i, card in enumerate(cardDeck):
            if card.selected:
                if card.cost <= joueur.mana:
                    if len(joueur.main) < 6:
                        joueur.main.append(card)
                        if tour == "j1":
                            card.moveTo(
                                40 + (155 * len(joueur.main)) + int(240 * 0.6) / 2,
                                260 + int(348 * 0.6) / 2,
                            )
                        else:
                            card.moveTo(
                                40 + (155 * len(joueur.main)) + int(240 * 0.6) / 2,
                                270 + int(348 * 0.6) / 2,
                            )
                        cardDeck.pop(i)
                        card.selected = False
                        card.set_selection()
                        card_selected = False
                        joueur.changerMana(-card.cost)
                        reloadDeck()
                        if card.effet == "Piocher":
                            card.agit(joueur, joueurEnnemi)
                    else:
                        return setTextInfo("Trop de cartes !")
                else:
                    return setTextInfo("Mana Insuffisant !")
        return setTextInfo("Aucune sélection !")


    def setTextInfo(text, time=350):
        canvas.itemconfig(textInfo, text=text)
        canvas.update()
        canvas.after(time, canvas.itemconfig(textInfo, text=""))
        canvas.update()


    def createRectangle(x, y, size, fill):
        return canvas.create_rectangle(x, y, x + size[0], y + size[1], fill=fill)

    ##########################################################################################################################################
    # Frame jeux
    frameJeux = Frame(fenetre, width=1280, height=720)
    activeJeuxFrame()

    canvas = Canvas(frameJeux, width=1280, height=720, bg="lightgray")
    canvas.pack()

    # Infos
    BlockJ1 = canvas.create_rectangle(195, 490, 1270, 720, outline="black", width=3)
    BlockJ2 = canvas.create_rectangle(
        195, 0 - 250, 1270, 230 - 250, outline="black", width=3
    )
    blockTextInfo = canvas.create_rectangle(
        5, 384, 180, 410, outline="black", width=3
    )
    textInfo = canvas.create_text(
        10, 397, text="", font="Arial 14", anchor="w", fill="black"
    )

    # Emplacement jeux / Plateau joueur
    emplacementJ1, emplacementJ2 = [], []
    for i in range(6):
        posX = 40 + (155 * (i + 1))
        emplacementJ1.append(
            createRectangle(posX, 260, (int(240 * 0.6), int(348 * 0.6)), "gray")
        )
        emplacementJ2.append(
            createRectangle(posX, 20, (int(240 * 0.6), int(348 * 0.6)), "gray")
        )

    joueur1 = joueur(canvas, 90, 615, 50, 1, [], "Joueur 1")
    joueur2 = joueur(canvas, 90, 105, 50, 0, [], "Joueur 2")

    buttonTour = Button(
        canvas, text="Finir tour", font="Arial 14", width=12, command=passerTour
    )
    buttonTour.place(x=1130, y=260)
    buttonKill = Button(
        canvas, text="Détruire carte", font="Arial 14", width=12, command=deleteCarte
    )
    buttonKill.place(x=1130, y=310)
    buttonPlayCard = Button(
        canvas, text="Joueur carte", font="Arial 14", width=12, command=jouerCarte
    )
    buttonPlayCard.place(x=1130, y=360)
    buttonQuit = Button(
        canvas, text="Retour Menu !", font="Arial 14", width=12, command=menu
    )
    buttonQuit.place(x=10, y=320)

    cardJ1, cardJ2 = [], []

    for i in range(2):
        piocher("j1")
        piocher("j2")