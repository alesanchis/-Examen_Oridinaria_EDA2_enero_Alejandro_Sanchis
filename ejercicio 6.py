#copia ejercicio 1
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

#generar 2000 armaduras

import random

class Armadura:
    def __init__(self, numero_serie, legion):
        self.numero_serie = numero_serie
        self.legion = legion

    def __str__(self):
        return "Número de serie: " + str(self.numero_serie) + ", Legión: " + self.legion

def generar_armaduras():
    legiones = ["FL", "TF", "TK", "CT", "FN", "FO"]
    armaduras = []
    for i in range(2000):
        numero_serie = random.randint(1000000, 9999999)
        legion = random.choice(legiones)
        armadura = Armadura(numero_serie, legion)
        armaduras.append(armadura)
    return armaduras

armaduras_generadas = generar_armaduras()
for armadura in armaduras_generadas:
    print(armadura)

#deberá cargar los Armaduras generados en dos tablas hash encadenadas, en la primera se deberá agrupar de acuerdo con los tres últimos dígitos del código y en la segunda a partir de las iniciales de la legión

import random

armaduras = []

legiones = ["FL", "TF", "TK", "CT", "FN", "FO"]

for i in range(2000):
    codigo = random.randint(1000, 9999)
    leg = random.choice(legiones)
    armadura = "A-" + leg + "-" + str(codigo)
    armaduras.append(armadura)

tabla1 = {}
tabla2 = {}

for armadura in armaduras:
    # Agrupamiento de acuerdo con los tres últimos dígitos del código
    ultimos_digitos = armadura[-3:]
    if ultimos_digitos not in tabla1:
        tabla1[ultimos_digitos] = []
    tabla1[ultimos_digitos].append(armadura)

    # Agrupamiento a partir de las iniciales de la legión
    iniciales = armadura[2:4]
    if iniciales not in tabla2:
        tabla2[iniciales] = []
    tabla2[iniciales].append(armadura)


#determinar si el Armaduras FN-2187 está cargado para poder quitarlo porque es un trai dor desertor,
#Utilizar una tabla hash encadenada para agrupar las armaduras según las iniciales de la legión.
#Recorrer la tabla hash encadenada buscando la legión "FN"
#Una vez encontrado la legión "FN", recorrer la lista encadenada buscando el código "FN-2187"
#Si se encuentra el código "FN-2187", eliminar el armadura de la lista encadenada y de la tabla hash encadenada
#Si no se encuentra el código "FN-2187", imprimir un mensaje indicando que no se encuentra la armadura.

class Armadura:
    def __init__(self, código, legión):
        self.código = código
        self.legión = legión

class TablaHash:
    def __init__(self):
        self.tabla = [[] for _ in range(1000)]
        
    def hash(self, código):
        return int(código[-3:])
    
    def agregar(self, armadura):
        index = self.hash(armadura.código)
        self.tabla[index].append(armadura)
        
    def buscar(self, código):
        index = self.hash(código)
        for armadura in self.tabla[index]:
            if armadura.código == código:
                return armadura
        return None
    
    def eliminar(self, código):
        armadura = self.buscar(código)
        if armadura:
            index = self.hash(código)
            self.tabla[index].remove(armadura)

tabla_hash = TablaHash()

# Generación de armaduras
for _ in range(2000):
    código = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    legión = random.choice(["FL", "TF", "TK", "CT", "FN", "FO"])
    armadura = Armadura(código, legión)
    tabla_hash.agregar(armadura)

# Determinar si la armadura FN-2187 está cargada
armadura = tabla_hash.buscar("FN-2187")
if armadura:
    print("La armadura FN-2187 está cargada.")
    tabla_hash.eliminar("FN-2187")
    print("La armadura FN-2187 ha sido eliminada.")
else:
    print("La armadura FN-2187 no está cargada.")

armadura = tabla_hash.buscar("781")
if armadura:
    print("Todas estas armaduras han sido asignados a una mision de asalto.")
else:
    print("No hay armaduras con el término 781.")

armadura = tabla_hash.buscar("537")
if armadura:
    print("Todas estas armaduras han sido asignados a una mision de exploracion.")
else:
    print("No hay armaduras con el término 537.")

# Acceder a la tabla hash encadenada de las legiones
legiones_hash = {
    "FL": [],
    "TF": [],
    "TK": [],
    "CT": [],
    "FN": [],
    "FO": []
}

# Obtener armaduras de la legión CT
armaduras_CT = []
for armadura in legiones_hash["CT"]:
    armaduras_CT.append(armadura)

# Obtener armaduras de la legión TF
armaduras_TF = []
for armadura in legiones_hash["TF"]:
    armaduras_TF.append(armadura)

# Imprimir armaduras obtenidas
print("Armaduras de la legión CT:", armaduras_CT)
print("Armaduras de la legión TF:", armaduras_TF)

