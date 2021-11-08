#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import os

# TODO: Définissez vos fonction ici
def signaler_dif(file_1, file_2):
    with open(file_1, 'r') as f1, open(file_2, 'r') as f2:
        for ligne1 in f1:
            ligne2 = f2.readline(f2)
            if ligne1 != ligne2:
                print('les 2 fichiers sont different')
        print('les 2 fichiers sont identiques')
    
    return None


def tripler_espace(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'w') as f2:
        f2.write(f1.read().replace(' ','   '))

    return None


def ecrire_notes(lecture_notes, ecriture_notes):
    with open(lecture_notes, 'r') as f1, open(ecriture_notes, 'w') as f2:
        for ligne in f1:
            for lettre, note in enumerate(PERCENTAGE_TO_LETTER):
                if note[1] > int(ligne) >= note[0]:
                    f2.write(PERCENTAGE_TO_LETTER[lettre] + '\n')

    return None

def ecrire_recette(file_path1):
    with open(file_path1, '+'):
        continuer_livre=('oui')

        while continuer_livre=='oui':
            recette=input('donnez le nom de la recette')
            livre[recette]=(input('donnez les ingredients de la rectte'))
            continuer_livre=(input('voulez vous continuer?'))

    return None

    
def ecrire_liste_nombres(file_path1):
    liste_nombre = []
    nombre = ''
    with open(file_path1, 'r') as f1:
        for ligne in f1:
            for lettre in ligne:
                if lettre.isnumeric():
                    nombre += lettre
                elif len(nombre) > 1:
                        liste_nombre.append(int(nombre))
                        nombre = ''

        liste_nombre.sort
    return(liste_nombre)


def ligne_sur_deux(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'w') as f2:
        for numero_ligne, ligne in enumerate(f1):
            if numero_ligne%2 == 0:
                f2.write(ligne)

    return None
                    


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print('yo')
    print(ecrire_liste_nombres('c03-ch8-exercices-seigward12\exemple.txt'))
    pass
