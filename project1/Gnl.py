#!/usr/bin/env python
import random

def G(n, l):
  '''losuje graf n-wierzcholkowy o l krawedziach (wszystkie mozliwosci rownie prawdopodobne)'''
  if l > n*(n-1)*0.5:
     raise IOError
  A = [[0] * n for i in range(n)]
  i = 0
  j = 1
  operation = 0
  for k in range(l):
    czujnik = 0
    while (i == j) or (A[i][j] == 1):
      i = random.randint(0,n-1)
      j = random.randint(0,n-1)

      czujnik += 1
      if czujnik == 10000:
         print "Wybierz inne n, l."
         return None
    A[i][j] = 1
    A[j][i] = 1
    operation +=1
  return A


def H(n,p):
  '''losuje graf n-wierzcholkowy z prawdopodobienstwem powstania kazdej krawedzi rownym p'''
  A = [[0] * n for i in range(n)]
  for i in range(n):
    for j in range(i+1, n):
      if random.random() < p:
        A[i][j] = 1
        A[j][i] = 1
  return A


if __name__=="__main__":
  from printCosts import *
  from GraphDigital import *
  from konwersje import *
  g = G(5,4)
  printCosts(g)
  wyswietl(matrixToList(g))
  print("*********************************************")
  printCosts(H(5,0.7))