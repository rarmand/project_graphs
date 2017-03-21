#!/usr/bin/env python
# -*- coding: utf-8 -*-

from konwersje import *
import collections


def BFS(Matrix, Flows):

    ''' lista sąsiedztwa'''
    Neighbours = matrixToList(Matrix)
    N = len(Matrix)

    ''' tablica poprzedników '''
    Parents = [-1 for i in range(N)]
    ''' niezmiennik w celu uniknięcia identyfikacji źródła jako wierzchołka do przeglądnięcia '''
    Parents[0] = -2


    ''' pojemność przepływu na danej ścieżce '''
    Measure = [float('inf') for i in xrange(N)]


    ''' kolejka piorytetowa; sprawdzanie wierzchołków'''
    Queue = collections.deque([0])

    while len(Queue) > 0:
        x = Queue.popleft()

        '''sprawdzanie na co wskazuje badany węzeł '''
        for y in Neighbours[x]:
            if Matrix[x][y] - Flows[x][y] > 0 and Parents[y] == -1:
                Parents[y] = x
                Measure[y] = min(Measure[x], Matrix[x][y] - Flows[x][y])

                if y != N-1:
                        Queue.append(y)
                else:
                    return Measure[N-1], Parents

    return 0, Parents



''' z założenia src = 0; dest = n-1 '''
def MaxFlow(Matrix):
    N = len(Matrix)
    flow = 0
    flowMatrix = [[0]*N for i in range(N)]

    for c in range(N):
        result, ParentsTable = BFS(Matrix, flowMatrix)

        if result == 0:
            break

        flow += result

        y = N-1
        print
        while y != 0:
            x = ParentsTable[y]

            m = Matrix[x][y] - flowMatrix[x][y]
            print x, " -> [", m , "] ->", y

            flowMatrix[x][y] = flowMatrix[x][y] + result
            flowMatrix[y][x] = flowMatrix[y][x] - result

            """zabezpieczenie w razie odwrócenia się kierunku przepływu w sieci"""
            if (Matrix[x][y] == flowMatrix[x][y]):
                if x != 0 and y != N - 1:
                    val = Matrix[x][y]
                    Matrix[x][y] = Matrix[y][x]
                    Matrix[y][x] = val
            y = x
        print result
        print
    return flow, flowMatrix


if __name__=='__main__':
    import sys
    n = 4 if len(sys.argv) < 2 else min(4, max(2, int(sys.argv[1])))

    from LetItFlowNetwork import *
    M, w = LetItFlowNetwork(2)
    printCosts(M)

    r, FM = MaxFlow(M)
    wyswietl(M, w, FM)

    print
    print "Maximum flow: ", r
    print
    print "Maximum flow matrix: "
    printCosts(FM)


