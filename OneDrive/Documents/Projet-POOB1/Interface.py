import random
from classe_creature import Creature, Hero, Monstre, CATALOGUE_HEROS, CATALOGUE_MONSTRES
from armes import lancer_des, Arme, Action, CATALOGUE_ARMES
from fonctionnalites import choisir_meteo, appliquer_meteo, declencher_piege

print("Bienvenue dans le système de combat RPG")


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

