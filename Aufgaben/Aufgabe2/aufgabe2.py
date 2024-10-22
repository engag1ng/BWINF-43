filename = "schwierigkeiten0.txt"

def check_highest(old_value, new_value):
    if old_value < new_value:
        return new_value
    return old_value

def check_lowest(old_value, new_value):
    if old_value > new_value:
        return new_value
    return old_value

with open(filename, 'r') as file:
    content = file.readlines()
    content.pop(0)
    searched = []
    searched = content[-1].strip().split()
    content.pop()

processed_content = []
for item in content:
    subarray = item.replace('<', '').replace('\n', '').split()
    processed_content.append(subarray)

value_dictionary = {}

for item in processed_content:
    for index, letter in enumerate(item):
        value_dictionary.update({letter: value_dictionary.get(letter, 0)+index})
        value_dictionary.update({f"{letter}_highest": check_highest(value_dictionary.get(f"{letter}_highest", 0), index)})
        value_dictionary.update({f"{letter}_lowest": check_lowest(value_dictionary.get(f"{letter}_lowest", 0), index)})
        value_dictionary.update({f"{letter}_occurrence": value_dictionary.get(f"{letter}_occurrence", 0)+1})

worth_dictionary = {}
for letter in searched:
    worth_dictionary.update({letter: round(value_dictionary.get(letter)/value_dictionary.get(f"{letter}_occurrence"),2)})

sorted_searched = sorted(
    searched,
    key = lambda item: (worth_dictionary.get(f"{item}"),
                        value_dictionary.get(f"{item}_highest", 0),
                        -value_dictionary.get(f"{item}_lowest", 0)
    )
)
print(sorted_searched)