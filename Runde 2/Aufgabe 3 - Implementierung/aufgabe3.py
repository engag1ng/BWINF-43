import time
import random

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
    """Returns whether a STRING either 'y' or '?' which is counted as True."""
    return string == "y" or string == '?'

def read_file():
    """
    Reads the example file and returns important information in the following order:
    ROWS (int): Number of Rows
    COLUMNS (int): Number of columns
    IS_LINE_SPECIFIED (bool): Whether or not a first line is specified
    FIRST_LINE (array): The first line, or empty array if not specified
    TABLE (nested array): The table made up of all rows  
    """
    with open(directory+filename, encoding='utf-8') as file:
        content = [line.strip() for line in file.readlines()]
    first_row = content[0].split()
    rows = int(first_row[0])
    columns = int(first_row[1])
    is_line_specified = is_True(first_row[2])

    if is_line_specified:
        first_line = content[-1].split()
        table = [row.split() for row in content[1:-1]]
    else:
        first_line = []
        table = [row.split() for row in content[1:]]
    return rows, columns, is_line_specified, first_line, table

def valid_lines(table):
    """Checks if every row in TABLE has enough 'y' or '?' to be valid."""
    for row in table:
        count = sum(1 for cell in row if is_True(cell))
        if count < 2:
            return False
    return True

def is_valid(table):
    """Checks if a table is valid. Meaning there are atleast 2 adjacent 'y' or '?' in each row."""
    if is_line_specified:
        if first_line != table[0]:
            return False
    for row in table:
        half = len(row) // 2
        count = sum(is_True(cell) for cell in row)
        if count > half: # If there are more than 50% trues than there have to be 2 adjacent.
            continue
        if not any(is_True(a) and is_True(b) for a, b in zip(row, row[1:])):
            return False 
    return True

def score_table(table):
    """Calculate a score indicating how close the table is to being valid. 
    For instance, sum scores for each row: +1 per valid adjacent pair and +0.5 per valid cell.
    """
    total_score = 0
    for row in table:
        valid_cells = sum(is_True(cell) for cell in row)
        row_score = valid_cells * 0.5
        
        row_score += sum(1 for a, b in zip(row, row[1:]) if is_True(a) and is_True(b))
        total_score += row_score
    return total_score

def find_hotspot(lst):
    """Finds the hotspot of True values in a row. This means that at the hotspot there is an equal distribution of True's to either side."""
    n = len(lst)
    min_diff = float('inf')
    hotspot_index = -1

    for i in range(n):
        left_count = sum(1 for x in lst[:i] if is_True(x))
        right_count = sum(1 for x in lst[i+1:] if is_True(x))
        
        diff = abs(left_count - right_count)

        if diff < min_diff:
            min_diff = diff
            hotspot_index = i
            
    return hotspot_index

def weighted_index(lst):
    """Creates a weights list that represents a heat-map for which columns are most likely to be changed around or changed to 
    due to the higher concentration of True's in the column."""
    hotspot = find_hotspot(lst)
    n = len(lst)
    weights = [0] * n
    
    if hotspot == -1:
        return weights
    
    max_weight = n // 2
    for i in range(n):
        weights[i] = max(0, max_weight - abs(hotspot - i))
    
    return weights

def random_index(weights):
    """Returns a random index based on the WEIGHTS."""
    total_weight = sum(weights)
    
    if total_weight == 0: 
        return random.randint(0, len(weights) - 1)
    
    chosen_index = random.choices(range(len(weights)), weights=weights)[0]
    return chosen_index

def simulated_annealing(col_table, max_time=30, initial_temp=100.0, cooling_rate=0.95):
    """Implementation of a simulated annealing approach to finding an optimal solution in MAX_TIME.
    The function returns the best found solution after MAX_TIME or a working solution if one is found before that.
    The standard starting parameters are MAX_TIME = 30 (s) INITIAL_TEMP = 100.0 and COOLINGRATE = 0.95"""
    if is_line_specified:
        column_sums = [sum(1 for cell in col if is_True(cell)) for col in col_table]
        col_table = sorted(
            col_table,
            key=lambda col: (column_sums[col_table.index(col)], -abs(find_hotspot(first_line) - col_table.index(col))),
            reverse=True
        )
    else:
        col_table = sorted(col_table, key=lambda x: sum(1 for cell in x if is_True(cell)), reverse=True)
    if is_valid(list(zip(*col_table))):
        return col_table
    
    current_table = col_table
    current_score = score_table(list(zip(*current_table)))
    best_table = current_table
    best_score = current_score
    temperature = initial_temp
    if is_line_specified:
        weights = weighted_index(first_line)
    else:
        weights = [len(current_table[0])-i+1 for i in range(len(current_table[0]))]

    while time.time() - start_time < max_time:
        new_table = current_table[:]
        while True:
            if len(new_table) < 500:
                a = random.randint(0, len(new_table) - 1)
                b = random.randint(0, len(new_table) - 1)
            else:
                a = random_index(weights)
                b = random_index(weights)
            if a != b:
                break

        if is_line_specified:
            current_rows = [list(row) for row in zip(*new_table)]
            if first_line == current_rows[0]:
                while True:
                    if new_table[a][0] == new_table[b][0]:
                        break
                    a = random_index(weights)
                    b = random_index(weights)

        new_table[a], new_table[b] = new_table[b], new_table[a]
        
        new_rows = [list(row) for row in zip(*new_table)]
        new_score = score_table(new_rows)
        
        delta = new_score - current_score
        if delta > 0 or math.exp(delta / temperature) > random.random():
            current_table = new_table
            current_score = new_score
            if new_score > best_score:
                best_table = new_table
                best_score = new_score

        temperature *= cooling_rate
        if temperature < 1e-3:
            temperature = initial_temp 

        if is_valid(new_rows):
            print(new_table)
            return new_table

    return best_table

rows, columns, is_line_specified, first_line, table = read_file()

if not valid_lines(table):
    print("Not a valid input")
    with open("./ausgaben/"+filename+".out", "w", encoding='utf-8') as file:
        file.write("Not a valid input!")
else:
    col_table = [list(col) for col in zip(*table)]
    result_table = simulated_annealing(col_table)
    row_table = [list(row) for row in zip(*result_table)]

    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime} seconds")

    start_string = "No solution found in"
    if is_valid(row_table):
        start_string = "Solution found in"
        print("Solution found")
    
    with open("./ausgaben/"+filename+".out", "w", encoding='utf-8') as file:
        file.write(f"{start_string} {runtime}s:\n{row_table}")