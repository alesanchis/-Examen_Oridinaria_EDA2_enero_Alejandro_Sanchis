from ejercicio 3 import ArtefactosValiosos
from ejercicio 1 import mochila_01


class ArtefactoValioso:
  def init(self, peso, nombre, precio, fecha_caducidad):
    self.peso = peso
    self.nombre = nombre
    self.precio = precio
    self.fecha_caducidad = fecha_caducidad
    print("El artefacto valioso ha sido creado con éxito.")
    

def init(self, peso, nombre, precio, fecha_caducidad):
  self.peso = peso
  self.nombre = nombre
  self.precio = precio
  self.fecha_caducidad = fecha_caducidad
  print("El artefacto valioso ha sido creado con éxito.")

def __str__(self):
    return "Nombre: {}, Peso: {}, Precio: {}, Fecha de Caducidad: {}".format(self.nombre, self.peso, self.precio, self.fecha_caducidad)

def hijo_sin_amor(mochila):
      if not mochila:
        print("La mochila está vacía.")
      return

objeto = mochila_01.pop()

if objeto.nombre == "Anillo de Poder":
    print("El objeto encontrado es:")
    print(objeto)
else:
    print("El objeto encontrado es:")
    print(objeto)
    hijo_sin_amor(mochila)

    mochila = [ArtefactosValiosos(5, "Anillo de Poder", 1000, "01/01/2022"),
  ArtefactosValiosos(2, "Piedra Filosofal", 500, "01/01/2025"),
  ArtefactosValiosos(3, "Varita Mágica", 800, "01/01/2023"),
  ArtefactosValiosos(1, "Poción de Inmortalidad", 200, "01/01/2024")]

hijo_sin_amor(mochila)

#ccrear objetos de valor:

anillo_poder = ArtefactoValioso(0.5, "Anillo de poder", 10000, "2022-12-31")
diamante = ArtefactoValioso(0.1, "Diamante", 500, "2022-01-01")
oro = ArtefactoValioso(1, "Oro", 1000, "2021-07-01")
plata = ArtefactoValioso(0.8, "Plata", 800, "2022-09-01")

#Crear una mochila con los objetos

mochila = [oro, plata, diamante, anillo_poder]

#Llamar a la función recursiva

hijo_sin_amor(mochila)

#b)

def hijo_sin_amor(mochila, contador):
    if not mochila:
        return "No se encontró el anillo de poder", contador
    objeto = mochila.pop(0)
    if objeto.nombre == "Anillo de Poder":
        return "Se encontró el anillo de poder", contador
    else:
        return hijo_sin_amor(mochila, contador+1)

resultado, objetos_revisados = hijo_sin_amor(mochila, 0)
print(resultado, objetos_revisados)

#c

def hijo_sin_amor(mochila, objetos_sacados=0):
    # Si la mochila está vacía o ya se encontró el anillo de poder, se retorna el número de objetos sacados
    if not mochila or "Anillo de poder" in mochila:
        return objetos_sacados
    # Se saca el primer objeto de la mochila
    objeto_sacado = mochila.pop(0)
    # Se aumenta el contador de objetos sacados
    objetos_sacados += 1
    # Se llama recursivamente a la función con la mochila actualizada
    return hijo_sin_amor(mochila, objetos_sacados)

# Se crea la lista que representa la mochila de Namor

mochila = ["Libro antiguo", "Anillo de poder", "Tesoro escondido", "Piedra preciosa"]

# Se llama a la función y se guarda el resultado en una variable

objetos_sacados = hijo_sin_amor(mochila)

# Se imprime el resultado

print(f"Número de objetos sacados para encontrar el Anillo de poder: {objetos_sacados}")
