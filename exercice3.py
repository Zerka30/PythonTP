accounts = [ #On définit une liste contenant des dictionnaire

    {"id": "5698", "owner": "Raphaël", "balance": "9634", "discover": "0"},
    {"id": "5632", "owner": "Clément", "balance": "127", "discover": "-500"},
    {"id": "5148", "owner": "Maxime", "balance": "1354", "discover": "-15000"},
    {"id": "3496", "owner": "Léo", "balance": "700", "discover": "-250"}

]

def printMenu():
    print(" ")
    print("Bienvenue à la C Bank")
    print(" ")
    print("(1) Afficher le solde")
    print("(2) Déposer de l'argent")
    print("(3) Retirer de l'argent")
    print("(4) Créer un compte")
    print("(5) Accèder aux données de tous les comptes")
    print("(e) Sortir de la Bank")
    choice = input("Entre l'action que vous souhaitez faire : ")
    print(" ")
    return choice

def account_exist(account): #On crée  une fonction qui nous retourne si le compte passe en paramètre existe
    found = False
    i = 0
    while found is not True and i < len(accounts):
        nbr = accounts[i]
        if nbr["id"] == account:
            found = True
        else:
            i += 1
    return found

def getAccount(): #On crée une fonction qui nous retourne le n° du compte dans la liste afin de pouvoir le récupére si besoin
    account = input("Entrer votre numéro de compte : ")
    if account_exist(account) == True:
        for i in range (0, len(accounts)):
            bank = accounts[i]
            if bank["id"] == account:
                break
    else:
        print("Votre compte n'existe pas")
    return i

def checkBalance():
    bank = accounts[getAccount()] #On récupére le compte correspondant au n° de compte donne lors de l'appel getAccount()
    print("Vous avez {}$ en banque".format(bank["balance"])) #On affice le solde du compte
    print(" ")

def depositMoney():
    bank = accounts[getAccount()] #On récupére le compte correspondant au n° de compte donne lors de l'appel getAccount()
    deposit = int(input("Combien souhaitez vous déposez ? \n"))
    bank["balance"] = deposit + int(bank["balance"]) #On met la somme du compte à la somme du compte + la somme déposer
    print("Vous avez désormais {}$ en banque".format(bank["balance"]))

def withdrawMoney():
    bank = accounts[getAccount()] #On récupére le compte correspondant au n° de compte donne lors de l'appel getAccount()
    withdraw = int(input("Combien souhaitez vous retirez ? \n"))
    if int(bank["balance"]) - withdraw > int(bank["discover"]): #On vérifie si ce que l'on souhaite retirer est possible en prennant en compte le découvert
        bank["balance"] =  int(bank["balance"]) - withdraw #On met à jour la somme
        print("Vous avez désormais {}$ en banque".format(bank["balance"]))
    else:
        print("Vous ne pouvez pas retire autant d'argent, vous dépasseriez votre découvert qui est actuellement de {}".format(bank["discover"]))
        print("Vous avez donc {}$ en banque".format(bank["balance"]))

def createAccount():
    id = int(input("Entrer une id de compte : "))
    owner = input("Entrer le propriétaire : ")
    balance = int(input("Entrer le montant du compte : "))
    discover = int(input("Entre le montant de discover : "))
    if account_exist(id) == True: #On vérifie si notre id existe déjà, si oui on affiche une erreur
        print("Le compte exite déjà dans notre banque")
    else:
        accounts.append({"id": id, "owner": owner,"balance": balance, "discover": discover}) #Sinon on ajoute notre compte à la liste

def seeAccounts(username="admin", password="Pa$$word"): #On crée une fonction qui permet de donne la liste de tous les comptes de la banque avec un identifiant et un mot de passe (on pourrait ajouter un système basique d'authentification)
    if(username == "admin")and(password== "Pa$$word"):
        for i in range (0, len(accounts)):
            account = accounts[i]
            print(" - id : {} , owner : {} , balance : {} , discover : {}".format(account["id"], account["owner"], account["balance"], account["discover"]))
    return


choice = printMenu()
while choice != 'e':
    if choice == "1":
        checkBalance()
    elif choice == "2":
        depositMoney()
    elif choice == "3":
        withdrawMoney()
    elif choice == "4":
        createAccount()
    elif choice == "5":
        seeAccounts()
    elif choice == "e":
        exit()
    choice = printMenu()
