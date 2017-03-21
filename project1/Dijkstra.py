#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Dijkstra(s, A):
   '''Oblicza najkrótszą drogę od s do każdego wierzchołka A, a także podaje dla każdego wierzchołka poprzedni wierzchołek na najkrótszej trasie.'''
   n = len(A)

   for i in range(n):
      for j in range(n):
         if A[i][j] < 0:
            print("BLAD: algorytm Dijkstry nie dozwala na ujemne wagi")
            return None

   Q = []
   ''' Q - zbiór wierzchołków do których dotarł już algorytm ale nie ustalono jeszcze najkrótszej ścieżki'''
   S = []
   ''' S - zbiór wierzchołków o już ustalonej najkrótszej scieżce, dalej juz nie będą rozpatrywane'''
   D = []
   ''' D - przechowuje wartości aktualnie najkrótszej ścieżki od źródła do węzła i'''
   P = []
   ''' P - przechowuje indeks węzła, który jest poprzednikiem węzła i na najkrótszej ścieżce od źródła do i'''

   D = [float('inf') for x in range(n+1)]  # n wartości zwykłych oraz jeden strażnik
   D[s] = 0

   P = [0 for x in range(n)]
   Q = [s]

   while len(S) < n:
      mini = len(D)-1  # strażnik w postaci nieskończoności
      for i in Q:
          print("CLICK:", i, Q)

          if (D[i] <= D[mini]) and (i not in S):
              mini = i
              print("cos")
      print "mini", mini
      S.append(mini)
      print("Q", Q)
      Q.remove(mini)
      print
      print
      for j in range(n):
         print j
         if (A[mini][j] != 0) and (j not in S):
            print A
            if (D[mini] + A[mini][j]) < D[j]:
               D[j] = D[mini] + A[mini][j]
               P[j] = mini
               print "J", j
               if j not in Q:
                  Q.append(j)
      print "ola", Q
      print
   D.pop()  # usuwamy strażnika
   return D, P


if __name__=='__main__':
    M = [[ 0, 5, 1, 0,10, 4, 0],
         [ 5, 0, 2, 0, 0, 0, 1],
         [ 1, 2, 0, 1, 0, 0, 0],
         [ 0, 0, 1, 0, 4, 1, 0],
         [10, 0, 0, 4, 0, 1, 0],
         [ 4, 0, 0, 1, 1, 0, 2],
         [ 0, 1, 0, 0, 0, 2, 0]]

    A = [[float('inf'), float('inf'), 0, 10, float('inf')],
         [0, float('inf'), float('inf'), float('inf'), float('inf')],
         [float('inf'), 0, float('inf'), float('inf'), 2],
         [float('inf'), float('inf'), 2, float('inf'), float('inf')],
         [4, 13, float('inf'), 0, float('inf')]]

    d = Dijkstra(1,A)
    print(d)
    #for i in range(len(M)):
    #   print i
       #d = Dijkstra(i,A)
    #   print "wagi:", d[0]
     #  print "poprzednicy:", d[1]
