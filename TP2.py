"""
Programme fait par Lily Qian
Groupe: 403
Description: un jeu qui te permet à deviner un chiffre aléatoirement généré par l'ordinateur
"""

import random
chiffre_aleatoire = random.randint(0, 100)
jeu = True
nbr_essai_initial = 0


def nbr_essais_total():
   global nbr_essai_initial
   nbr_essai_initial += 1
"""

Cette fonction sert à pouvoir montrer le nombre d'essais à la fin du jeu
"""

print("J'ai choisi un nombre entre 0 et 100. À vous de deviner...")

while jeu:
 essai = int(input("Entrez votre essai :"))

 if essai == chiffre_aleatoire:
     nbr_essais_total()
     reponse = input(f"Bravo! Bonne réponse. Vous avez réussi en {nbr_essai_initial} essai(s). Voulez-vous faire une autre partie (o/n)?")
     if reponse == 'n':
         print("Merci et au revoir...")
         jeu = False

     elif reponse == "o":
         jeu = True
         print("J'ai choisi un nombre entre 0 et 2. À vous de deviner...")


 elif essai > chiffre_aleatoire:
     print(f"Mauvais choix, le nombre est plus petit que {essai}")
     nbr_essais_total()


 elif essai < chiffre_aleatoire:
     print(f"Mauvais choix, le nombre est plus grand que {essai}")
     nbr_essais_total()


