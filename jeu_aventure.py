import random

def afficher_regles():
    print("Bienvenue dans le jeu de l'aventure textuelle !")
    print("Vous explorez un donjon mystérieux à la recherche d'un trésor caché.")
    print("Faites attention aux pièges et aux monstres !")
    print("Vous pouvez taper 'gauche (g)', 'droite (d)' ou 'tout droit (t)' pour avancer.")
    print("Vous pouvez aussi taper 'inventaire' pour voir votre sac ou 'potion' pour utiliser une potion.")
    print("Soyez stratégique dans vos choix pour survivre jusqu'à la fin !")
    print("Niveaux disponibles : 1 (facile), 2 (moyen), 3 (difficile)")

def choisir_niveau():
    while True:
        try:
            niveau = int(input("Choisissez un niveau (1-3) : "))  
            if niveau in [1, 2, 3]: 
                return niveau   
            else:
                print("Veuillez entrer un niveau valide (1, 2 ou 3).")  
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def choix_direction():
    return input("Choisissez une direction (gauche/droite/tout droit) : ").strip().lower()

def rencontre_aleatoire(niveau):  
    evenements_probables = {
        1: ["monstre", "piège", "rien", "trésor", "potion", "marchand", "coffre", "rien"],
        2: ["monstre", "piège", "rien", "trésor", "potion", "marchand", "coffre", "araignée"],
        3: ["monstre", "piège", "poison", "araignée", "trésor", "potion", "marchand", "coffre","Géant Goblin"]
    }
    return random.choice(evenements_probables[niveau])

def gerer_evenement(evenement, joueur, niveau): 
    if evenement == "monstre":
        print("Un monstre apparaît !")
        chance = 0.7 - (niveau * 0.1)
        if random.random() < chance:
            print("Vous avez vaincu le monstre !")
        else:
            degats = 10 + niveau * 5 
            print(f"Le monstre vous a blessé ! Vous perdez {degats} points de vie.")
            joueur["vie"] -= degats
    elif evenement == "piège":
        degats = 5 + niveau * 2
        print(f"Vous tombez dans un piège ! Vous perdez {degats} points de vie.")
        joueur["vie"] -= degats
    elif evenement == "poison":
        print("Vous avez avalé du poison ! Vous perdez 35 points de vie.")
        joueur["vie"] -= 35
    elif evenement == "Géant Goblin":
        print("Vous avez a peine battu le Géant goblin mais vous perdez 99 de vie..")
        joueur["vie"] -= 99
    elif evenement == "rien":
        print("Rien ne se passe...")
    elif evenement == "trésor":
        print("Félicitations ! Vous avez trouvé le trésor caché !")
        joueur["trésor"] = True 
    elif evenement == "potion":
        print("Vous trouvez une potion de soin !")
        joueur["inventaire"].append("potion")
    elif evenement == "marchand":
        print("Vous rencontrez un marchand mystérieux. Il vous vend une potion pour 5 points de vie.")
        if joueur["vie"] > 5:
            joueur["vie"] -= 5
            joueur["inventaire"].append("potion") 
            print("Vous achetez une potion.")
        else:
            print("Vous n'avez pas assez de vie pour acheter quoi que ce soit.")
    elif evenement == "araignée":
        degats = 90 - (niveau * 15)
        print(f"Vous tombez sur une araignée géante qui vous attaque. Vous perdez {degats} points de vie !")
        joueur["vie"] -= degats
    elif evenement == "coffre":
        print("Vous découvrez un coffre !")
        if random.random() < 0.5:
            print("Le coffre contenait une épée magique qui vous protégera mieux des monstres !")
            joueur["inventaire"].append("épée magique")
        else:
            print("Le coffre était vide...")

def afficher_inventaire(joueur):
    print("Inventaire :", joueur["inventaire"])

def utiliser_potion(joueur):
    if "potion" in joueur["inventaire"]: 
        print("Vous utilisez une potion et regagnez 10 points de vie.")
        joueur["vie"] += 10
        joueur["inventaire"].remove("potion")
    else:
        print("Vous n'avez pas de potion !")

def jeu_aventure():
    joueur = {"vie": 100, "trésor": False, "inventaire": []}
    afficher_regles()
    niveau = choisir_niveau()

    while joueur["vie"] > 0 and not joueur["trésor"]:
        direction = choix_direction()
        if direction == "inventaire":
            afficher_inventaire(joueur)
            continue
        elif direction == "potion":
            utiliser_potion(joueur) 
            continue
        elif direction not in ["g", "d", "t"]: 
            print("Direction invalide. Essayez encore.")
            continue
        
        evenement = rencontre_aleatoire(niveau)
        gerer_evenement(evenement, joueur, niveau)
        
        print(f"Points de vie restants : {joueur['vie']}")
        
    if joueur["vie"] <= 0:
        print("Vous avez perdu ! Votre aventure s'arrête ici.")
    elif joueur["trésor"]:
        print("Bravo ! Vous avez gagné !")

if __name__ == "__main__":
    jeu_aventure()
