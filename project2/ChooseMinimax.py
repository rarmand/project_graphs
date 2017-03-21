#n - numer ostatniego wierzchołka

def ChooseMiniMax(matrix, n):
    vertex = 0
    minimax = sys.maxint
    firstV = 1
    lastV = n
    for v1 in range(firstV, lastV):
        v_minimax = 0
        for v2 in range(firstV, lastV):
            if matrix[v1][v2] > v_minimax:
                v_minimax = matrix[v1][v2]
        if v_minimax < minimax:
            minimax = v_minimax
            vertex = v1
    return (vertex, minimax)