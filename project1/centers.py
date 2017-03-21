#!/usr/bin/python
# -*- coding: utf-8 -*-

def chooseMiniMax(M):
  N = len(M)
  A = findAllShortestPaths(M)

  ver = 0
  minimax = float('inf')

  for i in range(N):
    v_minimax = 0
    for j in range(N):  # wyznacz maksymalną odległość
      if A[i][j] > v_minimax:
        v_minimax = A[i][j]

    if v_minimax < minimax:  # sprawdź, czy jest krótsza od minimalnej maksymalnej
      minimax = v_minimax
      ver = i
  return (ver, minimax)

def chooseCenter(M):
  N = len(M)
  A = findAllShortestPaths(M)

  ver = 0
  suma = float('inf')

  for i in range(N):
    v_suma = 0
    for j in range(N):
      v_suma += A[i][j]
    if v_suma < suma:
      suma = v_suma
      ver = i
  return (ver, suma)

if __name__=='__main__':
    from losowyZWagami import *
    from shortestPaths import *
    import sys

    # UWAGA! n,l to wartości STARTOWE, nie docelowe!
    n = 5 if len(sys.argv) < 2 else int(sys.argv[1])
    l = 5 if len(sys.argv) < 2 else int(sys.argv[2])

    A = losowyZWagami(n,l)
    A = [[ 0, 5, 1, float('inf'),10, 4, float('inf')],
                    [ 5, 0, 2, float('inf'), float('inf'), float('inf'), 1],
                           [ 1, 2, 0, 1, float('inf'), float('inf'), float('inf')],
                                  [ float('inf'), float('inf'), 1, 0, 4, 1, float('inf')],
                                         [10, float('inf'), float('inf'), 4, 0, 1, float('inf')],
                                                [ 4, float('inf'), float('inf'), 1, 1, 0, 2],
                                                       [ float('inf'), 1, float('inf'), float('inf'), float('inf'), 2, 0]]

    print "Center:",  chooseCenter(A)
    print "MiniMax:", chooseMiniMax(A)

    from GraphDigital2 import *
    from konwersje import *
    wyswietl(A)