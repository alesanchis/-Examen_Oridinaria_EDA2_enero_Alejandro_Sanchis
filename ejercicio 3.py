
#creacion:

class ArtefactoValioso:
  def __init__(self, peso, nombre, precio, fecha_caducidad):
    self.peso = peso
    self.nombre = nombre
    self.precio = precio
    self.fecha_caducidad = fecha_caducidad
    print(f"Artefacto valioso {nombre} creado con éxito")

  def __str__(self):
    return f"{self.nombre}: peso {self.peso}, precio {self.precio}, fecha de caducidad {self.fecha_caducidad}"

artefacto = ArtefactoValioso(5, "Anillo de oro", 1000, "01/01/2025")
print(artefacto)

#experimentacion:

artefactos = [
    ArtefactoValioso(5, "Anillo", 1000, "01/01/2025"),
    ArtefactoValioso(10, "Rolex", 5000, "01/01/2022"),
    ArtefactoValioso(1, "Ordenador portátil", 2000, "01/01/2023"),
]


artefactos.sort(key=lambda x: x.fecha_caducidad)
for artefacto in artefactos:
  print(artefacto)


artefactos[0].precio = 1500
print(artefactos[0])
