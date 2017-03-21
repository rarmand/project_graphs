#!/usr/bin/python

import random

def LetItFlowNetwork(N):
  warstwy = [[0]]  # zawiera zrodlo
  w = 1  # numer wierzcholka

  for i in xrange(1,N+1):
    ra = random.randint(2,N)
    warstwy.append([w+i for i in xrange(ra)])  # dodawanie warstwy
    w += ra

  warstwy.append([w])  # dodanie ujscia
  A = [[float('inf') if i != j else 0
      for i in xrange(w+1)] for j in xrange(w+1)]

  for i in xrange(len(warstwy)-1):  # z kazdego z warstwy i wychodzi krawedz do warstwy i+1
    for j in warstwy[i]: 
      if len(warstwy[i+1]) < 2:
        A[j][warstwy[i+1][0]] = random.randint(1, 10)
      else:
        ra = random.randint(warstwy[i+1][0], warstwy[i+1][-1])
        A[j][ra] = random.randint(1, 10)

  for i in xrange(1, len(warstwy)-1):  # do kazdego z warstwy i+1 wchodzi krawedz do warstwy i
    for j in warstwy[i]:
      for k in range(len(warstwy)-1):  # sprawdzenie, czy istnieje juz takie polaczenie
        if A[i][j] != float('inf'):
          if i==j:
            continue
          break
      else:  # jesli petla nie znajdzie krawedzi to ja dodaje
        if len(warstwy[i-1]) < 2:
          A[warstwy[i-1][0]][j] = random.randrange(1,10)
        else:
          ra = random.randint(warstwy[i-1][0], warstwy[i-1][-1])
          A[ra][j] = random.randint(1,10)

  for i in range(2*N):
    a,b = random.randint(0,w), random.randint(1,w+1)
    while a==b or A[a][b] != float('inf'):
      a,b = random.randint(0,w), random.randint(1,w+1)

    A[a][b] = random.randint(1,10)
  return A, map(len, warstwy)

if __name__=='__main__':
  import sys
  N = 2 if len(sys.argv) < 2 else min(int(sys.argv[1]), 2)
  A, w = LetItFlowNetwork(N)

  from GraphDigital3 import *
  wyswietl(A, w)
