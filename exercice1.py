#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Clément PERRIN
Year: 2020
"""

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Constante

chaine = input("Entrez votre chaine à décoder: ")  # P0$ùa1'OMàç-(98*/-M(-(0E+%S

result = ""
for i in range(len(chaine)):
    for j in range(len(char)):
        if chaine[i] == char[j]:
            result += char[j]
print(result)
