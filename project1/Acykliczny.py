#!/usr/bin/python
# -*- coding: utf-8 -*-

from Kruskal import *
from Gnl import *
from konwersje import *


def DAG(n, p = 0.7):
  '''tworzenie grafu acyklicznego
  tworzy graf losowy H(n,p) jako macierz sąsiedztwa i zamienia na drzewo rozpinające przez algorytm Kruskala
  nastepnie nadaje kierunek węzłom wychodzącym z danego wierzchołka'''

  Matrix = H(n, p)
  Matrix = Kruskal(Matrix)

  N = len(Matrix)
  for i in range(N-1):
    for j in range(i+1, N):
      if Matrix[i][j] == 0:
        Matrix[i][j] = float('inf')
        Matrix[j][i] = float('inf')
      else:
        if random.randint(0,1) == 0:
          Matrix[i][j] = float('inf')
        else:
          Matrix[j][i] = float('inf')
  return Matrix


if __name__=='__main__':
  import sys

  n = 7   if len(sys.argv) < 3 else   int(sys.argv[1])
  p = 0.7 if len(sys.argv) < 3 else float(sys.argv[2])

  print "Directed acyclic graph version:"
  A = DAG(n, p)
  print matrixToList(A)
