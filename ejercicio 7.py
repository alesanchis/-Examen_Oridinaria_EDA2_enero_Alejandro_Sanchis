import heapq
from collections import defaultdict

# Función para generar el árbol de Huffman a partir de las frecuencias de los símbolos
def generate_huffman_tree(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

# Función para generar el diccionario de codificaciones a partir del árbol de Huffman
def generate_codes(huffman_tree):
    codes = defaultdict(str)
    for pair in huffman_tree[1:]:
        codes[pair[0]] = pair[1]
    return codes

# Función para comprimir un mensaje utilizando el diccionario de codificaciones
def compress(message, codes):
    compressed_message = ""
    for symbol in message:
        compressed_message += codes[symbol]
    return compressed_message

# Función para descomprimir un mensaje utilizando el árbol de Huffman
def decompress(compressed_message, huffman_tree):
    message = ""
    node = huffman_tree
    for bit in compressed_message:
        if bit == '0':
            node = node[1]
        else:
            node = node[2]
        if type(node) == str:
            message += node
            node = huffman_tree
    return message

# Ejemplo de uso
frequencies = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09, "T": 0.15}
huffman_tree = generate_huffman_tree(frequencies)
codes = generate_codes(huffman_tree)
message = "AF1330MTA"
compressed_message = compress(message, codes)
print("Mensaje original:", message)
print("Mensaje comprimido:", compressed_message)