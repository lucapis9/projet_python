import random

def afficher_regles():   #here we are printing all the rules for the game
    print("Bienvenue dans le jeu de l'aventure textuelle !")
    print("Vous explorez un donjon mystérieux à la recherche d'un trésor caché.")
    print("Faites attention aux pièges et aux monstres !")
    print("Vous pouvez taper 'gauche (g)', 'droite (d)' ou 'tout droit (t)' pour avancer.")
    print("Vous pouvez aussi taper 'inventaire' pour voir votre sac ou 'potion' pour utiliser une potion.")
    print("Soyez stratégique dans vos choix pour survivre jusqu'à la fin !")
    print("Niveaux disponibles : 1 (facile), 2 (moyen), 3 (difficile)")

def choisir_niveau():   #this function is for the player to choose a level
    while True:    #this is a loop until the player chooses a valid level (1,2 or 3)
        try:
            niveau = int(input("Choisissez un niveau (1-3) : "))  #asking for the level (the user chooses it)
            if niveau in [1, 2, 3]:   #checking for the level if its valid
                return niveau   #returning the level that the user has chosen
            else:
                print("Veuillez entrer un niveau valide (1, 2 ou 3).")   #if the level set by the user isnt valid then ask him again
        except ValueError:   #if its not a number
            print("Entrée invalide. Veuillez entrer un nombre.")   #ask the user to choose a number for the level

def choix_direction():   #here the player chooses where to go
    return input("Choisissez une direction (gauche/droite/tout droit) : ").strip().lower()   #here the player gives us the direction, and once he gave us the direction, the strip is going to clear all the blank spaces and lower is going to make the direction in lowercases. For example Gauche =gauche

def rencontre_aleatoire(niveau):   #this is the function to return a random event based on the level that the player choses   
    evenements_probables = {   #dictionnary fro each level with the possible events
        1: ["monstre", "piège", "rien", "trésor", "potion", "marchand", "coffre", "rien"],
        2: ["monstre", "piège", "rien", "trésor", "potion", "marchand", "coffre", "araignée"],
        3: ["monstre", "piège", "poison", "araignée", "trésor", "potion", "marchand", "coffre","Géant Goblin"]
    }
    return random.choice(evenements_probables[niveau])   #retunr a random event based on the level chosen

def gerer_evenement(evenement, joueur, niveau):  #this is the function that handles every event, and what happens in each event
    if evenement == "monstre":
        print("Un monstre apparaît !")
        chance = 0.7 - (niveau * 0.1)   #if the level is high than you have a lower chance to of winning
        if random.random() < chance:
            print("Vous avez vaincu le monstre !")
        else:
            degats = 10 + niveau * 5  #the damage increases if the level chosen is higher
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
        joueur["inventaire"].append("potion") #add a potion to the iventory list for the player
    elif evenement == "marchand":
        print("Vous rencontrez un marchand mystérieux. Il vous vend une potion pour 5 points de vie.")
        if joueur["vie"] > 5:
            joueur["vie"] -= 5
            joueur["inventaire"].append("potion") 
            print("Vous achetez une potion.")
        else:
            print("Vous n'avez pas assez de vie pour acheter quoi que ce soit.")
    elif evenement == "araignée":
        degats = 90 - (niveau * 15)  # the higher the level the less you loose life
        print(f"Vous tombez sur une araignée géante qui vous attaque. Vous perdez {degats} points de vie !")
        joueur["vie"] -= degats
    elif evenement == "coffre":
        print("Vous découvrez un coffre !")
        if random.random() < 0.5:  #50% chance of getting the magic sword
            print("Le coffre contenait une épée magique qui vous protégera mieux des monstres !")
            joueur["inventaire"].append("épée magique") #give the player the swords in his inventory
        else:
            print("Le coffre était vide...")

def afficher_inventaire(joueur): #funtion to show the players inventory
    print("Inventaire :", joueur["inventaire"])

def utiliser_potion(joueur):
    if "potion" in joueur["inventaire"]:  #function to use the potion in his inventory
        print("Vous utilisez une potion et regagnez 10 points de vie.")
        joueur["vie"] += 10
        joueur["inventaire"].remove("potion") #if player used a potion, then the potion is removed from his invetonry
    else:
        print("Vous n'avez pas de potion !")

def jeu_aventure():  #main function to run the game
    joueur = {"vie": 100, "trésor": False, "inventaire": []} #initialize the players stats
    afficher_regles()  #prints the rules of the game
    niveau = choisir_niveau() # let the player choose a difficulty

    while joueur["vie"] > 0 and not joueur["trésor"]: # loop if player have more than 0 lives and if the treasure hasn't been found
        direction = choix_direction() #ask for the direction
        if direction == "inventaire": #show players inventory
            afficher_inventaire(joueur)
            continue
        elif direction == "potion": #use a potion 
            utiliser_potion(joueur) 
            continue
        elif direction not in ["g", "d", "t"]: #if the direction isn't g,d or t then the direction is invalid
            print("Direction invalide. Essayez encore.")
            continue
        
        evenement = rencontre_aleatoire(niveau) #random event occurs depending on the level
        gerer_evenement(evenement, joueur, niveau)  #handle the event
        
        print(f"Points de vie restants : {joueur['vie']}")  #print the players health
        
    if joueur["vie"] <= 0:  #game ends here if the player has less than 0 life
        print("Vous avez perdu ! Votre aventure s'arrête ici.")
    elif joueur["trésor"]: #game ends if the treasure is found
        print("Bravo ! Vous avez gagné !")

if __name__ == "__main__":  #only runs this scripts if its executed directly
    jeu_aventure()  #start of the game
