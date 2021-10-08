#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re


def find_square(filenames):
    for filename in filenames :
        print('\n>processing {} ...'.format(filename))

        try :
            with open(filename, "r") as file:
                lines = file.readlines()

                nb_lines, vide, obstacle, plein = lines[0].split()
                nb_lines = int(nb_lines)

                carte = [line.strip() for line in lines[1:]]

                if not is_map_valid(carte, nb_lines, vide, obstacle, plein) :
                    print("Map error for file {}".format(filename))
                    continue

                else :
                    process_map(carte, obstacle)
                    

        except IOError :
            print("Can not read file {}".format(filename))
            continue


'''
- cas1 : Toutes les lignes doivent avoir la même longueur.
- cas2 : Il y a au moins une ligne d’au moins une case.
- cas3 : À la fin de chaque ligne il y a un retour à la ligne.
- cas4 : Les caractères présent dans la carte doivent être uniquement ceux présenté à la première ligne.
'''
def is_map_valid(carte, nb_lines, vide='.', obstacle='o', plein='X'):
    if len(carte) != nb_lines : #cas3
        return False

    if not all([len(line) == len(carte[0]) for line in carte]) : # cas1
        return False

    if not any([line.count(vide)>1 for line in carte]) : # cas2
        return False


    carte_str = ''.join(carte) # tous les caractères de la carte dans un string
    pattern = '[^{}{}{}]'.format(vide, obstacle, plein)

    if re.search(pattern=pattern, string=carte_str): # cas4
        return False

    # jusqu'ici, pas d'erreur
    return True


def process_map(carte, obstacle):
    max_square = (0,0,0) # pos_line, pos_col, wide

    for i in range(len(carte)):
        for j in range(len(carte[0])):
            wide_range = min(len(carte[0])-j, len(carte)-i)

            for k in range(max_square[2]+1, wide_range):
                if is_full(carte, i, j, k, obstacle):
                    max_square = (i, j, k)


    print("find best at {} {} and wide {}".format(*max_square))

    pos_line, pos_col, wide = max_square

    for i in range(wide):
        carte[pos_line+i] = carte[pos_line+i][:pos_col] + 'X'*wide + carte[pos_line+i][pos_col+wide:]

    print('\n'.join(carte))

def is_full(carte, pos_line, pos_col, wide, obstacle):
    return all([line[pos_col:pos_col+wide].count(obstacle) == 0 for line in carte[pos_line:pos_line+wide]])

    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Find_square expects at least one parameter.')
        exit()
    find_square(sys.argv[1:])
