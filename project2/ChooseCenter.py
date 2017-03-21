#n - numer ostatniego wierzchołka

def ChooseCenter(matrix, n):
    center = 0
    cost = sys.maxint
    firstV = 1
    lastV = n
    for v1 in range(firstV, lastV):
        v_cost = 0
        for v2 in range(firstV, lastV):
            v_cost = v_cost + matrix[v1][v2]
        if(v_cost < cost):
            cost = v_cost
            center = v1
    return (center, cost)
