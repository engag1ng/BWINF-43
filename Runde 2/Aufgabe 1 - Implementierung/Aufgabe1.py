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

### CLASS DEFINITIONS ###
import heapq

class Node:
    def __init__(self, value, is_leaf=True):
        self.value = value
        self.is_leaf = is_leaf
        self.children = []
        self.parent = None

    def __lt__(self, other):
        return self.value < other.value

class TreeWithHeap:
    def __init__(self, is_weighted, frequencies= {}):
        if is_weighted:
            self.root = Node(0)
            self.leaf_heap = [(self.root.value, self.root)]# Min-heap of leaf nodes
        else:
            self.root = Node(0)
            self.top_layer = []
            for item in frequencies.items():
                self.node = Node(item[1]) 
                self.top_layer.append(self.node)

    def add_parent(self, children, value):
        new_parent = Node(value, is_leaf=False)
        for child in children:
            # If the child already has a parent, remove it from that parent's children list.
            if child.parent is not None:
                child.parent.children.remove(child)
            child.parent = new_parent
            new_parent.children.append(child)
            # Remove the child from top_layer if it is present there.
            if child in self.top_layer:
                self.top_layer.remove(child)
        # Add the new parent to the top_layer.
        self.top_layer.append(new_parent)
        return new_parent

    def add_child(self, parent, value):
        new_node = Node(value)
        new_node.parent = parent
        parent.children.append(new_node)
        return new_node

    def find_n_smallest(self, n):
        if n <= 0:
            return []

        return heapq.nsmallest(n, self.top_layer, key=lambda node: node)

    def find_min_leaf(self):
        if not self.leaf_heap:
            return None
        return self.leaf_heap[0][1]

    def transform_and_add_children(self, node, new_values):
        # Transform the leaf node into an internal node
        node.is_leaf = False
        # Remove it from the heap
        self.leaf_heap = [(val, n) for val, n in self.leaf_heap if n != node]
        heapq.heapify(self.leaf_heap)

        # Add new children
        for value in new_values:
            # New node's value = parent's value + added value
            new_node_value = node.value + value
            new_node = Node(new_node_value)
            node.children.append(new_node)
            heapq.heappush(self.leaf_heap, (new_node.value, new_node))

    def find_all_paths(self, is_weighted=False):
        paths = []

        def dfs(node, current_path):
            if node.is_leaf:
                if is_weighted:
                    paths.append((current_path, node.value))
                else:
                    if len(current_path) == 0:
                        current_path = "0"
                        path_length = 1
                    else:
                        path_length = len(current_path)
                    paths.append((current_path, path_length))
                return

            for index, child in enumerate(node.children):
                dfs(child, current_path + str(index_mapping(index)))

        dfs(self.root, "")
        return paths

    def print_tree(self, nodes=None):
        def _print_tree(node, prefix="", is_last=True):
            branch = "└── " if is_last else "├── "
            print(prefix + branch + str(node.value))
            prefix += "    " if is_last else "│   "
            child_count = len(node.children)
            for i, child in enumerate(node.children):
                _print_tree(child, prefix, i == child_count - 1)

        if nodes is None:
            nodes = self.top_layer
    
        for node in nodes:
            print(str(node.value))
            child_count = len(node.children)
            for i, child in enumerate(node.children):
                _print_tree(child, "", i == child_count - 1)
            print()


### GENERAL FUNCTION DEFINITIONS ### 

def read_file():
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

def count_frequencies(frequencies={}):
    for char in message:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
        
    return frequencies, len(frequencies)

def collapse_tree(tree, n): 
    n_smallest = tree.find_n_smallest(n)
    if len(n_smallest) == 1:
        return tree
    tree.add_parent(n_smallest, sum([node.value for node in n_smallest]))

    collapse_tree(tree, n)

    return tree

def index_mapping(index):
    if index < 10:
        return index
    elif index >= 10 and index <= 36:
        return chr(index+55)
    elif index >= 37 and index <= 62:
        return chr(index+60)
    else:
        raise ValueError("Wie kann das sein?")

def assign_codes(paths, frequencies, total_characters):
    paths = sorted(paths, key=lambda x: x[1])[:total_characters]
    frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    codes = {}
    for i in range(len(frequencies)):
        codes[frequencies[i][0]] = paths[i]

    return codes

def encode_message(codes):
    encoded = ""
    encoded_length = 0
    for char in message:
        encoded += codes[char][0]
        encoded_length += codes[char][1]
    with open("./ausgaben/"+filename+".out", "w", encoding='utf-8') as file:
        file.write(str(codes)+"\n"+f"Kodierte Textlänge: {encoded_length}")
    print(codes)
    print(f"Kodierte Textlänge: {encoded_length}")

### IMPLEMENTATION ###
def n_ary_huffman(n):
    frequencies, total_characters = count_frequencies()

    tree = TreeWithHeap(False, frequencies)
    
    collapse_tree(tree, n)

    tree.root = tree.top_layer[0]

    paths = tree.find_all_paths()
    
    codes = assign_codes(paths, frequencies, total_characters)

    encode_message(codes)

def weighted_huffman(n, pearls, message):
    frequencies, total_characters = count_frequencies()
    needed_expansions = (total_characters-1)/(n-1)
    
    tree = TreeWithHeap(True)

    for i in range(math.ceil(needed_expansions)):
        min_leaf_node = tree.find_min_leaf()
        tree.transform_and_add_children(min_leaf_node, pearls)

    paths = tree.find_all_paths(True)

    codes = assign_codes(paths, frequencies, total_characters)

    encode_message(codes)

### CHECK WHICH CONDITION APPLIES ###
n, pearls, message = read_file()
n_not_1 = len([x for x in pearls if x != 1])
if n > 62: #Es wird maximal mit 62 Perlen kodiert
        n = 62
if n_not_1 == 0:
    n_ary_huffman(n)
else:
    weighted_huffman(n, pearls, message)

end_time = time.time()
print(f"Runtime: {(end_time - start_time)*1000} milli seconds")