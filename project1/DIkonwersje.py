#!/usr/bin/env python
# -*- coding: utf-8 -*-

def easyMat(Mat):
  return [[x if x!=None else float('inf') for x in row] for row in Mat]


''' oblicza długość jednej współrzędnej macierzy
    jedzie po macierzy -> x i y
    pobiera wartość z macierzy
        jeśli i != j i istnieje połączenie
    dodajemy elem do listy pod indeks i z dopiską łączonego wierzchołka'''
def matrixToList(Mac):
  N = len(Mac)
  List = [[] for x in range(N)]
  for i in range(N):
    for j in range(N):
      cost = Mac[i][j]
      if i != j  and  cost != float('inf'):
        # koszt nieskończony oznacza brak połączenia
        List[i].append((j, cost))
  return List

''' oblicza długość listy
    tworzy macierz z braków połączeń o dł listy
    uzupełnia macierz:
        wartość na diagonali oznacza jako 0
        pobiera z listy oba elementy dla danego i
        łączy elem z i i wstawia odpowiednie połaczenie cost'''
def listToMatrix(List):
  N = len(List)
  Matrix = [[float('inf') for x in range(N)] for x in range(N)]
  for i in range(N):
    Matrix[i][i] = 0
    for elem,cost in List[i]: # polacz z kazdym sasiadem
      Matrix[i][elem] = cost
  return Matrix

''' macierz sąsiedztwa w macierz incydencji
    pobiera długość wiersza 0 macierzy
    uzupełnia macierz incydencji jadąc po długości pierwszego wiersza
        pobiera COST z macierzy sas
        jeśli i != j i istnieje połączenie między wierzchołkami:
            MatIn dodaje krawędź
                0 dla wszystkich wierzchołków (dł N) i koszt
                określa kierunek'''
def matSasToMatIn(MatSas):
  N = len(MatSas[0])
  MatIn = []
  for i in range(N):
    for j in range(N):
      cost = MatSas[i][j]
      if i != j  and  cost != float('inf'):
        MatIn.append(([0 for x in range(N)], cost)) # krawędź = koszt + końce
        MatIn[-1][0][i] = -1  # kierunek z - do +
        MatIn[-1][0][j] = +1
  return MatIn

''' macierz incydencji w macierz sąsiedztwa
    oblicza ilość wierzchołków
    tworzy macierz sąsiedztwa z brakiem połączeń
    pobiera krawędź i bada jej zwrot
    przypisuje odpowiendnio do wierzchołków ten zwrot
    wstawia koszt'''
def matInToMatSas(MatIn):
  N = len(MatIn[0][0])
  MatSas = [[float('inf') for x in range(N)] for x in range(N)]
  for kr,cost in MatIn:
    i = kr.index(-1)
    j = kr.index(+1)
    MatSas[i][j] = cost
  return MatSas

''' lista do macierzy incydencji
    pobiera długość listy (ile wierzchołków)
    jedzie po wierzchołkach i tworzy macierz incydencji:
        pobiera połączeniowy wierzchołek i koszt połączenia z listy dla danego n
        dodaje do Incydencji krawędź (wiersz) i nadaje mu koszt
        określa jej zwrot'''
def listToMatIn(List):
  N = len(List)
  MatIn = []
  for n in range(N):
    for e,cost in List[n]:
      MatIn.append(([0 for x in range(N)], cost))
      MatIn[-1][0][n] = -1
      MatIn[-1][0][e] = +1
  return MatIn


''' macierz incydencji do listy '''
''' pobiera ilość wierzchołków
    tworzy listę list
    pobiera krawędź i nadaje jej kierunek +/-
    dodaje do listy pod wierzchołkiem i wierzchołek j i koszt '''
def matInToList(MatIn):
  N = len(MatIn[0][0])
  List = [[] for x in range(N)]
  for kr,cost in MatIn:
    i = kr.index(-1)
    j = kr.index(+1)
    List[i].append((j,cost))
  return List


if __name__=='__main__':
    from printCosts   import *
    from GraphDigital import *


    am = easyMat([[None,  -2,   3,None,None],
                  [   1,None,None,None,   1],
                  [   3,None,None,None,None],
                  [None,None,None,None,None],
                  [None,  -4,None,None,None]])

    printCosts(am)
    wyswietl(am)

    al = matrixToList(am)
    am = listToMatrix(al)
    print '\nLista z Macierzy:', al
    print 'Macierz z Listy:'
    printCosts(am)
    wyswietl(am)

    ai = matSasToMatIn(am)
    print '\nIncydencji z Macierzy:', ai, '\n'
    am = matInToMatSas(ai)
    print '\nSąsiedztwa z Incydencji:'
    printCosts(am)
    wyswietl(am)
    print '\n\n', 'Lista:', al
    ai = listToMatIn(al)
    print '\n', 'Incydencji z Listy:', ai
    al = matInToList(ai)
    print '\n', 'Lista z Incydencji:', al