import random

print("Bienvenue dans le système de combat RPG")


def lancer_des(nb_des, faces):
    total = 0
    for i in range(nb_des):
        total += random.randint(1, faces)
    return total


def saisir_entier(message, min_val, max_val):
    while True:
        try:
            valeur = int(input(message))
            if valeur >= min_val and valeur <= max_val:
                return valeur
            else:
                print("Entrez un nombre entre", min_val, "et", max_val)
        except ValueError:
            print("Entrez un nombre valide.")


def choisir_meteo():
    meteo = random.choice(list(METEOS.keys()))
    print("\nMétéo du combat :", meteo)
    effets = METEOS[meteo]
    for type_degats, bonus in effets.items():
        if bonus > 0:
            print(" +", bonus, "dégâts pour les attaques de type", type_degats)
        else:
            print(" ", bonus, "dégâts pour les attaques de type", type_degats)
    return meteo


def appliquer_meteo(degats, type_degats, meteo):
    effets = METEOS[meteo]
    if type_degats in effets:
        bonus = effets[type_degats]
        degats = degats + bonus
        if bonus > 0:
            print("La météo booste les dégâts de", bonus, "!")
        else:
            print("La météo réduit les dégâts de", abs(bonus), ".")
    if degats < 1:
        degats = 1
    return degats


def declencher_piege(toutes_creatures):
    jet = lancer_des(1, 6)
    if jet == 6:
        creatures_vivantes = []
        for c in toutes_creatures:
            if c.est_vivant():
                creatures_vivantes.append(c)
        cible = random.choice(creatures_vivantes)
        degats = lancer_des(1, 6)
        cible.pv = cible.pv - degats
        print("\nPiège !", cible.nom, "tombe dans un piège et subit",
              degats, "dégâts. PV restants :", cible.pv)


METEOS = {
    "Soleil":  {"Feu": 2, "Glace": -2},
    "Pluie":   {"Feu": -2, "Perçant": 1},
    "Orage":   {"Magique": 2, "Feu": -1},
    "Neige":   {"Tranchant": 1, "Feu": -3},
}


class Creature:

    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.actions = []
        self.initiative = 0
        self.resistances = []

    def est_vivant(self):
        return self.pv > 0


class Hero(Creature):

    def __init__(self, nom, description, pv, defense, arme):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = arme.type_degats
        self.actions = []
        self.initiative = 0
        self.resistances = []
        self.arme = arme

    def afficher_caracteristiques(self):
        print("\n--- HÉROS ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.type_degats)
        print("Arme :", self.arme.nom)


class Monstre(Creature):

    def __init__(self, nom, description, pv, defense, type_degats, nb_des, faces, resistances=None):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.actions = []
        self.initiative = 0
        self.nb_des = nb_des
        self.faces = faces
        if resistances is None:
            resistances = []
        self.resistances = resistances

    def afficher_caracteristiques(self):
        print("\n--- MONSTRE ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.type_degats)
        print("Résistances :", self.resistances)


class Arme:

    def __init__(self, nom, nb_des, faces, type_degats):
        self.nom = nom
        self.nb_des = nb_des
        self.faces = faces
        self.type_degats = type_degats

    def lancer_degats(self):
        return lancer_des(self.nb_des, self.faces)


class Action:

    def __init__(self, nom):
        self.nom = nom


CATALOGUE_ARMES = [
    Arme("Epée", 1, 8, "Tranchant"),
    Arme("Dague", 1, 4, "Perçant"),
    Arme("Hache", 2, 6, "Tranchant"),
    Arme("Arc", 1, 8, "Perçant"),
    Arme("Marteau", 2, 6, "Contondant"),
    Arme("Bâton", 1, 6, "Magique"),
]

CATALOGUE_MONSTRES = [
    Monstre("Gobelin", "Petite créature rusée", 18, 9, "Perçant", 1, 4),
    Monstre("Squelette", "Guerrier mort-vivant", 25, 10, "Tranchant", 1, 6),
    Monstre("Dragon", "Seigneur des flammes", 60, 16, "Feu", 3, 8, ["Feu"]),
    Monstre("Loup", "Bête sauvage agile", 22, 10, "Tranchant", 1, 6),
]

CATALOGUE_HEROS = [
    {"nom": "Guerrier", "description": "Brave combattant proche du corps à corps",
        "pv": 35, "defense": 12},
    {"nom": "Magicien", "description": "Maître de la magie offensive",
        "pv": 25, "defense": 10},
    {"nom": "Archer", "description": "Expert du combat à distance",
        "pv": 28, "defense": 11},
    {"nom": "Paladin", "description": "Guerrier sacré protecteur",
        "pv": 40, "defense": 14},
    {"nom": "Assassin", "description": "Combattant furtif et rapide",
        "pv": 26, "defense": 13},
]

nb_heros = saisir_entier(
    "Combien de héros vont combattre ? ", 1, len(CATALOGUE_HEROS))

heros = []

for i in range(nb_heros):
    print("\nHéros", i + 1)

    for j, hero in enumerate(CATALOGUE_HEROS, 1):
        print(j, "-", hero["nom"], "-", hero["description"],
              "- PV:", hero["pv"], "- Défense:", hero["defense"])

    choix = saisir_entier("Choisissez un héros : ", 1, len(CATALOGUE_HEROS))
    hero_choisi = CATALOGUE_HEROS[choix - 1]

    for j, arme in enumerate(CATALOGUE_ARMES, 1):
        print(j, "-", arme.nom, "-", arme.nb_des,
              "d", arme.faces, "-", arme.type_degats)

    choix_arme = saisir_entier(
        "Choisissez une arme : ", 1, len(CATALOGUE_ARMES))
    arme_choisie = CATALOGUE_ARMES[choix_arme - 1]

    hero = Hero(hero_choisi["nom"], hero_choisi["description"],
                hero_choisi["pv"], hero_choisi["defense"], arme_choisie)
    heros.append(hero)

nb_monstres = saisir_entier(
    "Combien de monstres vont combattre ? ", 1, len(CATALOGUE_MONSTRES))

monstres = []

for i in range(nb_monstres):
    print("\nMonstre", i + 1)

    for j, monstre in enumerate(CATALOGUE_MONSTRES, 1):
        print(j, "-", monstre.nom, "-", monstre.description,
              "- PV:", monstre.pv, "- Défense:", monstre.defense)

    choix = saisir_entier("Choisissez un monstre : ",
                          1, len(CATALOGUE_MONSTRES))
    monstre_choisi = CATALOGUE_MONSTRES[choix - 1]
    monstres.append(monstre_choisi)

print("\n--- INITIATIVE ---")

for hero in heros:
    hero.initiative = lancer_des(1, 20)
    print(hero.nom, ":", hero.initiative)

for monstre in monstres:
    monstre.initiative = lancer_des(1, 20)
    print(monstre.nom, ":", monstre.initiative)

toutes_creatures = heros + monstres

for i in range(len(toutes_creatures) - 1):
    for j in range(i + 1, len(toutes_creatures)):
        if toutes_creatures[j].initiative > toutes_creatures[i].initiative:
            temp = toutes_creatures[i]
            toutes_creatures[i] = toutes_creatures[j]
            toutes_creatures[j] = temp

print("\n--- ORDRE DE JEU ---")
for creature in toutes_creatures:
    print(creature.nom, ":", creature.initiative)

meteo = choisir_meteo()

print("\n--- COMBAT ---")

combat_en_cours = True

while combat_en_cours:
    print("\n--- Nouveau round ---")
    declencher_piege(toutes_creatures)

    for creature in toutes_creatures:
        if creature.est_vivant():
            print("\nC'est au tour de", creature.nom)
            print("1 - Attaque")
            print("2 - Soin")
            print("3 - Buff (augmente la défense d'un allié de +3)")
            print("4 - Debuff (réduit la défense d'un ennemi de -3)")
            choix_action = saisir_entier("Choisissez une action : ", 1, 4)

            if choix_action == 1:
                print("\nChoisissez une cible :")
                if creature in heros:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]
                else:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]

                jet = lancer_des(1, 20)
                print(creature.nom, "lance 1d20 :", jet)

                if creature in heros:
                    degats_normaux = creature.arme.lancer_degats()
                else:
                    degats_normaux = lancer_des(
                        creature.nb_des, creature.faces)

                degats_normaux = appliquer_meteo(
                    degats_normaux, creature.type_degats, meteo)

                if jet == 1:
                    creature.pv = creature.pv - degats_normaux
                    print("Echec critique !", creature.nom, "se blesse pour",
                          degats_normaux, "dégâts. PV restants :", creature.pv)

                elif jet == 20:
                    degats = degats_normaux * 2
                    if creature.type_degats in cible.resistances:
                        degats = degats // 2
                        print("Résistance !", cible.nom,
                              "résiste et ne subit que", degats, "dégâts.")
                    cible.pv = cible.pv - degats
                    print("Réussite critique !", cible.nom, "subit",
                          degats, "dégâts. PV restants :", cible.pv)

                elif jet > cible.defense:
                    if creature.type_degats in cible.resistances:
                        degats_normaux = degats_normaux // 2
                        print("Résistance !", cible.nom,
                              "résiste et ne subit que", degats_normaux, "dégâts.")
                    cible.pv = cible.pv - degats_normaux
                    print("Touché !", cible.nom, "subit", degats_normaux,
                          "dégâts. PV restants :", cible.pv)

                else:
                    print("Raté ! Le jet", jet, "est inférieur à la défense de",
                          cible.nom, "(", cible.defense, ")")

            elif choix_action == 2:
                print("\nChoisissez une cible à soigner :")
                if creature in heros:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]
                else:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]

                soin = lancer_des(2, 8)
                cible.pv = cible.pv + soin
                print(creature.nom, "soigne", cible.nom, "de",
                      soin, "PV. PV restants :", cible.pv)

            elif choix_action == 3:
                print("\nChoisissez un allié à booster :")
                if creature in heros:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]
                else:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]

                cible.defense = cible.defense + 3
                print(creature.nom, "booste la défense de", cible.nom,
                      "de +3. Défense maintenant :", cible.defense)

            elif choix_action == 4:
                print("\nChoisissez un ennemi à affaiblir :")
                if creature in heros:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]
                else:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]

                cible.defense = cible.defense - 3
                print(creature.nom, "affaiblit la défense de", cible.nom,
                      "de -3. Défense maintenant :", cible.defense)

    heros_vivants = 0
    for hero in heros:
        if hero.est_vivant():
            heros_vivants += 1

    monstres_vivants = 0
    for monstre in monstres:
        if monstre.est_vivant():
            monstres_vivants += 1

    if heros_vivants == 0:
        print("\nDéfaite ! Tous les héros sont morts.")
        combat_en_cours = False

    elif monstres_vivants == 0:
        print("\nVictoire ! Tous les monstres sont vaincus !")
        combat_en_cours = False