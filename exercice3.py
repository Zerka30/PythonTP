#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Clément PERRIN & Raphaël HIEN
Year: 2020
"""

bank_accounts = [  # On définit une liste contenant des dictionnaire
    {"id": 5698, "owner": "Raphaël", "balance": 9634.0, "discover": 0.0},
    {"id": 5632, "owner": "Clément", "balance": 127.0, "discover": -500.0},
    {"id": 5148, "owner": "Maxime", "balance": 1354.0, "discover": -15000.0},
    {"id": 3496, "owner": "Léo", "balance": 700.0, "discover": -250.0}
]


def print_menu():
    """
    Fonction perméttant d'afficher le menu et de demander à l'utilisateur quelle action il veut faire.
    :return: l'action que veux faire l'utilisateur.
    """
    print("\t(1) Afficher le solde.")
    print("\t(2) Déposer de l'argent.")
    print("\t(3) Retirer de l'argent.")
    print("\t(4) Créer un compte.")
    print("\t(5) Accèder aux données de tous les comptes.")
    print("\t(e) Sortir de la Bank.")
    return input("Entrez l'action que vous souhaitez faire: ")


def account_exist(account_id, accounts):
    """
    Fonction pour savoir si compte existe en utilisant son identifiant unique.
    :param accounts: liste des comptes.
    :param account_id: l'identifiant du compte a tester.
    :return: une Tuple avec comme première valeur: vrai si le compte existe et faux si le compte n'existe pas et en deuxième valeur la position dans la liste des comptes passé en parramètre.
    """
    found = False
    i = 0
    while found is not True and i < len(accounts):
        if accounts[i]["id"] == account_id:
            found = True
        else:
            i += 1
    return found, i


def get_account(accounts):
    """
    Fonction permettant de récupérer la position du compte dans la liste des comptes passé en parramètre.
    :param accounts: liste des comptes.
    :return: une Tuple: un boolean si le compte démandé existe et la position dans la liste des comptes du comptes demandés.
    """
    account_id = int(input("Entrez votre numéro de compte: "))
    exist = account_exist(account_id, accounts)
    if not exist[0]:
        print("Votre compte n'existe pas")
    return exist[0], exist[1]


def get_balance(accounts):
    """
    Procédure permettant d'afficher le solde d'un compte qui se trouve dans la liste passé en parramètre
    :param accounts: liste des comptes
    """
    account = get_account(accounts)
    if account[0]:
        bank = accounts[account[1]]
        print("Vous avez {:.2f}$ en banque".format(bank["balance"]))


def deposit_money(accounts):
    """
    Procédure pour déposer de l'argent sur un compte qui se trouve dans la liste passé en parramètre.
    :param accounts: liste des comptes.
    """
    account = get_account(accounts)
    if account[0]:
        bank = accounts[account[1]]
        deposit = float(input("Combien souhaitez vous déposer ? "))
        bank["balance"] += deposit
        print("Vous avez désormais {:.2f}$ en banque".format(bank["balance"]))


def withdraw_money(accounts):
    """
    Procédure pour retirer de l'argent sur un compter qui se trouve dans la liste passé en parramètre.
    :param accounts: liste des comptes.
    """
    account = get_account(accounts)
    if account[0]:
        bank = accounts[account[1]]
        withdraw = float(input("Combien souhaitez vous retirer ? "))
        if bank["balance"] - withdraw > bank["discover"]:
            bank["balance"] -= withdraw
            print("Vous avez désormais {:.2f}$ en banque".format(bank["balance"]))
        else:
            print(
                "Vous ne pouvez pas retirer autant d'argent, vous dépasseriez votre découvert qui est actuellement de {:.2f}.".format(
                    bank["discover"]))
            print("Vous avez donc {:.2f}$ en banque.".format(bank["balance"]))


def create_account(accounts):
    """
    Procédure pour créer un compte et l'ajouter dans la liste des comptes passé en parramètre.
    :param accounts: liste des comptes.
    """
    id = int(input("Entrez une id de compte: "))
    owner = input("Entrez le propriétaire: ")
    balance = float(input("Entrez le montant du compte : "))
    discover = float(input("Entrez le montant de discover : "))
    if account_exist(id, accounts)[0]:
        print("Le compte existe déjà dans notre banque !")
    else:
        accounts.append({"id": id, "owner": owner, "balance": balance, "discover": discover})
        print("Le compte a bien été créé !")


def see_account(accounts, username="admin", password="Pa$$word"):
    """
    Procédure permettant d'afficher les informations de tous les comptes.
    :param accounts: liste de comptes.
    :param username: login administrateur.
    :param password: mot de passe administrateur.
    :return:
    """
    if username == "admin" and password == "Pa$$word":
        for i in range(len(accounts)):
            account = accounts[i]
            print(" - id : {} , owner : {} , balance : {} , discover : {}".format(account["id"], account["owner"],
                                                                                  account["balance"],
                                                                                  account["discover"]))


print(" ")
print("Bienvenue à la Bank")
print(" ")

running = True

while running:
    choice = print_menu()
    if choice == "1":
        get_balance(bank_accounts)
    elif choice == "2":
        deposit_money(bank_accounts)
    elif choice == "3":
        withdraw_money(bank_accounts)
    elif choice == "4":
        create_account(bank_accounts)
    elif choice == "5":
        see_account(bank_accounts)
    elif choice == "e":
        print("Au revoir ...")
        running = False
    print()
