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
