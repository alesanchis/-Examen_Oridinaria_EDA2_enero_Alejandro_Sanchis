class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("La armadura ha sido creada con éxito.")

class Armadura:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("La armadura ha sido creada con éxito.")
    
    def calificacion(self):
        if self.nombre == "Iron Man":
            mk = self.rango.split("-")[0]
            id_coherente = self.rango.split("-")[1]
            id_siglo = self.rango.split("-")[2]
            num_armadura = self.rango.split("-")[3]
            num_escuadra = self.rango.split("-")[4]
            print("MK: ", mk)
            print("Identificacion Coherente: ", id_coherente)
            print("Identificacion de siglo: ", id_siglo)
            print("Numero de armadura: ", num_armadura)
            print("Numero de escuadra: ", num_escuadra)
        else:
            print("No es una armadura de Iron Man")

armor_1 = Armadura("Iron Man", "MK-8-8-8-8")
armor_1.calificacion()

armaduras_list = []
armaduras_list.append(Armadura("Iron Man", "MK-8-8-8-8"))
armaduras_list.append(Armadura("Iron Man", "MK-9-8-7-6"))
armaduras_list.append(Armadura("Iron Man", "MK-10-9-8-7"))

for armor in armaduras_list:
    armor.calificacion()
