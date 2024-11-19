filename = "schwierigkeitenX.txt"

def check_highest(old_value, new_value):
    """
    Vergleicht einen alten und neuen Wert und gibt den höheren zurück.

    >>> old_value = 1
    >>> new_value = 2
    >>> check_highest(old_value, new_value)
    2

    >>> old_value = 2
    >>> new_value = 1
    >>> check_highest(old_value, new_value)
    2
    """
    if old_value < new_value:
        return new_value
    return old_value

def check_lowest(old_value, new_value):
    """
    Vergleicht einen alten und neuen Wert und gibt den niedrigeren zurück.

    >>> old_value = 1
    >>> new_value = 2
    >>> check_highest(old_value, new_value)
    1

    >>> old_value = 2
    >>> new_value = 1
    >>> check_highest(old_value, new_value)
    1
    """
    if old_value > new_value:
        return new_value
    return old_value

# Liest die Aufgabedatei ein
with open(filename, 'r') as file:
    content = file.readlines()
    content.pop(0) # Die erste Zeile kann wird nicht benötigt
    searched = []
    searched = content[-1].strip().split() # Speichert die gesuchten Werte ab
    content.pop() # Löscht die gesuchten Werte aus der Werteliste

# Räumt die Werteliste auf, entfernt zusätzliche Zeichen
processed_content = []
for item in content:
    subarray = item.replace('<', '').replace('\n', '').split()
    processed_content.append(subarray)

# Speichert alle wichtigen Werte ab
value_dictionary = {}

# Findet den höchsten und niedrigsten Auftritt und die Häufigkeit 
# jedes Buchstabens in der Werteliste
for item in processed_content:
    for index, letter in enumerate(item):
        value_dictionary.update({letter: value_dictionary.get(letter, 0)+index})
        value_dictionary.update({f"{letter}_highest": check_highest(value_dictionary.get(f"{letter}_highest", 0), index)})
        value_dictionary.update({f"{letter}_lowest": check_lowest(value_dictionary.get(f"{letter}_lowest", 0), index)})
        value_dictionary.update({f"{letter}_occurrence": value_dictionary.get(f"{letter}_occurrence", 0)+1})

# Kalkuliert den Wert jedes Buchstabens
worth_dictionary = {}
for letter in searched:
    worth_dictionary.update({letter: round(value_dictionary.get(letter)/value_dictionary.get(f"{letter}_occurrence"),2)})

# Sortiert die Liste an gesuchten Werten basierend auf Wert, dann dem höchsten und dann niedrigsten Auftritt
sorted_searched = sorted(
    searched,
    key = lambda item: (worth_dictionary.get(f"{item}"),
                        value_dictionary.get(f"{item}_highest", 0),
                        -value_dictionary.get(f"{item}_lowest", 0)
    )
)
# Gibt die sortierte Liste (Ergebnisse) aus
print(sorted_searched)