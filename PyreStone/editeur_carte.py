import tkinter as tk
from PIL import Image as Img, ImageTk as ImgTk
from constantes import *
import json


def editeur():
    def activeEditeurFrame():
        frameEditeur.pack()

    def desactiveEditeurFrame():
        frameEditeur.pack_forget()
        frameMenu.pack()

    def changerCarte(event=None):
        global image_element, image_monster
        selected_monster = listbox_monster.index(ANCHOR)
        selected_element = listbox_element.index(ANCHOR)
        if not entryNom.get():
            canvas.itemconfig(nomCarte, text=monsterFR[selected_monster])
        image_element = tk.PhotoImage(
            file=f"images/card_element/card_element_{element[selected_element]}.png"
        )
        image_monster = Img.open(
            f"images/monster/{monster[selected_monster]}_{element[selected_element]}.png"
        )
        image_monster = image_monster.resize(
            monsterSize[selected_monster], Img.ANTIALIAS
        )
        image_monster = ImgTk.PhotoImage(image_monster)
        canvas.itemconfig(elementImage, image=image_element)
        canvas.itemconfig(monsterImage, image=image_monster)

    def changerEffet(event=None):
        canvas.itemconfig(labelEffet, text=listbox_effet.get(ANCHOR))

    def changerCible(event=None):
        canvas.itemconfig(labelCible, text=listbox_cible.get(ANCHOR))

    def menu():
        desactiveEditeurFrame()

    def sauvegarderCard():
        # Nom
        if entryNom.get():
            nom = entryNom.get()
        else:
            nom = monsterFR[listbox_monster.index(ANCHOR)]
        # Vie
        vie = vieScale.get()
        # Cost
        cout = manaCost.get()
        # Attaque
        attaque = attaqueScale.get()
        # Element
        carteElement = element[listbox_element.index(ANCHOR)]
        # Monstre
        monstre = monster[listbox_monster.index(ANCHOR)]
        # Size
        size = monsterSize[listbox_monster.index(ANCHOR)]
        # Effet
        effet = listbox_effet.get(ANCHOR)
        # Cible
        cible = listbox_cible.get(ANCHOR)

        carte = {
            "nom": nom,
            "element": carteElement,
            "monstre": monstre,
            "size": size,
            "cout": cout,
            "vie": vie,
            "attaque": attaque,
            "effet": effet,
            "cible": cible,
        }

        if listbox_listCard.index(ANCHOR) == 0:
            with open("cartes.json", "r") as cartes:
                cartes_list = json.load(cartes)
                cartes_list.append(carte)

            with open("cartes.json", "w") as cartes:
                json.dump(cartes_list, cartes, indent=4)

            listbox_listCard.delete(0, END)
            listbox_listCard.insert(END, "Nouvelle Carte")
            for card in cartes_list:
                listbox_listCard.insert(tk.END, card["nom"])
            listbox_listCard.selection_anchor(END)
            listbox_listCard.selection_set(END)
        else:
            with open("cartes.json", "r") as cartes:
                cartes_list = json.load(cartes)
                index = listbox_listCard.index(ANCHOR)
                if listbox_listCard.get(ANCHOR) != carte["nom"]:
                    listbox_listCard.delete(index)
                    listbox_listCard.insert(index, carte["nom"])
                cartes_list[index - 1] =  carte

            with open("cartes.json", "w") as cartes:
                json.dump(cartes_list, cartes, indent=4)

    def deleteCard():
        if listbox_listCard.index(ANCHOR) != 0:
            with open("cartes.json", "r") as cartes:
                cartes_list = json.load(cartes)
                index = listbox_listCard.index(ANCHOR)
                listbox_listCard.delete(index)
                del cartes_list[index - 1]
                listbox_listCard.selection_anchor(0)
                listbox_listCard.selection_set(0)

            with open("cartes.json", "w") as cartes:
                json.dump(cartes_list, cartes, indent=4)

    def changerNom():
        if entryNom.get():
            canvas.itemconfig(nomCarte, text=entryNom.get())

    def changerCout(event=None):
        canvas.itemconfig(coutmana, text=manaCost.get())

    def changerVie(event=None):
        canvas.itemconfig(vieText, text=vieScale.get())
        canvas.itemconfig(vieText2, text=vieScale.get())
        canvas.itemconfig(vieText3, text=vieScale.get())

    def changerAttaque(event=None):
        canvas.itemconfig(attaqueText, text=attaqueScale.get())
        canvas.itemconfig(attaqueText2, text=attaqueScale.get())
        canvas.itemconfig(attaqueText3, text=attaqueScale.get())

    def selectCarte(event=None):
        if listbox_listCard.index(ANCHOR) != 0:
            carteIndex = listbox_listCard.index(ANCHOR) - 1
            with open("cartes.json", "r") as cartes:
                cards = json.load(cartes)
            carte = cards[carteIndex]
            ######################################
            # Carte
            if not carte["nom"] in monsterFR:
                entryNom.delete(0, END)
                entryNom.insert(0, carte["nom"])
            else:
                entryNom.delete(0, END)
            changerNom()
            ######################################
            # Configuration
            # Element
            listbox_element.select_clear(0, END)
            listbox_element.selection_anchor(element.index(carte["element"]))
            listbox_element.selection_set(element.index(carte["element"]))
            # Monstre
            listbox_monster.select_clear(0, END)
            listbox_monster.selection_anchor(monster.index(carte["monstre"]))
            listbox_monster.selection_set(monster.index(carte["monstre"]))
            changerCarte()
            # Mana
            manaCost.set(carte["cout"])
            changerCout()
            # Vie
            vieScale.set(carte["vie"])
            changerVie()
            # Attaque
            attaqueScale.set(carte["attaque"])
            changerAttaque()
            # Cible
            listbox_cible.select_clear(0, END)
            listbox_cible.selection_anchor(ciblesFR.index(carte["cible"]))
            listbox_cible.selection_set(ciblesFR.index(carte["cible"]))
            changerCible()
            # Effet
            listbox_effet.select_clear(0, END)
            listbox_effet.selection_anchor(effets.index(carte["effet"]))
            listbox_effet.selection_set(effets.index(carte["effet"]))
            changerEffet()
            ######################################
        else:
            ######################################
            # Carte
            entryNom.delete(0, END)
            changerNom()
            ######################################
            # Configuration
            # Element
            listbox_element.select_clear(0, END)
            listbox_element.selection_anchor(0)
            listbox_element.selection_set(0)
            # Monstre
            listbox_monster.select_clear(0, END)
            listbox_monster.selection_anchor(0)
            listbox_monster.selection_set(0)
            changerCarte()
            # Mana
            manaCost.set(1)
            changerCout()
            # Vie
            vieScale.set(1)
            changerVie()
            # Attaque
            attaqueScale.set(1)
            changerAttaque()
            # Cible
            listbox_cible.select_clear(0, END)
            listbox_cible.selection_anchor(0)
            listbox_cible.selection_set(0)
            changerCible()
            # Effet
            listbox_effet.select_clear(0, END)
            listbox_effet.selection_anchor(0)
            listbox_effet.selection_set(0)
            changerEffet()
            #######################################


    # Frame editeur carte
    frameEditeur = Frame(fenetre, width=1280, height=720)
    activeEditeurFrame()

    # Canvas editeur carte
    canvas = Canvas(
        frameEditeur, width=ecran_width, height=ecran_height, bg="lightgray"
    )
    canvas.pack(fill="both")

    # Monster Canvas
    monsterCanvas = Canvas(canvas, bg="gray")
    monsterCanvas.place(x=210, y=65)

    # Effet canvas
    effetCanvas = Canvas(canvas, bg="gray")
    effetCanvas.place(x=30, y=545)

    # Cible Canvas
    cibleCanvas = Canvas(canvas, bg="gray")
    cibleCanvas.place(x=240, y=545)

    # Liste_carte Canvas
    listCardCanvas = Canvas(canvas, bg="gray")
    listCardCanvas.place(x=470, y=65)

    # Lecture des images
    image_element = tk.PhotoImage(
        file=f"images/card_element/card_element_{element[0]}.png"
    )
    image_monster = Img.open(f"images/monster/{monster[0]}_{element[0]}.png")
    image_monster = image_monster.resize(monsterSize[0], Img.ANTIALIAS)
    image_monster = ImgTk.PhotoImage(image_monster)
    # Création des images dans le canvas
    elementImage = canvas.create_image(1050, 245, image=image_element)
    monsterImage = canvas.create_image(1050, 320, image=image_monster, anchor="s")

    box_element_monster = canvas.create_rectangle(
        20, 20, 440, 220, outline="black", width=3
    )
    name_element = canvas.create_text(
        30, 30, text="Element :", font=arial14, anchor="nw"
    )
    ligne_box_element_monster = canvas.create_line(205, 20, 205, 220)
    name_monster = canvas.create_text(
        210, 30, text="Monstre :", font=arial14, anchor="nw"
    )
    # Création de la liste d'élément
    listbox_element = tk.Listbox(
        canvas,
        width=15,
        height=len(element),
        selectbackground="gray",
        activestyle="none",
        cursor="hand2",
        font=arial14,
        exportselection=False,
        selectmode=SINGLE,
    )
    listbox_element.bind(
        "<<ListboxSelect>>", changerCarte
    )  # Lorsqu'une sélection est faites, effectué la fonction changerCarte
    listbox_element.place(x=30, y=65)

    # Création de la liste de monstre
    listbox_monster = tk.Listbox(
        monsterCanvas,
        width=18,
        height=6,
        selectbackground="gray",
        activestyle="none",
        cursor="hand2",
        font=arial14,
        exportselection=False,
        selectmode=SINGLE,
    )
    listbox_monster.bind(
        "<<ListboxSelect>>", changerCarte
    )  # Lorsqu'une sélection est faites, effectué la fonction changerCarte
    listbox_monster.pack(side="left", fill="y")

    # Scrollbar monster
    scrollMonsterList = tk.Scrollbar(
        monsterCanvas, orient="vertical", command=listbox_monster.yview
    )
    scrollMonsterList.pack(side="right", fill="y")
    listbox_monster.config(yscrollcommand=scrollMonsterList.set)

    # Définir la list d'élément
    for elem in elementFr:
        listbox_element.insert(tk.END, elem)
    listbox_element.selection_anchor(0)
    listbox_element.selection_set(first=0)
    # Définir la list de monstre
    for monstre in monsterFR:
        listbox_monster.insert(tk.END, monstre)
    listbox_monster.selection_anchor(0)
    listbox_monster.selection_set(first=0)

    # Label texte de la carte
    nomCarte = canvas.create_text(955, 140, text=monsterFR[0], font=arial14, anchor="w")

    # Nom carte
    entryNom = tk.Entry(canvas, font=arial14, width=15)
    entryNom.place(x=875, y=25)
    buttonNom = tk.Button(
        canvas,
        text="Définir Nom",
        width=23,
        cursor="hand2",
        font="Arial 10",
        command=changerNom,
    )
    buttonNom.place(x=1055, y=25)

    # Carac box
    carac_box = canvas.create_rectangle(20, 235, 440, 495, outline="black", width=3)
    carac_text = canvas.create_text(
        30, 245, text="Caractéristiques :", font=arial14, anchor="nw"
    )

    # Label texte du coût en mana
    coutmana = canvas.create_text(
        1049, 100, text="1", font=arial14, anchor="center", fill="white"
    )

    cost = StringVar()
    manaCost = tk.Scale(
        canvas,
        from_=1,
        to=10,
        orient="horizontal",
        length=390,
        width=12,
        label="Coût en mana :",
        variable=cost,
        command=changerCout,
        font="Arial 12",
    )
    manaCost.place(x=30, y=280)

    # Vie de la carte
    vieText = canvas.create_text(
        1144, 394, text="1", font="Arial 15", anchor="center", fill="black"
    )
    vieText3 = canvas.create_text(
        1146, 396, text="1", font="Arial 15", anchor="center", fill="black"
    )
    vieText2 = canvas.create_text(
        1145, 395, text="1", font="Arial 15", anchor="center", fill="white"
    )

    vie = StringVar()
    vieScale = tk.Scale(
        canvas,
        from_=1,
        to=100,
        orient="horizontal",
        length=390,
        width=12,
        label="Vie :",
        variable=vie,
        command=changerVie,
        font="Arial 12",
    )
    vieScale.place(x=30, y=350)

    # Attaque de la carte
    attaqueText = canvas.create_text(
        953, 395, text="1", font="Arial 18", anchor="center", fill="black"
    )
    attaqueText3 = canvas.create_text(
        955, 397, text="1", font="Arial 18", anchor="center", fill="black"
    )
    attaqueText2 = canvas.create_text(
        954, 396, text="1", font="Arial 18", anchor="center", fill="white"
    )

    attaque = StringVar()
    attaqueScale = tk.Scale(
        canvas,
        from_=1,
        to=20,
        orient="horizontal",
        length=390,
        width=12,
        label="Attaque :",
        variable=attaque,
        command=changerAttaque,
        font="Arial 12",
    )
    attaqueScale.place(x=30, y=420)

    # box effet
    box_effet = canvas.create_rectangle(20, 510, 440, 700, outline="black", width=3)
    box_effet_ligne = canvas.create_line(230, 520, 230, 690)
    effet_text = canvas.create_text(30, 520, text="Effet :", font=arial14, anchor="nw")
    cible_text = canvas.create_text(240, 520, text="Cible :", font=arial14, anchor="nw")

    # Label effet
    labelEffet = canvas.create_text(
        1050, 338, text=effets[0], font="Arial 14", anchor="center", fill="black"
    )

    # Label cible
    labelCible = canvas.create_text(
        1050, 358, text=ciblesFR[0], font="Arial 14", anchor="center", fill="black"
    )

    # Création de la liste effet
    listbox_effet = tk.Listbox(
        effetCanvas,
        width=14,
        height=6,
        selectbackground="gray",
        activestyle="none",
        cursor="hand2",
        font=arial14,
        exportselection=False,
        selectmode=SINGLE,
    )
    listbox_effet.bind("<<ListboxSelect>>", changerEffet)
    listbox_effet.pack(side="left", fill="y")

    # Scrollbar effet
    scrollEffetList = tk.Scrollbar(
        effetCanvas, orient="vertical", command=listbox_effet.yview
    )
    scrollEffetList.pack(side="right", fill="y")
    listbox_effet.config(yscrollcommand=scrollEffetList.set)

    # Définir la liste d'effet
    for effet in effets:
        listbox_effet.insert(tk.END, effet)
    listbox_effet.selection_anchor(0)
    listbox_effet.selection_set(first=0)

    # Création de la liste de cible
    listbox_cible = tk.Listbox(
        cibleCanvas,
        width=14,
        height=6,
        selectbackground="gray",
        activestyle="none",
        cursor="hand2",
        font=arial14,
        exportselection=False,
        selectmode=SINGLE,
    )
    listbox_cible.bind("<<ListboxSelect>>", changerCible)
    listbox_cible.pack(side="left", fill="y")

    # Scrollbar cible
    scrollCibleList = tk.Scrollbar(
        cibleCanvas, orient="vertical", command=listbox_cible.yview
    )
    scrollCibleList.pack(side="right", fill="y")
    listbox_cible.config(yscrollcommand=scrollCibleList.set)

    # Définir la liste de cible
    for cible in ciblesFR:
        listbox_cible.insert(tk.END, cible)
    listbox_cible.selection_anchor(0)
    listbox_cible.selection_set(first=0)

    # Bouton menu
    buttonMenu = Button(
        canvas, text="Menu", width=16, cursor="hand2", font="Arial 12", command=menu
    )
    buttonMenu.place(x=975, y=660)

    # Bouton sauvegarder
    buttonSave = Button(
        canvas,
        text="Sauvegarder",
        width=16,
        cursor="hand2",
        font="Arial 12",
        command=sauvegarderCard,
    )
    buttonSave.place(x=465, y=660)

    # Bouton supprimer
    buttonDelete = Button(
        canvas, text="Supprimer",
        width=16,
        cursor="hand2",
        font="Arial 12",
        command=deleteCard,
    )
    buttonDelete.place(x=640, y=660)

    #####################################################################
    # Partie récupération de la base de donnée carte
    # Rectangle liste de cartes
    rect_listCard = canvas.create_rectangle(455, 20, 800, 700, outline="black", width=3)
    effet_text = canvas.create_text(
        465, 30, text="Liste de carte :", font=arial14, anchor="nw"
    )

    # Création de la liste de carte
    listbox_listCard = tk.Listbox(
        listCardCanvas,
        width=27,
        height=12,
        selectbackground="gray",
        activestyle="none",
        cursor="hand2",
        font=arial14,
        exportselection=False,
        selectmode=SINGLE,
    )
    listbox_listCard.bind("<<ListboxSelect>>", selectCarte)
    listbox_listCard.pack(side="left", fill="y")

    # Scrollbar liste de carte
    scrollListCardList = tk.Scrollbar(
        listCardCanvas, orient="vertical", command=listbox_listCard.yview
    )
    scrollListCardList.pack(side="right", fill="y")
    listbox_listCard.config(yscrollcommand=scrollListCardList.set)

    # Définir la liste de cible
    with open("cartes.json", "r") as cartes:
        cards = json.load(cartes)
        listbox_listCard.insert(END, "Nouvelle Carte")
        for card in cards:
            listbox_listCard.insert(END, card["nom"])
    listbox_listCard.selection_anchor(0)
    listbox_listCard.selection_set(first=0)

    #####################################################################

    fenetre.mainloop()
