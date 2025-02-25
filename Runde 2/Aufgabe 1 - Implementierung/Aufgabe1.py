import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Beispiel Textdatei aus ./beispiele/")

    parser.add_argument('beispiel', type=str, help='Beispiel zum berechnen.')

    args = parser.parse_args()


directory = "./beispiele/"
filename = args.beispiel

def is_tree(tree):
    """Gibt True zurück wenn TREE, eine Liste, ein Baum ist. Ansonsten False."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def branches(tree):
    "Gibt den alle Zweige von TREE zurück."
    return tree[1:]

def read_file():
    """
    Liest alle wichtigen Daten aus dem Beispiel aus und gibt diese zurück.
    N: Integer, Die Anzahl an verschieden Perlen
    Pearls: Liste, Die Größen der Perlen
    Message: String, Die zu kodierende Nachricht
    """
    with open(directory+filename, encoding='utf-8') as file:
        content = file.readlines()
        content = [line.strip() for line in content]
    n = int(content[0])
    if n == 1:
        with open("./ausgaben/"+filename+".out", "w", encoding='utf-8') as file:
            file.write("Es muss mindestens 2 Perlen geben!")
        raise ValueError('Es muss mindestens 2 Perlen geben!')
    pearls = [int(number) for number in content[1].split()]
    message = content[2]

    return n, pearls, message

n, pearls, message = read_file()

def count_frequencies (frequencies={}):
    for char in message:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    my_tree = sorted([[freq, [char]] for char, freq in frequencies.items()], key= lambda x: x[0])

    return my_tree
my_tree = count_frequencies()
print(my_tree)

def collapse_tree(tree, n):
    """
    Fusioniert die N Knoten mit dem kleinsten Label Wert in TREE bis ein valider Baum mit nur einem Wurzelknoten ensteht.
    N: Integer der bestimmt wie viele Knoten auf einmal fusioniert werden.
    TREE: Ein invalider Baum mit einer Anzahl an Teilbäumen in Form von Listen als Zweigen.
    """
    if len(tree) == 1:
        return tree[0]
    n_smallest = []
    for index, node in enumerate(tree):
        if len(n_smallest) < n:
            n_smallest.append((index, node[0]))
        else:
            n_smallest = sorted(n_smallest, key=lambda x: x[1], reverse=True)
            if node[0] < n_smallest[0][1]:
                n_smallest[0] = (index, node[0])

    combined_branch = [tree[item[0]] for item in n_smallest]
    combined_branch.insert(0, sum([item[0] for item in combined_branch]))

    for item in sorted(n_smallest, key=lambda x: x[0], reverse=True):
        tree.remove(my_tree[item[0]])
    tree.insert(min([item[0] for item in n_smallest]), combined_branch)
    collapse_tree(tree, n)
    return tree[0]

if n > 62: #Es wird maximal mit 62 Perlen kodiert
    n = 62
collapsed_tree = collapse_tree(my_tree, n)
print(f"Collapsed tree:{collapsed_tree}")

def index_mapping(index):
    """
    Erlaubt Kodierungen mit bis zu 62 Perlen.
    Nimmt N, wenn N kleiner 10 -> gibt N, ansonsten gibt zugehörigen ASCII Charakter von 10 = A bis 62 = z.
    """
    if index < 10:
        return index
    elif index >= 10 and index <= 36:
        return chr(index+55)
    elif index >= 37 and index <= 62:
        return chr(index+60)
    else:
        raise ValueError("Wie kann das sein?")

def find_paths(tree, path="", checked=False):
    """
    Findet den Pfad zu allen Blättern mit Hilfe von Rekursion. Der Pfad wird als String durch die Indeces in jedem Teilbaum angegeben.
    """
    paths = {}

    # Check for single character
    if checked == False and len(tree[1]) == 1:
        leaf_value = tree[1][0]
        paths[leaf_value] = "00"
        return paths
    
    checked = True

    # Check if the current node is a leaf
    if isinstance(tree, list) and len(tree) == 1 and isinstance(tree[0], str):
        leaf_value = tree[0]
        paths[leaf_value] = path
        return paths

    # If the node is not a leaf, iterate over its children
    else:
        for index, subtree in enumerate(tree[1:]):
            subtree_paths = find_paths(subtree, path + str(index_mapping(index)), checked)
            paths.update(subtree_paths)

    return paths

codes = find_paths(collapsed_tree)
for letter in codes:
    codes[letter] = codes[letter][:-1] # Because of the nesting of the tree every path gets an unncessary '0' at the end

def encode_message(encoded = ""):
    for char in message:
        encoded += codes[char]
    with open("./ausgaben/"+filename+".out", "w", encoding='utf-8') as file:
        file.write(str(codes)+"\n"+f"Kodierte Textlänge {len(encoded)}")
    print(codes)
    print(f"Kodierte Textlänge {len(encoded)}")

encode_message()