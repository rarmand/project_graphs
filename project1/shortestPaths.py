#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy


""" wyszukuje najkrótsze ścieżki między wierzchołkami biorąc pod uwage ich kierunek"""


def findAllShortestPaths(A):
  N = len(A)
  dist = copy.deepcopy(A) # copy distance matrix

  for k in range(N):
    for i in range(N):
      for j in range(N):
        if dist[i][j] > dist[i][k] + dist[k][j]:  # if can be better, make it better
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist

if __name__=='__main__':
  from printCosts import *
  #m = [[0, 3, 10, float('inf')],
  #     [3, 0, 4, 10],
  #     [10, 4, 0, 14],
  #     [float('inf'), 10, 14, 0]]

  m = [[ 0, 5, 1, float('inf'),10, 4, float('inf')],
       [ 5, 0, 2, float('inf'), float('inf'), float('inf'), 1],
       [ 1, 2, 0, 1, float('inf'), float('inf'), float('inf')],
       [ float('inf'), float('inf'), 1, 0, 4, 1, float('inf')],
       [10, float('inf'), float('inf'), 4, 0, 1, float('inf')],
       [ 4, float('inf'), float('inf'), 1, 1, 0, 2],
       [ float('inf'), 1, float('inf'), float('inf'), float('inf'), 2, 0]]


  print "Original matrix:"
  printCosts(m)
  d = findAllShortestPaths(m)
  print "Shortest distances:"
  printCosts(d)

