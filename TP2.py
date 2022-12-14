"""
Programme fait par Lily Qian
Groupe: 403
Description: un jeu qui te permet à deviner un chiffre aléatoirement généré par l'ordinateur
"""
import random


def choix_de_bornes():
    """
    Cette fonction sert à permettre au joueur de définir les bornes
    """
    global borne_minimale, borne_maximale
    borne_minimale = int(input('Entrez le nombre minimale :'))
    borne_maximale = int(input('Entrez le nombre maximale :'))


choix_de_bornes()
chiffre_aleatoire = random.randint(borne_minimale, borne_maximale)
jeu = True
nbr_essais_total = 0


def nbr_essais_addition():
    """
    Cette fonction sert à pouvoir montrer le nombre d'essais à la fin du jeu
    """
    global nbr_essais_total
    nbr_essais_total += 1


print(f"J'ai choisi un nombre entre {borne_minimale} et {borne_maximale}. À vous de deviner...")

while jeu:
    essai = int(input("Entrez votre essai :"))

    if essai == chiffre_aleatoire:
        nbr_essais_addition()
        reponse = input(
            f"Bravo! Bonne réponse. Vous avez réussi en {nbr_essais_total} essai(s). Voulez-vous faire une autre partie (o/n)?")
        if reponse == 'n':
            print("Merci et au revoir...")
            jeu = False

        elif reponse == "o":
            jeu = True
            nbr_essais_total = 0
            choix_de_bornes()
            chiffre_aleatoire = random.randint(borne_minimale, borne_maximale)
            print(f"J'ai choisi un nombre entre {borne_minimale} et {borne_maximale}. À vous de deviner...")
    elif essai > chiffre_aleatoire:
        print(f"Mauvais choix, le nombre est plus petit que {essai}")
        nbr_essais_addition()
    elif essai < chiffre_aleatoire:
        print(f"Mauvais choix, le nombre est plus grand que {essai}")
        nbr_essais_addition()
