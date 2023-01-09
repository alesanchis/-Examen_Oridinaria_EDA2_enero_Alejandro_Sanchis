# Clase Planeta
class Planeta:
   def _init_(self, nombre):
       self.nombre = nombre
       self.vecinos = []
       self.costos = []
 
 
# Clase GrafoNoDirigido
class GrafoNoDirigido:
   def _init_(self):
       self.planetas = {}
       self.distancias = {}
 
   def agregar_planeta(self, nombre):
       # Agregamos un nuevo planeta al grafo
       planeta = Planeta(nombre)
       self.planetas[nombre] = planeta
 
   def conectar(self, nombre1, nombre2, costo):
       # Conectamos dos planetas y le asignamos un costo a la conexión
       planeta1 = self.planetas[nombre1]
       planeta2 = self.planetas[nombre2]
       planeta1.vecinos.append(planeta2)
       planeta2.vecinos.append(planeta1)
       planeta1.costos.append(costo)
       planeta2.costos.append(costo)
       self.distancias[(nombre1, nombre2)] = costo
 
   def arbol_expansion_minima(self, nombre_inicio):
       # Utilizamos el algoritmo de Prim para encontrar el árbol de expansión mínima
       visitados = []
       no_visitados = list(self.planetas.keys())