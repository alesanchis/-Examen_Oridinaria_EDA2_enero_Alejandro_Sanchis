
def usar_la_fuerza(mochila, objetos_sacados=0):
 
  if not mochila:
    return (False, objetos_sacados)

  if "sable de luz" in mochila:
    return (True, objetos_sacados + 1)
  
  return usar_la_fuerza(mochila[1:], objetos_sacados + 1)

mochila = ["pistola", "cargadores", "sable de luz", "granada", "mechero", "telefono"]
encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
  print(f"El sable de luz fue encontrado después de sacar {objetos_sacados} objetos de la mochila")
else:
  print("El sable de luz no fue encontrado en la mochila")
