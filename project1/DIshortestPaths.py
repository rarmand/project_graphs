#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

def findAllShortestPaths(A):
  N = len(A)
  dist = [[[x, []] for x in row] for row in A] # copy distance matrix

  for k in range(N):
    for i in range(N):
      for j in range(N):
        if dist[i][j][0] > dist[i][k][0] + dist[k][j][0]:
          dist[i][j][0] = dist[i][k][0] + dist[k][j][0]
          dist[i][j][1] = dist[i][k][1] + [k] + dist[k][j][1]
          if j in dist[i][j][1]:
            d = dist[i][j][1]
            d = d[d.index(j):]+[j]
            print "Negative cycle:",
            print "-".join(map(str,d)), "with",
            d[0] = (0, d[0])
            print reduce(lambda x,y: (x[0] + dist[x[1]][y][0], y), d)[0]
            return None
  return [[x[0] for x in row] for row in dist]

if __name__=='__main__':
  import sys
  n = 20 if len(sys.argv) < 2 else int(sys.argv[1])
  l = 30 if len(sys.argv) < 2 else int(sys.argv[2])

  from printCosts import *
  from DIrandom import *
  from DIrandomizeWeights import *
  from GraphDigital2 import *

  A = losowyDigraf(n,l)
  wyswietl(A,False)

  from DIspojne import *
  from GraphSlice import *
  A = GraphSlice(A, listaSpojnychSkladowych(A)[0])
  A = randomizeWeights(A,-5,20)
  wyswietl(A)

  print "Original matrix:"
  printCosts(A)

  d = findAllShortestPaths(A)
  if d != None:
      print "Shortest distances:"
      printCosts(d)
