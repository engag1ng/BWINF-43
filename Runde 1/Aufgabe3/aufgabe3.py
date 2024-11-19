filename = 'wandernX.txt'

# Datei einlesen
with open(filename, 'r') as file:
    lines = file.readlines()
# Erste Zeile wird nicht benötigt, andere Werte in Array speichern
number_array = [[index, tuple(map(int, line.strip().split()))] for index, line in enumerate(lines[1:])]

# Aufsteigend nach erstem Wert sortieren
number_array = sorted(number_array, key=lambda x: x[1])

scores = []
seen_minimums = set()

def find_values(start_index):
    """
    Findet alle sinnvollen Rennlängen und die Überschneidungen mit den Wunschlängen durch einen Sweep-Line Algorithmus.
    Die Funktion ist rekursiv.

    intersections -- Zählt die Nummer an Überschneidungen
    people        -- Speichert den Index jeder Überschneidung
    minimum       -- Untere Grenze der Sweep-Line
    maximum       -- Obere Grenze der Sweep-Line
    seen_minimums -- Alle bereits vorgekommenen Minimums
    """
    intersections = 0
    people = []
    minimum = 0
    maximum = 10**100

    for pair in number_array[start_index:]:
        if int(pair[1][0]) >= minimum and int(pair[1][0]) <= maximum:
            minimum = int(pair[1][0])
        else:
            if intersections > 1 or len(scores) < 3:
                if minimum not in seen_minimums:
                    scores.append([intersections, people, minimum])
                    seen_minimums.add(minimum)
            start_index += 1 
            if start_index < len(number_array):
                find_values(start_index)
            return
       
        if int(pair[1][1]) >= minimum and int(pair[1][1]) <= maximum:
            maximum = int(pair[1][1])
        
        intersections += 1
        people.append(pair[0])
    if intersections > 1 or len(scores) < 3:
        if minimum not in seen_minimums:
            scores.append([intersections, people, minimum])
            seen_minimums.add(minimum)

find_values(0) # Ruft die Funktion das erste mal auf
scores = sorted(scores, key=lambda x: x[0], reverse=True) # Sortiert nach der Anzahl der Überschneidungen

people = []
for score in scores:
    people.append(score[1]) # Speichert die teilnehmenden Leute für jeden möglichen Wert

def iter_combinations(iterable, r):
    """
    Findet alle möglichen Kombination aus r items, in diesem Fall Listen von Leuten zurück.
    
    Implementation der Python itertools Bibliothek für Kombinationen: https://docs.python.org/3/library/itertools.html#itertools.combinations
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))

    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

combinations = list(iter_combinations(people, 3))

# Berechnet für jede Kombination die Anzahl an einzigartigen Teilnehmern
top_scores = []
for index,combination in enumerate(combinations):
    top_score = len(set(combination[0] + combination[1] + combination[2]))
    top_scores.append([index, top_score])

# Sortiert die Liste top_scores absteigend
top_scores = sorted(top_scores, key=lambda x: x[1], reverse=True)
top_scores = top_scores[0]

# Gibt die beste Kombination zurück
best_combination = combinations[top_scores[0]]

# Findet die zugehörigen Indexes für die teilnehmenden Leute der besten Kombination
matching_results = []
for index, score in enumerate(scores):
    if score[1] in best_combination:
        matching_results.append(score)
        
# Gibt das Ergebnis aus
print(f"""Beste 3 Werte sind: {matching_results[0][2]}, {matching_results[1][2]}, {matching_results[2][2]}. 
Dabei nehmen jeweils die Personen: 
{str(matching_results[0][1]).replace('[','').replace(']', '')}; 
{str(matching_results[1][1]).replace('[','').replace(']', '')}; 
{str(matching_results[2][1]).replace('[','').replace(']', '')} teil. 
Insgesamt würden {top_scores[1]} Leute teilnehmen.""")