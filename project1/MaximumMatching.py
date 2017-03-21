#!/usr/bin/env python
# -*- coding: utf-8 -*-

from siecPrzeplywowa import *
from konwersje import *
from MaxFlow import *

''' przyjmuje macierz sąsiedztwa grafu nieskierowanego'''
def maxMatching(Network):
    N = len(Network)
    Neighbours = matrixToList(Network)

    ''' tablica kolorowania wierzchołków '''
    ''' 0 oznacza kolor szary - wierzchołek niesprawdzony '''
    ''' 1 - kolor czerwony (pierwszy zbiór) '''
    ''' -1 - kolor niebieski (drugi zbiór) '''
    Color = [0 for i in xrange(N)]

    ''' kolejka piorytetowa '''
    Queue = collections.deque();

    ''' przejście BFS w poszukiwaniu szarych wierzchołków i oznaczaniu ich '''
    for i in range(N):
        if Color[i] == 0:
            ''' początkowa wartość '''
            Color[i] = 1

            Queue.append(i)

            while len(Queue) > 0:
                v = Queue.popleft()

                ''' sprawdzamy sąsiadów badanego wierzchołka '''
                for u in Neighbours[v]:
                    ''' jesli ma taki sam kolor, wyrzucenie błędu '''
                    if Color[u] == Color[v]:
                        print "graf nie jest dwudzielny"
                        return 0
                    '''znalezienie wierzchołka niepokolorowanego'''
                    if Color[u] == 0:
                        Color[u] = -Color[v]
                        Queue.append(u)
    print "pokolorowane", Color
    print

    ''' tworzenie sieci przepływów: dodanie źródła i końca'''
    Capacity = [[0] * (N+2) for i in xrange (N+2)]

    ''' połączenie ze źródłem zbioru czerwonego i skierowanie przepływu od czerwonych do niebieskich '''
    ''' zbiór niebieski wskazuje na koniec przepływu '''
    for i in xrange(N):
        if Color[i] == 1:
            Capacity[i+1][N+1] = 1
        else:
            for neighbour in Neighbours[i]:
                Capacity[i+1][neighbour+1] = 1
            Capacity[0][i+1] = 1



    print "Sieć: "
    printCosts(Network)
    print "Macierz pojemności:"
    printCosts(Capacity)
    print
    print "Algorytm MaxFlow:"
    maxflow, flowMatrix = MaxFlow(Capacity)
    print "Maksymalne skojarzenie: ", maxflow
    print
    print "Skojarzenia:"
    for i in range(1,N+1):
        for j in range(1,N+1):
            if Capacity[i][j] == 1 and flowMatrix[i][j]:
                print "[", i-1, "][", j-1, "]"

'''
    blue = 0
    red = 0

    for x in Color:
        if x == -1:
            blue += 1
        else:
            red += 1
    war = []
    war.append(1)
    war.append(red)
    war.append(blue)
    war.append(1)

    return Capacity, war
'''

if __name__=='__main__':

    from siecPrzeplywowa import *
    A = prostaSiecPrzeplywowa(3)
    N = len(A)

   #from GraphDigital import *
    #wyswietl(A)

    '''zamiana grafu skierowanego na nieskierowany aby otrzymać wszystkie możliwe połączenia wierzchołków'''
    for i in xrange(N):
        for j in xrange(N):
            if A[i][j] == 1:
                A[j][i] = 1

    ''' test błedu '''
    from LetItFlowNetwork import *
    B, w = LetItFlowNetwork(2)

    maxMatching(A)

'''
    newMatrix, warstwy = maxMatching(A)
    wyswietl(newMatrix, warstwy)
    printCosts(newMatrix)
'''