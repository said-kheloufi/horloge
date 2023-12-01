from datetime import datetime, timedelta
import time

def afficher_heure(heure, minute, seconde):
    heure_format = "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde)
    print(heure_format, end='\r')

def saisir_heure():
    try:
        print("Régler l'heure")
        heure = int(input("Entrez l'heure : "))
        minute = int(input("Entrez les minutes : "))
        seconde = int(input("Entrez les secondes : "))
        return datetime(2000, 1, 1, heure, minute, seconde)
    except ValueError:
        print("Veuillez entrer des valeurs numériques.")
        return saisir_heure()

def saisir_alarme():
    try:
        print("Régler l'alarme")
        heure = int(input("Entrez l'heure de l'alarme : "))
        minute = int(input("Entrez les minutes de l'alarme : "))
        seconde = int(input("Entrez les secondes de l'alarme : "))
        return datetime(2000, 1, 1, heure, minute, seconde)
    except ValueError:
        print("Veuillez entrer des valeurs numériques.")
        return saisir_alarme()

def regler_alarme(heure_alarme, heure_actuelle):
    if heure_actuelle == heure_alarme:
        print("Alarme ! L'heure de l'alarme est atteinte.")

heure_actuelle = saisir_heure()
heure_alarme = saisir_alarme()

while True:
    afficher_heure(heure_actuelle.hour, heure_actuelle.minute, heure_actuelle.second)
    regler_alarme(heure_alarme, heure_actuelle)
    time.sleep(1)

    heure_actuelle += timedelta(seconds=1)
