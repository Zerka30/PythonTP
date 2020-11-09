# Procedure avec 2 parramètres n etc
def triangle(n, c):
    """
    Afficher un triangle selon les parramètres passé lors de l'appel de la procédure.
    :param n: la taille du triangle
    :param c: le carractère pour faire le triangle
    """
    z = n - 1
    x = 1
    for i in range(n):
        print(" " * z + c * x + " " * z)
        x += 2
        z -= 1


# Programme principal
n = -1
while n < 0:
    try:
        n = int(input("Entrez la taille du triangle: "))
    except ValueError:
        n = -1

c = input("Entrez le caractère pour afficher le triangle: ")
triangle(n, c)
