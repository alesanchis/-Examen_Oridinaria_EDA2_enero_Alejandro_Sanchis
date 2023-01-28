class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("La armadura ha sido creada con éxito.")

    def calificacion(self):
        print("La armadura ha sido clasificada como " + self.rango)
    
    def __str__(self):
        return self.nombre + " con clasificación " + self.rango

armaduras_list = []
armaduras_list.append(Armadura("Iron Man", "MK-8-8-8-8"))
armaduras_list.append(Armadura("Iron Man", "MK-9-8-7-6"))
armaduras_list.append(Armadura("Iron Man", "MK-10-9-8-7"))

for armor in armaduras_list:
    print(armor)

#experimentacion

class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("La armadura ha sido creada con éxito.")

    def __str__(self):
        return "Nombre: " + self.nombre + ", Rango: " + self.rango

armaduras_list = []
armaduras_list.append(Armadura("Iron Man", "MK-8-8-8-8"))
armaduras_list.append(Armadura("Iron Man", "MK-9-8-7-6"))
armaduras_list.append(Armadura("Iron Man", "MK-10-9-8-7"))

for armor in armaduras_list:
    print(armor)

armaduras_list = []
armaduras_list.append(Armadura("Iron Man", "MK-8-8-8-8"))
armaduras_list.append(Armadura("Iron Man", "MK-9-8-7-6"))
armaduras_list.append(Armadura("Iron Man", "MK-10-9-8-7"))
armaduras_list.append(Armadura("Iron Man", "MK-11-9-8-7"))
armaduras_list.append(Armadura("Iron Man", "MK-12-9-8-7"))

for armor in armaduras_list:
    print(armor)

for armor in armaduras_list:
    print(armor.__str__())