#!/usr/bin/python
import random
from printCosts import *
from GraphDigital3 import *

def LetItFlowNetwork(N):
  warstwy = []
  warstwy.append([])
  warstwy[0].append(0) # dodawanie zrodla
  w = 1 # numer wierzcholka
  for i in xrange(1,N+1):
    warstwy.append([]) # dodawanie warstwy
    if N==2: # bo randrange nie ogarnia przedzialu (2,2)
      warstwy[i].append(w)
      w += 1
      warstwy[i].append(w)
      w += 1
    else:
      for j in xrange(random.randrange(2,N+1)):
        warstwy[i].append(w)
        w += 1
  warstwy.append([])
  warstwy[N+1].append(w) # dodanie ujscia
  A = [[float('inf') for i in range(w+1)] for j in range(w+1)]
  for i in range(w+1):
    A[i][i] = 0
  for i in range(len(warstwy)-1): # z kazdego z warstwy i wychodzi krawedz do warstwy i+1
    for j in warstwy[i]:
      if len(warstwy[i+1]) < 2:
        A[j][warstwy[i+1][0]] = random.randrange(1,10)
      else:
        A[j][random.randrange(warstwy[i+1][0],warstwy[i+1][-1])] = random.randrange(1,10)
  for i in range(1,len(warstwy)-1): # do kazdego z warstwy i+1 wchodzi krawedz do warstwy i
    for j in warstwy[i]:
      for k in range(len(warstwy)-1): # sprawdzenie, czy istnieje juz takie polaczenie
        if A[i][j] != float('inf'):
          if i==j:
            continue
          break
      else: # jesli petla nie znajdzie krawedzi to ja dodaje
        if len(warstwy[i-1]) < 2:
          A[warstwy[i-1][0]][j] = random.randrange(1,10)
        else:
          A[random.randrange(warstwy[i-1][0], warstwy[i-1][-1])][j] = random.randrange(1,10)
  for i in range(2*N):
    a,b = random.randrange(0,w), random.randrange(1,w+1)
    while a==b or A[a][b]!=float('inf'):
      a,b = random.randrange(0,w), random.randrange(1,w+1)
    A[a][b] = random.randrange(1,10)
  return A,map(len,warstwy)

if __name__=='__main__':
  import sys
  N = 2 if len(sys.argv) < 2 else int(sys.argv[1])
  if N < 2:
    N = 2
  A,w = LetItFlowNetwork(N)
  print w
  printCosts(A)
  wyswietl(A,w)
