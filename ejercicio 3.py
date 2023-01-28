class ArtefactosValiosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
valioso = ArtefactosValiosos(3, "Ring of power", 1000, "2022-12-31")
print(valioso.peso)
print(valioso.nombre)
print(valioso.precio)
print(valioso.fecha_caducidad)

class ArtefactosValiosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print("El artefacto valioso ha sido creado con éxito.")

valioso = ArtefactosValiosos(3, "Ring of power", 1000, "2022-12-31")

class ArtefactosValiosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print("El artefacto valioso ha sido creado con éxito.")
        
    def __str__(self):
        return f'Nombre: {self.nombre} \nPeso: {self.peso} \nPrecio: {self.precio} \nFecha de caducidad: {self.fecha_caducidad}'

valioso = ArtefactosValiosos(3, "Ring of power", 1000, "2022-12-31")
print(valioso)

ring_of_power = ArtefactosValiosos(3, "Ring of power", 1000, "2022-12-31")
necklace_of_wisdom = ArtefactosValiosos(2, "Necklace of wisdom", 800, "2023-06-30")
amulet_of_protection = ArtefactosValiosos(1, "Amulet of protection", 500, "2022-09-15")

artefactos = [ArtefactoValioso("Jarabe de arce", 2.5, 12.50, "2022-12-31"),              ArtefactoValioso("Miel de abeja", 1.5, 8.75, "2022-09-15"),              ArtefactoValioso("Mermelada de frutas", 3.0, 15.00, "2022-05-31")]

artefactos_ordenados = sorted(artefactos, key=lambda x: x.fecha_caducidad)

for artefacto in artefactos_ordenados:
  print(artefacto)

# modificar el precio de un artefacto valioso
artefactos[0].precio = 14.99
