#!/usr/bin/env python
# -*- coding: utf-8 -*-

from siecPrzeplywowa import *
from printCosts import *
from konwersje import *

def BFS(Matrix, Flows):

    ''' lista sąsiedztwa '''
    Neighbours = matrixToList(Matrix)
    n = len(Matrix)

    ''' tablica poprzedników '''
    Parents = []
    for i in range(n):
        Parents.append(-1)
    ''' niezmiennik w celu uniknięcia identyfikacji źródła jako wierzchołka do przeglądnięcia '''
    Parents[0] = -2


    ''' pojemność przepływu na danej ścieżce '''
    Measure = []
    for i in range(n):
        Measure.append(float('inf'))
    Measure[0] = float('inf')


    ''' kolejka piorytetowa; sprawdzanie wierzchołków'''
    Queue = []
    Queue.append(0)

    while len(Queue) > 0:
        x = Queue[0]
        print Queue

        del Queue[0]

        '''sprawdzanie na co wskazuje badany węzeł '''
        for y in Neighbours[x]:
            if Matrix[x][y] - Flows[x][y] > 0 and Parents[y] == -1:
                Parents[y] = x
                Measure[y] = min(Measure[x], Matrix[x][y] - Flows[x][y])

                print Measure
                print Parents
                print Measure[n-1]

                if y != n-1:
                        Queue.append(y)
                else:
                    return Measure[n-1], Parents

    return 0, Parents



''' z założenia src = 0; dest = n-1 '''
def MaxFlow(Matrix):

    flow = 0
    flowMatrix = [[0]*n for i in range(n)]

    flag = True
    c = 0
    while c < len(Matrix):
        result, ParentsTable = BFS(Matrix, flowMatrix)

        if result == 0:
            break

        flow += result
        print flow
        y = n-1
        while y != 0:
            x = ParentsTable[y]
            flowMatrix[x][y] = flowMatrix[x][y] + result
            flowMatrix[y][x] = flowMatrix[y][x] - result
            y = x

    return flow, flowMatrix


if __name__=='__main__':
    from DIkonwersje import easyMat
    n = 2
    A,sq = siecPrzeplywowa(2, nn=2)

    from GraphDigital3 import wyswietl
    wyswietl( A, sq)

    r, FM = MaxFlow(A)
    print r
    wyswietl(FM, sq)
