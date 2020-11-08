accounts = [  # On définit une liste contenant des dictionnaire
    {"id": 5698, "owner": "Raphaël", "balance": 9634.0, "discover": 0.0},
    {"id": 5632, "owner": "Clément", "balance": 127.0, "discover": -500.0},
    {"id": 5148, "owner": "Maxime", "balance": 1354.0, "discover": -15000.0},
    {"id": 3496, "owner": "Léo", "balance": 700.0, "discover": -250.0}
]


def print_menu():
    print("\t(1) Afficher le solde.")
    print("\t(2) Déposer de l'argent.")
    print("\t(3) Retirer de l'argent.")
    print("\t(4) Créer un compte.")
    print("\t(5) Accèder aux données de tous les comptes.")
    print("\t(e) Sortir de la Bank.")
    return input("Entrez l'action que vous souhaitez faire: ")


def account_exist(account_id):  # On crée  une fonction qui nous retourne si le compte passé en paramètre existe
    found = False
    i = 0
    while found is not True and i < len(accounts):
        account = accounts[i]
        if account["id"] == account_id:
            found = True
        else:
            i += 1
    return found


def get_account():  # On crée une fonction qui nous retourne le n° du compte dans la liste afin de pouvoir le récupére si besoin
    account = int(input("Entrer votre numéro de compte : "))
    id = -1
    found = False
    if account_exist(account):
        for i in range(len(accounts)):
            bank = accounts[i]
            if bank["id"] == account:
                id = i
                found = True
    else:
        print("Votre compte n'existe pas")
    return found, id


def check_balance():
    account = get_account() # On récupére le compte correspondant au n° de compte donne lors de l'appel get_account()
    if account[0]:
        bank = accounts[account[1]]
        print("Vous avez {:.2f}$ en banque".format(bank["balance"]))  # On affice le solde du compte
        print(" ")


def deposit_money():
    account = get_account() # On récupére le compte correspondant au n° de compte donne lors de l'appel get_account()
    if account[0]:
        bank = accounts[account[1]]
        deposit = float(input("Combien souhaitez vous déposer ? "))
        bank["balance"] = bank["balance"] + deposit  # On met la somme du compte à la somme du compte + la somme déposer
        print("Vous avez désormais {:.2f}$ en banque".format(bank["balance"]))


def withdraw_money():
    account = get_account() # On récupére le compte correspondant au n° de compte donne lors de l'appel get_account()
    if account[0]:
        bank = accounts[account[1]]
        withdraw = float(input("Combien souhaitez vous retirer ? "))
        if bank["balance"] - withdraw > bank["discover"]:  # On vérifie si ce que l'on souhaite retirer est possible en prennant en compte le découvert
            bank["balance"] = bank["balance"] - withdraw  # On met à jour la somme
            print("Vous avez désormais {:.2f}$ en banque".format(bank["balance"]))
        else:
            print("Vous ne pouvez pas retirer autant d'argent, vous dépasseriez votre découvert qui est actuellement de {:.2f}.".format(bank["discover"]))
            print("Vous avez donc {:.2f}$ en banque.".format(bank["balance"]))


def create_account():
    id = int(input("Entrez une id de compte : "))
    owner = input("Entrez le propriétaire : ")
    balance = float(input("Entrez le montant du compte : "))
    discover = float(input("Entrez le montant de discover : "))
    if account_exist(id):  # On vérifie si notre id existe déjà, si oui on affiche une erreur
        print("Le compte existe déjà dans notre banque !")
    else:
        accounts.append({"id": id, "owner": owner, "balance": balance, "discover": discover})  # Sinon on ajoute notre compte à la liste
        print("Le compte a bien été créé !")


def see_account(username="admin", password="Pa$$word"):  # On crée une fonction qui permet de donne la liste de tous les comptes de la banque avec un identifiant et un mot de passe (on pourrait ajouter un système basique d'authentification)
    if username == "admin" and password == "Pa$$word":
        for i in range(0, len(accounts)):
            account = accounts[i]
            print(" - id : {} , owner : {} , balance : {} , discover : {}".format(account["id"], account["owner"], account["balance"], account["discover"]))


print(" ")
print("Bienvenue à la C Bank")
print(" ")

choice = print_menu()
while choice != 'e':
    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        create_account()
    elif choice == "5":
        see_account()
    elif choice == "e":
        exit()
    choice = print_menu()
