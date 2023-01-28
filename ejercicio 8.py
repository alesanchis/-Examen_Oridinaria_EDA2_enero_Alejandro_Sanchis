import networkx as nx

# Crear un grafo vacío
G = nx.Graph()

# Agregar los planetas al grafo
planetas = ["Tierra", "Knowhere", "Zen-Whoberi", "Vomir", "Titán", "Nidavellir", "Planeta1", "Planeta2", "Planeta3", "Planeta4", "Planeta5", "Planeta6", "Planeta7"]
G.add_nodes_from(planetas)

# Agregar conexiones entre los planetas
G.add_edge("Tierra", "Knowhere")
G.add_edge("Tierra", "Zen-Whoberi")
G.add_edge("Tierra", "Vomir")
G.add_edge("Tierra", "Titán")
G.add_edge("Tierra", "Nidavellir")
G.add_edge("Tierra", "Planeta1")
G.add_edge("Tierra", "Planeta2")
G.add_edge("Tierra", "Planeta3")
G.add_edge("Tierra", "Planeta4")
G.add_edge("Tierra", "Planeta5")
G.add_edge("Tierra", "Planeta6")
G.add_edge("Tierra", "Planeta7")

# Dibujar el grafo
nx.draw(G, with_labels=True)

camino = nx.dijkstra_path(G, "Tierra", "Nidavellir")
print(camino)

componente = nx.connected_components(G)
print(componente)

grado = nx.degree(G, "Tierra")
print(grado)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
            
    def DFS(self, vertex):
        stack = []
        visited = []
        stack.append(vertex)
        while stack:
            m = stack.pop()
            if m not in visited:
                visited.append(m)
                stack.extend(self.vertices[m] - set(visited))
        return visited
    
    def BFS(self, vertex):
        queue = []
        visited = []
        queue.append(vertex)
        while queue:
            m = queue.pop(0)
            if m not in visited:
                visited.append(m)
                queue.extend(self.vertices[m] - set(visited))
        return visited
    
    def Dijkstra(self, vertex1, vertex2):
        queue = []
        visited = []
        distances = {vertex: float('infinity') for vertex in self.vertices}
        previous_vertices = {vertex: None for vertex in self.vertices}

        return

# Crear el grafo vacío
grafo = {
    'Tierra': [],
    'Knowhere': [],
    'Zen-Whoberi': [],
    'Vomir': [],
    'Titán': [],
    'Nidavellir': [],
    'Xandar':[],
    'Asgard':[],
    'Hala':[],
    'Mephisto':[],
    'Ego':[],
}

# Agregar las 4 aristas para cada uno de los planetas
grafo['Tierra'].append('Xandar')
grafo['Tierra'].append('Asgard')
grafo['Tierra'].append('Hala')
grafo['Tierra'].append('Mephisto')

grafo['Knowhere'].append('Ego')
grafo['Knowhere'].append('Mephisto')
grafo['Knowhere'].append('Hala')
grafo['Knowhere'].append('Xandar')

grafo['Zen-Whoberi'].append('Asgard')
grafo['Zen-Whoberi'].append('Mephisto')
grafo['Zen-Whoberi'].append('Hala')
grafo['Zen-Whoberi'].append('Xandar')

grafo['Vomir'].append('Asgard')
grafo['Vomir'].append('Mephisto')
grafo['Vomir'].append('Hala')
grafo['Vomir'].append('Xandar')

grafo['Titán'].append('Ego')
grafo['Titán'].append('Mephisto')
grafo['Titán'].append('Hala')
grafo['Titán'].append('Xandar')

grafo['Nidavellir'].append('Ego')
grafo['Nidavellir'].append('Mephisto')
grafo['Nidavellir'].append('Hala')
grafo['Nidavellir'].append('Xandar')

grafo['Xandar'].append('Tierra')
grafo['Xandar'].append('Asgard')
grafo['Xandar'].append('Hala')
grafo['Xandar'].append('Mephisto')

grafo['Asgard'].append('Tierra')
grafo['Asgard'].append('Zen-Whoberi')
grafo['Asgard'].append('Vomir')
grafo['Asgard'].append('Mephisto')

grafo['Hala'].append('Tierra')
grafo['Hala'].append('Zen-Whoberi')
grafo['Hala'].append('Vomir')
grafo['Hala'].append('Mephisto')

grafo['Mephisto'].append('Xandar')
grafo['Mephisto'].append('Tierra')
grafo['Mephisto'].append('Egor')
grafo['Mephisto'].append('Zen-Whoberi')

grafo['Ego'].append('Ego')
grafo['Ego'].append('Mephisto')
grafo['Ego'].append('Zen-Whoberi')
grafo['Ego'].append('Xandar')

def obtenerArbolExpansionMinima(grafo):
    arbol = set()
    nodosVisitados = {grafo.keys()[0]}
    nodosNoVisitados = set(grafo.keys()) - nodosVisitados
  
    while nodosNoVisitados:
        aristaMinima = None
        for nodo in nodosVisitados:
            for vecino, costo in grafo[nodo]:
                if vecino in nodosNoVisitados:
                    if aristaMinima is None or costo < aristaMinima[2]:
                        aristaMinima = (nodo, vecino, costo)
        nodosVisitados.add(aristaMinima[1])
        nodosNoVisitados.remove(aristaMinima[1])
        arbol.add(aristaMinima)
  
    return arbol

from queue import PriorityQueue

def shortest_path(graph, start, end):
    # Diccionario para almacenar los costos y predecesores de cada nodo
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    predecessors = {node: None for node in graph}

    # Cola de prioridad para elegir el nodo con menor costo
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        current_cost, current_node = queue.get()

        # Si se llegó al nodo final, se termina el ciclo
        if current_node == end:
            break

        # Se recorren los vecinos del nodo actual
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                predecessors[neighbor] = current_node
                queue.put((new_cost, neighbor))

    # Se recupera el camino más corto
    path = [end]
    while path[-1] != start:
        path.append(predecessors[path[-1]])
    path.reverse()

    return path, costs[end]

# Se define el grafo con las aristas y sus costos
graph = {
    'Tierra': {'Knowhere': 2, 'Zen-Whoberi': 3, 'Nidavellir': 4},
    'Knowhere': {'Titán': 1, 'Vomir': 5},
    'Zen-Whoberi': {'Vomir': 2, 'Nidavellir': 3},
    'Vomir': {'Titán': 4},
    'Titán': {'Nidavellir': 2},
    'Nidavellir': {}
}

# Se busca el camino más corto entre Tierra y Vormir
start = 'Tierra'
end = 'Vormir'
path, cost = shortest_path(graph, start, end)
print("Camino más corto desde %s hasta %s:" % (start, end), path)
print("Costo:", cost)

import heapq

def dijkstra(graph, start):
    # Crear una cola de prioridades para seleccionar el nodo con la distancia tentativa más pequeña
    queue = [(0, start)]
    # Inicializar distancias tentativas con infinito
    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0
    # Inicializar diccionario de predecesores
    previous = {vertex: None for vertex in graph}
    # Repetir mientras haya nodos por visitar
    while queue:
        # Obtener el nodo con la distancia tentativa más pequeña
        (cost, current) = heapq.heappop(queue)
        # Si ya se ha visitado, continuar
        if current in dist and cost > dist[current]:
            continue
        # Marcar como visitado
        dist[current] = cost
        # Actualizar distancias tentativas de los vecinos
        for neighbor, cost in graph[current].items():
            if cost + dist[current] < dist[neighbor]:
                dist[neighbor] = cost + dist[current]
                heapq.heappush(queue, (dist[neighbor], neighbor))
                previous[neighbor] = current
    # Devolver distancias y predecesores
    return dist, previous

def dijkstra(grafo, inicio, fin):
    # Crea un diccionario para almacenar las distancias desde el inicio a cada nodo
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    # Crea un conjunto de nodos no visitados
    no_visitados = set(grafo)
    # Mientras queden nodos no visitados
    while no_visitados:
        # Selecciona el nodo con distancia mínima entre los no visitados
        nodo_actual = min(no_visitados, key=lambda x: distancias[x])
        # Si se ha llegado al nodo final, se devuelve la distancia
        if nodo_actual == fin:
            return distancias[fin]
        # Marca el nodo actual como visitado y lo elimina del conjunto de no visitados
        no_visitados.discard(nodo_actual)
        # Actualiza las distancias de los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            if peso + distancias[nodo_actual] < distancias[vecino]:
                distancias[vecino] = peso + distancias[nodo_actual]
    return None

dijkstra(grafo, "Zen-Whoberi", "Nidavellir")

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbour in graph[vertex]:
                stack.append(neighbour)
    return visited

# Ejemplo de uso
planets = {"Tierra": ["Knowhere", "Zen-Whoberi"], 
           "Knowhere": ["Vomir", "Titán"], 
           "Zen-Whoberi": ["Nidavellir"], 
           "Vomir": [], 
           "Titán": ["Nidavellir", "Vomir"], 
           "Nidavellir": []}

print(dfs(planets, "Titán"))
