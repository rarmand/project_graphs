#n - numer ostatniego wierzchołka

def TheShortestPath(matrix, v1, v2):
    rev_list = [v2]
    cost = matrix[v1][v2]
    elem = v2
    while elem != v1:
        elem = matrix[elem][v2].s
        rev_list.append(elem)
    result = []
    for r in reverse(rev_list):
        result.append(r)
    return result

def PrintTheShortestPath(matrix, n):
    firstV = 1
    lastV = n
    for v1 in range(firstV, lastV-1):
        for v2 in range(v1+1, lastV):
            print(TheShortestPath(v1,v2))

