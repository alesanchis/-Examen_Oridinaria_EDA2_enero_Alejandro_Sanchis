from heapq import heappush, heappop

# Función para encontrar el camino más corto desde el planeta de origen hasta el de destino
def shortest_path(graph, origin, destination):
    # Crear una lista de distancias y un diccionario de predecesores para almacenar los caminos más cortos
    distances = {}
    predecessors = {}

    # Inicializar las distancias y los predecesores para todos los planetas
    for planet in graph.planets.values():
        distances[planet] = float("inf")
        predecessors[planet] = None

    # Crear una lista de prioridades para implementar el algoritmo de Dijkstra
    heap = []

    # Añadir el planeta de origen a la lista de prioridades con distancia 0
    heappush(heap, (0, origin))
    distances[origin] = 0

    # Mientras haya planetas por procesar en la lista de prioridades
    while heap:
        # Tomar el planeta con menor distancia
        distance, planet = heappop(heap)

        # Si el planeta es el de destino, terminar el algoritmo
        if planet == destination:
            break

        # Recorrer los vecinos del planeta
        for neighbor, cost in planet.neighbors:
            # Calcular la distancia a través del vecino
            new_distance = distance + cost

            # Si la distancia a través del vecino es menor que la distancia actual al vecino, actualizarla
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = planet

                # Añadir el vecino a la lista de prioridades
                heappush(heap, (new_distance, neighbor))

    # Crear una lista para almacenar el camino más corto
    path = []

    # Recorrer los predecesores desde el planeta de destino hasta el de origen
    planet = destination
    while planet is not None:
        # Añadir el planeta al camino
        path.append(planet)

        # Pasar al predecesor del planeta
        planet = predecessors[planet]

    # Devolver el camino en orden inverso (del origen al destino)
    return path[::-1]
# Crear el grafo
graph = Graph()

# Añadir los planetas al grafo
planet_names = ["Alderaan", "Endor", "Dagobah", "Hoth", "Tatooine", "Kamino", "Naboo", "Mustafar", "Scarif", "Bespin",]
for name in planet_names:
    graph.add_planet(planet(name))

# Añadir las conexiones entre los planetas
graph.add_edge("Alderaan", "Endor", 20)
graph.add_edge("Alderaan", "Dagobah", 10)
graph.add_edge("Endor", "Hoth", 15)
graph.add_edge("Endor", "Tatooine", 5)
graph.add_edge("Dagobah", "Tatooine", 15)
graph.add_edge("Dagobah", "Kamino", 5)
graph.add_edge("Hoth", "Tatooine", 10)
graph.add_edge("Hoth", "Naboo", 20)
graph.add_edge("Tatooine", "Naboo", 5)
graph.add_edge("Tatooine", "Mustafar", 10)
graph.add_edge("Kamino", "Mustafar", 15)
graph.add_edge("Naboo", "Mustafar", 5)
graph.add_edge("Naboo", "Scarif", 10)
graph.add_edge("Mustafar", "Scarif", 15)
graph.add_edge("Scarif", "Bespin", 10)

# Encontrar el camino más corto desde Tatooine hasta Dagobah
path = shortest_path(graph, graph.planets["Tatooine"], graph.planets["Dagobah"])

# Imprimir el camino más corto
print("Camino más corto:")
for planet in path:
    print(planet.name)

# Encontrar el camino más corto desde Alderaan hasta Endor
path = shortest_path(graph, graph.planets["Alderaan"], graph.planets["Endor"])

# Imprimir el camino más corto
print("Camino más corto:")
for planet in path:
    print(planet.name)

# Encontrar el camino más corto desde Hoth hasta Tatooine
path = shortest_path(graph, graph.planets["Hoth"], graph.planets["Tatooine"])

# Imprimir el camino más corto
print("Camino más corto:")
for planet in path:
    print(planet.name)

