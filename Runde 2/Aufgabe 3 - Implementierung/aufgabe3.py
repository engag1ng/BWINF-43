import time

start_time = time.time()

import argparse
import math
from math import ceil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Beispiel Textdatei aus ./beispiele/")

    parser.add_argument('beispiel', type=str, help='Beispiel zum berechnen.')

    args = parser.parse_args()


directory = "./beispiele/"
filename = args.beispiel

def is_True(string):
    return string == "y"

def read_file():
    with open(directory+filename, encoding='utf-8') as file:
        content = file.readlines()
        content = [line.strip() for line in content]
    first_row = content[0].split()
    rows = int(first_row[0])
    columns = int(first_row[1])
    is_line_specified = is_True(first_row[2])

    if is_line_specified:
        first_line = content[-1].split()
        print(first_line)
        table = [list(column) for column in zip(*content[1:-1])]
    else:
        first_line = False
        table = [list(column) for column in zip(*content[1:])]
    
    table = [element for index, element in enumerate(table) if index%2 == 0]

    print(table)
    return rows, columns, is_line_specified, first_line, table

def generate_permutations(array=[]):
    """Generates all possible permutations, and the amount, from an input array using lexicographic ordering"""

def has_first_line(first_line, table):
    """Returns whether a table has a certain first line"""
    return first_line == [list(row) for row in zip(*table)][0]

def replace_first_unreadable(table):
    """Replaces the first unreadable symbol in the table with both an cross and checkmark and returns both variants"""

def is_valid_table(table):
    """Returns whether a table is valid or not. To be valid every row has to have at least two adjacent 'y' in it."""
    table_rows = [list(row) for row in zip(*table)]
    for row in table_rows:
        if not any(row[i] == "y" and row[i + 1] == "y" for i in range(len(row) - 1)):
            return False
    return True
        

rows, columns, is_line_specified, first_line, table = read_file()

end_time = time.time()
print(f"Runtime: {(end_time - start_time)*1000} milli seconds")