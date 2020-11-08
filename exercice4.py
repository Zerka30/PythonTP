
import string
import random

parking = []
unlock_code = []
string.ascii_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range (0, 81): # On Ajoute 81 fois "D" dans le tableau parking
    parking.append("D")

for i in range(0, 3): #Cette boucle nous permet d'ajouter aléatoirement 2 places handicapés par etage
    for j in range(0, 2):
        if i == 0:
            handi_place = random.randint(0, 27)
            parking[handi_place] = "H"
        if i == 1:
            handi_place = random.randint(27, 54)
            parking[handi_place] = "H"
        if i == 2:
            handi_place = random.randint(54, 81)
            parking[handi_place] = "H"

for i in range(0, 81): # On génére les codes d'identification pour sortir du parking
    if i < 10:
        letters = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        code = str(0)+str(i)
        unlock_code.append({"place": i, "code": letters+"-"+code})
print(unlock_code)

def print_parking():
    print("Etage n°0 : ")
    for i in range (0, 27):
        print(parking[i], end=" ")
        if i == 8 or i == 17: #Permet de faire un retour à la ligne au bout de 9 caractères
            print(" ")
    print("\nEtage n°1 : ")
    for i in range (27,54):
        print(parking[i], end=" ")
        if i == 35 or i == 44: #Permet de faire un retour à la ligne au bout de 9 caractères
            print(" ")
    print("\nEtage n°2 : ")
    for i in range (54,81):
        print(parking[i], end=" ")
        if i == 62 or i == 71: #Permet de faire un retour à la ligne au bout de 9 caractères
            print(" ")
    print("")

def park_cars():
    place = int(input("\nA quels place souhaitez vous vous garer ? \n"))
    while place < 0 or place > 81: #On vérifie que l'utilisateur à entrer une place existant sinon on lui redemande son n° de place
        print("Cette place n'existe pas, nous avons actuellement une capacité de 81 places")
        place = int(input("A quels place souhaitez vous vous garer ? \n"))
    while parking[place] == "P": #On vérifie si la place est libre sinon on redemande son n° place
        print("Désolé mais cette place est déjà prise")
        place = int(input("A quels place souhaitez vous vous garer ? \n"))
    parking[place] = "P" #On modifie l'état de la place
    print("Le code de sortie de votre place est {}".format(unlock_code[place].get("code"))) #On affiche le code de la place
    print_parking()

def exit_cars():
    place = int(input("\nDe quels place souhaitez vous sortir ? \n"))
    while place < 0 or place > 81: #On vérifie que l'utilisateur à entrer une place existant sinon on lui redemande son n° de place
        print("Cette place n'existe pas")
        place = int(input("De quels place souhaitez vous sortir ? \n"))
    while parking[place] == "D": #On vérifie si la place est prise sinon on redemande son n° place
        print("Désolé mais cette place n'est pas occupé par une voiture")
        place = int(input("De quels place souhaitez vous sortir ? \n"))
        if place == "e": #On ajoute une fonction pour sortir de la boucle (pas obligatoire)
            exit()
    code_place = unlock_code[place].get("code") #On récupére le code du n° de la place
    code = input("Entrer votre code : ") #On demande son code
    if code_place == code: #On vérifie que le code donne et le code de la place son identique
        parking[place] = "D" #On modifie l'état de la place
    else:
        print("Désolé le code est erronée") 
    print_parking()

def menu():
    print("\nBienvenue dans notre parking")
    print(" ")
    print("(1) Afficher l'état du parking")
    print("(2) Garer sa voiture")
    print("(3) Sortir sa voiture")
    print("(e) Sortir du menu")
    choice = input("Entre l'action que vous souhaitez faire : ")
    print(" ")
    return choice

choice = menu()
while choice != "e":
    if choice == "1": #Bien penser à mettre les guillemets, il s'agit ici du caractère 1 qui compris par la fonction input et pas le chiffre 1 (distanction entre string & int / float)
        print_parking()
    elif choice == "2":
        park_cars()
    elif choice == "3":
        exit_cars()
    elif choice == "e":
        exit()
    choice = menu()
