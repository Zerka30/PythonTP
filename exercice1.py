input = input("Entrée votre chaine à décoder") # P0$ùa1'OMàç-(98*/-M(-(0E+%S
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

for i in range(0, len(input)):
    for j in range(0, len(char)):
        if input[i] == char[j]:
          result = result + char[j]
print(result)
