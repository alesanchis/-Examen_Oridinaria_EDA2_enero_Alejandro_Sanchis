
def mochila_01(pesos, precios, peso_maximo):
    n = len(pesos)
    matriz = [[0 for _ in range(peso_maximo + 1)] for _ in range(n + 1)]

   
    for i in range(1, n + 1):
        
        for w in range(1, peso_maximo + 1):
           
            if pesos[i - 1] > w:
                matriz[i][w] = matriz[i - 1][w]
            
            else:
                matriz[i][w] = max(matriz[i - 1][w], matriz[i - 1][w - pesos[i - 1]] + precios[i - 1])

    return matriz[n][peso_maximo]

precios = [103, 60, 70, 5, 15]
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100

valor_maximo = mochila_01(pesos, precios, peso_maximo)
print(f"El valor máximo de los artículos que se pueden agregar a la mochila es {valor_maximo}.")
