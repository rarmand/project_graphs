#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
rnd = random.Random()

""" konwersja z grafu w digraf"""

"""zamiana zer w nieskończoności"""
def zerosToInfs(Mat):
  return [[x if x != 0 or i==j else float('inf') for j,x in enumerate(row)]
                                                for i,row in enumerate(Mat)]

def toDI(Mat):
  '''convert a graph into a digraph'''
  # ATTENTION! Symmetry isn't checked!

  """
  [ x x x
      x x
        x }
  """
  N = len(Mat)
  for i in range(N-1):
    for j in range(i+1,N):
      m = Mat[i][j]
      """ random obiera kierunek w digrafe, na którego padnie ten traci tak jakby połączenie"""
      r = rnd.randint(-1,+1)
      if   r == -1:
        Mat[i][j] = float('inf')
      elif r == +1:
        Mat[j][i] = float('inf')
  return Mat


if __name__=='__main__':

  A = zerosToInfs([[ 0, 1, 3, 0, 0],
                   [ 1, 0, 0, 0,-4],
                   [ 3, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0],
                   [ 0,-4, 0, 0, 0]])

  from printCosts import *
  print "Original graph:"
  printCosts(A)

  print "Digraph version:"
  A = toDI(A)
  printCosts(A)