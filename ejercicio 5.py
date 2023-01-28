precio = [103, 60, 70, 5, 15]
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100

n = len(precio)

tabla = [[0 for x in range(peso_maximo + 1)] for x in range(n + 1)]

for i in range(n + 1):
    for w in range(peso_maximo + 1):
        if i == 0 or w == 0:
            tabla[i][w] = 0
        elif pesos[i-1] <= w:
            tabla[i][w] = max(precio[i-1] + tabla[i-1][w-pesos[i-1]], tabla[i-1][w])
        else:
            tabla[i][w] = tabla[i-1][w]

print(tabla[n][peso_maximo])

