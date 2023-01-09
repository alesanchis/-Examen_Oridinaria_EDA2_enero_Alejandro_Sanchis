#apartados a y b

import random

class Stormtrooper:
    def __init__(self, code, legion):
        self.code = code
        self.legion = legion

class Node:
    def __init__(self, stormtrooper):
        self.stormtrooper = stormtrooper
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None for _ in range(size)]

    def hash_function(self, key):
       
        if self.size == 10:
            return key[-1]
        else:
            return ord(key[0]) % self.size

    def insert(self, stormtrooper):
        key = stormtrooper.code if self.size == 10 else stormtrooper.legion
        index = self.hash_function(key)
        new_node = Node(stormtrooper)
        if self.buckets[index] is None:
            self.buckets[index] = new_node
        else:
            current_node = self.buckets[index]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

def generate_stormtroopers():
    legions = ["FL", "TF", "TK", "CT", "FN", "FO"]
    stormtroopers = []
    for i in range(2000):
        code = "".join([random.choice(string.digits) for _ in range(7)])
        legion = random.choice(legions)
        stormtrooper = Stormtrooper(code, legion)
        stormtroopers.append(stormtrooper)
    return stormtroopers

stormtroopers = generate_stormtroopers()

hash_table1 = HashTable(10)
hash_table2 = HashTable(26)

for stormtrooper in stormtroopers:
    hash_table1.insert(stormtrooper)
    hash_table2.insert(stormtrooper)

# apartados c, d y e


def search_by_code(hash_table, code):
    index = hash_table.hash_function(code)
    current_node = hash_table.buckets[index]
    while current_node is not None:
        if current_node.stormtrooper.code == code:
            return True
        current_node = current_node.next
    return False


def get_by_code(hash_table, code):
    stormtroopers = []
    for i in range(hash_table.size):
        current_node = hash_table.buckets[i]
        while current_node is not None:
            if current_node.stormtrooper.code.endswith(code):
                stormtroopers.append(current_node.stormtrooper)
            current_node = current_node.next
    return stormtroopers


def get_by_legion(hash_table, legion):
    index = hash_table.hash_function(legion)
    stormtroopers = []
    current_node = hash_table.buckets[index]
    while current_node is not None:
        if current_node.stormtrooper.legion == legion:
            stormtroopers.append(current_node.stormtrooper)
        current_node = current_node.next
    return stormtroopers


if search_by_code(hash_table1, "FN-2187"):
    print("El Stormtrooper FN-2187 está cargado en la tabla hash.")
else:
    print("El Stormtrooper FN-2187 no está cargado en la tabla hash.")


stormtroopers_781 = get_by_code(hash_table1, "781")
stormtroopers_537 = get_by_code(hash_table1, "537")


print(f"Se han encontrado {len(stormtroopers_781)} Stormtrooper terminados en 781.")
print(f"Se han encontrado {len(stormtroopers_537)} Stormtrooper terminados en 537.")


stormtroopers_CT = get_by_legion(hash_table2, "CT")
stormtroopers_TF = get_by_legion(hash_table2, "TF")

