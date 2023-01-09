#creación:

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

trooper = Stormtrooper("Finn", "TK-8654")

print(trooper.calificacion())  # TK-8654


#experimentacion:

stormtroopers = [    Stormtrooper("Finn", "TK-8654"),    Stormtrooper("Phasma", "FN-2187"),    Stormtrooper("Hux", "KN-1239"),]

for trooper in stormtroopers:
  print(trooper.calificacion())
