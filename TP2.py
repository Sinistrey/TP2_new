"""
Programme fait par Lily Qian
Groupe: 403
Description: un jeu qui te permet à deviner un chiffre aléatoirement généré par l'ordinateur
"""

import random
chiffre_aleatoire = random.randint(0, 2)
jeu = True
nbr_essai = 0
def nbr_essai_total():
    global nbr_essai
    nbr_essai += 1

while jeu:
  print("J'ai choisi un nombre entre 0 et 2. À vous de deviner...")
  essai = int(input("Entrez votre essai"))

  if essai == chiffre_aleatoire:
      reponse = input(f"Bravo! Bonne réponse. Vous avez réussi en {nbr_essai_total}: Voulez-vous rejouer? (o/n)")
      if reponse == 'n':
          print("Merci et aurevoir...")
          jeu = False

      elif reponse == "o":
          jeu = True


  elif essai > chiffre_aleatoire:
      print(f"Mauvais choix, le nombre est plus petit que {essai}")


  elif essai < chiffre_aleatoire:
      print(f"Mauvais choix, le nombre est plus grand que {essai}")






