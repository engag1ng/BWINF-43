# QUADRATISCH, PRAKTISCH, GRÜN
#
# ACHTUNG: Vor dem benutzen muss in Zeile 82 umbedingt gartenX.txt mit dem richtigen Dateinamen z.B. garten0.txt, garten1.txt, ..., garten5.txt ausgetauscht werden! 
#

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
    divisors = [i for i in range(1, int(Interessenten**0.5) + 1) if Interessenten % i == 0]
    divisors += [Interessenten // i for i in divisors if i != Interessenten // i]

    closest_divisor = min(divisors, key=lambda d: abs(d - gerundet_optimale_horizontale_Aufteilungen))

    return closest_divisor

def solve_QPG(Höhe, Breite, Interessenten):
    if prime_check(Interessenten):
        if Interessenten < 10:
            if Höhe > Breite:
                beste_feld_höhe = round(Höhe / Interessenten, 3)
                horizontale_felder_anzahl = Interessenten

                beste_feld_breite = round(Breite, 3)
                vertikale_felder_anzahl = 1

            else:
                beste_feld_höhe = round(Höhe, 3)
                horizontale_felder_anzahl = 1

                beste_feld_breite = round(Breite/Interessenten, 3)
                vertikale_felder_anzahl = Interessenten

            return f"Beste Aufteilung ist {int(horizontale_felder_anzahl)} horizontale Felder mal {int(vertikale_felder_anzahl)} vertikale Felder à {beste_feld_höhe}m hoch mal {beste_feld_breite}m breit."
        else:
            Interessenten += 1
        
    optimale_horizontale_Aufteilungen = math.sqrt((Breite*Interessenten)/Höhe)
    gerundet_optimale_horizontale_Aufteilungen = round(optimale_horizontale_Aufteilungen, 0)

    if Interessenten % gerundet_optimale_horizontale_Aufteilungen == 0:
        beste_feld_höhe = round(Höhe/gerundet_optimale_horizontale_Aufteilungen, 3)
        beste_feld_breite = round(Breite * gerundet_optimale_horizontale_Aufteilungen/Interessenten, 3)

        return f"Beste Aufteilung ist {int(gerundet_optimale_horizontale_Aufteilungen)} horizontale Felder mal {int(Interessenten/gerundet_optimale_horizontale_Aufteilungen)} vertikale Felder à {beste_feld_höhe}m hoch mal {beste_feld_breite}m breit."

    else:
        nearest_optimale_horizontale_Aufteilungen = nearest_multiple_finder(gerundet_optimale_horizontale_Aufteilungen, Interessenten)

        beste_feld_höhe = round(Höhe/nearest_optimale_horizontale_Aufteilungen, 3)
        beste_feld_breite = round(Breite * nearest_optimale_horizontale_Aufteilungen/Interessenten, 3)

        return f"Beste Aufteilung ist {int(nearest_optimale_horizontale_Aufteilungen)} horizontale Felder mal {int(Interessenten/nearest_optimale_horizontale_Aufteilungen)} vertikale Felder à {beste_feld_höhe}m hoch mal {beste_feld_breite}m breit."

filename = 'gartenX.txt'
Interessenten, Höhe, Breite = read_file(filename)
print(solve_QPG(Höhe, Breite, Interessenten))