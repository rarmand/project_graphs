#!/usr/bin/python

from Dijkstra import *
from DIshortestPaths import *

def potencjal(A):
    N = len(A)
    B = copy.deepcopy(A)
    for i in B:
        i.append(float('inf'))
    B.append([0 for i in range(N+1)])
    d = findAllShortestPaths(B)
    if not d:
        return None
    return d

def Johnson(A):

    printCosts(A)

    N = len(A)
    d = potencjal(A)
    if not d:
        return None
    for v in range(N):
        for u in range(N):
            A[u][v] = A[u][v] + d[-1][u] - d[-1][v]
    print
    printCosts(A)

    d2 = []
    for u in range(N):
        d2 = Dijkstra(u,A)
    #for u in range(N):
    #    dfg = Dijkstra(u,A)
    # BLAD dla u=1

    #for v in range(N):
    # A[u][v] = d2[v] + d[-1][u] - d[-1][v]
    return A

from printCosts import *
from DIrandom import *
from DIrandomizeWeights import *
from GraphDigital import *

if __name__=='__main__':
    A = [[float('inf'), float('inf'), 1, 7, float('inf')],
        [4, float('inf'), float('inf'), float('inf'), float('inf')],
        [float('inf'),-5, float('inf'), float('inf'), 2],
        [float('inf'), float('inf'), 6, float('inf'), float('inf')],
        [3, 8, float('inf'),-4, float('inf')]]

    A = Johnson(A)
