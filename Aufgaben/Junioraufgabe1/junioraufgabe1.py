# QUADRATISCH, PRAKTISCH, GRÜN

import math

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        Interessenten = int(lines[0].strip())
        Höhe = int(lines[1].strip())
        Breite = int(lines[2].strip())

    return Interessenten, Höhe, Breite

def prime_check(number):
    f = 2

    while f * f <= number:
        if number%f == 0:
            return False
        f += 1
    return True

def nearest_multiple_finder(gerundet_optimale_horizontale_Aufteilungen, Interessenten):
    lower_multiple = (gerundet_optimale_horizontale_Aufteilungen//Interessenten) * Interessenten
    upper_multiple = lower_multiple + Interessenten

    diff_lower = abs(lower_multiple-gerundet_optimale_horizontale_Aufteilungen)
    diff_upper = abs(upper_multiple-gerundet_optimale_horizontale_Aufteilungen)

    if diff_lower < diff_upper:
        return lower_multiple
    elif diff_lower > diff_upper:
        return upper_multiple
    else:
        if optimale_horizontale_Aufteilungen > gerundet_optimale_horizontale_Aufteilungen:
            return upper_multiple
        else:
            return lower_multiple 

def solve_QPG(Höhe, Breite, Interessenten):
    if prime_check(Interessenten):
        if Interessenten < 10:
            if Höhe > Breite:
                beste_feld_höhe = Höhe / Interessenten
                horizontale_felder_anzahl = Interessenten

                beste_feld_breite = Breite
                vertikale_felder_anzahl = 1

            else:
                beste_feld_höhe = Höhe
                horizontale_felder_anzahl = 1

                beste_feld_breite = Breite/Interessenten
                vertikale_felder_anzahl = Interessenten

            return f"Beste Aufteilung ist {horizontale_felder_anzahl} horizontale Felder mal {vertikale_felder_anzahl} vertikale Felder à {beste_feld_höhe} hoch mal {beste_feld_breite} breit."
        else:
            Interessenten += 1
        
    optimale_horizontale_Aufteilungen = math.sqrt((Breite*Interessenten)/Höhe)
    gerundet_optimale_horizontale_Aufteilungen = round(optimale_horizontale_Aufteilungen, 0)

    if Interessenten % gerundet_optimale_horizontale_Aufteilungen == 0:
        beste_feld_höhe = Höhe/gerundet_optimale_horizontale_Aufteilungen
        beste_feld_breite = Breite * gerundet_optimale_horizontale_Aufteilungen/Interessenten

        return f"Beste Aufteilung ist {gerundet_optimale_horizontale_Aufteilungen} horizontale Felder mal {Interessenten/gerundet_optimale_horizontale_Aufteilungen} vertikale Felder à {beste_feld_höhe} hoch mal {beste_feld_breite} breit."

    else:
        nearest_optimale_horizontale_Aufteilungen = nearest_multiple_finder(gerundet_optimale_horizontale_Aufteilungen, Interessenten)

        beste_feld_höhe = Höhe/nearest_optimale_horizontale_Aufteilungen
        beste_feld_breite = Breite * nearest_optimale_horizontale_Aufteilungen/Interessenten

        return f"Beste Aufteilung ist {nearest_optimale_horizontale_Aufteilungen} horizontale Felder mal {Interessenten/nearest_optimale_horizontale_Aufteilungen} vertikale Felder à {beste_feld_höhe} hoch mal {beste_feld_breite} breit."

filename = 'garten0.txt'
Interessenten, Höhe, Breite = read_file(filename)
print(solve_QPG(Höhe, Breite, Interessenten))