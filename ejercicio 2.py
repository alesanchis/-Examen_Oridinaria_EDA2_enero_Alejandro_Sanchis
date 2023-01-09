#creacion:

class Stormtrooper:
  def __init__(self, nombre, rango):
    self.nombre = nombre
    self.rango = rango
    print(f"Stormtrooper {nombre} creado con éxito")

  def calificacion(self):
    legion = self.rango[:2]
    cohorte = self.rango[2]
    siglo = self.rango[3]
    escuadra = self.rango[4]
    trooper = self.rango[5:]
    return f"{legion}-{cohorte}{siglo}{escuadra}{trooper}"
  
  def __str__(self):
    return f"Stormtrooper {self.nombre} con rango {self.rango}"

stormtroopers = [
    Stormtrooper("Finn", "TK-8654"),
    Stormtrooper("Phasma", "FN-2187"),
    Stormtrooper("Hux", "KN-1239"),
]

for trooper in stormtroopers:
  print(trooper)

#experimentacion:

class Stormtrooper:
  def __init__(self, nombre, rango):
    self.nombre = nombre
    self.rango = rango
    print(f"Stormtrooper {nombre} creado con éxito")

  def __str__(self):
    return f"Stormtrooper {self.nombre} con rango {self.rango}"

stormtroopers = [
    Stormtrooper("Finn", "TK-8654"),
    Stormtrooper("Phasma", "FN-2187"),
    Stormtrooper("Hux", "KN-1239"),
]

for trooper in stormtroopers:
  print(trooper)
