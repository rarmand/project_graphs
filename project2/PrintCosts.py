# n - ile wierzchołków tworzy macierz
# matrix - macierz

# funkcja wypisuje wagi dla każdej krawędzi pomiędzy wierzchołkami

def PrintCosts(matrix, n):
    firstV = 1
    lastV = n
    for v1 in range(firstV, lastV):
        for v2 in range(firstV, lastV):
            print(matrix[v1][v2].w)
        print()
