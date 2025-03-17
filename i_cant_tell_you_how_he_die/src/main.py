import random
import time
import os
import sys
import threading


def jouer_bruit():
    try:
        os.system("afplay /System/Library/Sounds/Sosumi.aiff")  # macOS
    except:
        pass  # Ne rien faire si le son ne peut pas être joué

# Messages effrayants générés par l'entité
messages_terrifants = [
    "Tu ne devrais pas être ici.",
    "Je te vois.",
    "Tu sais ce que j'attends de toi...",
    "Le temps est compté.",
    "Regarde derrière toi.",
    "Ton écran commence à se briser... doucement.",
    "Les yeux... je vois des yeux derrière l'écran.",
    "Tu ne peux pas m'échapper, peu importe ce que tu fais.",
    "L'heure approche... tu vas bientôt comprendre."
]


def attente_angoissante():
    time.sleep(random.uniform(2, 5))  # Attente aléatoire pour perturber le rythme


def entite_parle():
    for i in range(5):
        attente_angoissante()
        print(f"\n{random.choice(messages_terrifants)}")
        jouer_bruit()  # Si le son fonctionne
        attente_angoissante()


def erreur_systeme():
    erreur_message = random.choice([
        "Erreur système grave : Impossible de récupérer la mémoire.",
        "Le programme a détecté une anomalie dans le système.",
        "Echec de la connexion à Internet.",
        "Redémarrage forcé en cours... erreur critique détectée !"
    ])
    print(f"\n{erreur_message}")
    time.sleep(2)
    print("\nVérification du disque... C'est étrange, une erreur persiste.")
    time.sleep(3)


def programme_terrifant():
    print("Tu viens de lancer un programme inconnu...")
    time.sleep(2)
    print("\nTout semble normal... mais pourquoi ton écran clignote-t-il légèrement ?")
    time.sleep(3)

    # L'entité parle après quelques secondes
    entite_parle()

    # Manipulation des erreurs système
    erreur_systeme()

    # La fin est ambiguë, l'entité laisse un dernier message
    print("\nLe programme semble se fermer tout seul...")
    time.sleep(3)
    print("\nAttends... c'est impossible. Tu ne peux pas éteindre ton ordinateur.")
    print("\nLe programme est toujours là. Tu n'es jamais seul.")


def lancer_programme():
    thread = threading.Thread(target=programme_terrifant)
    thread.start()
    thread.join()

if __name__ == "__main__":
    print("Bienvenue dans le programme spécial Halloween...")
    lancer_programme()