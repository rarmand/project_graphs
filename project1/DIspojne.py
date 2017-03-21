#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections
from DIkonwersje import *



def listaCykli(A):
  N = len(A)

  czyWolne = [True for x in range(N)]
  cy = []
  trasa = []
  i = 0
  while len(trasa) > 0  or  i < N:
    if i < N:
      if len(trasa) != 0:
        poprz = trasa[-1]
      else:
        poprz = None

      if poprz==None or (A[poprz][i] != float('inf') and czyWolne[i]):
        trasa.append(i)
        czyWolne[i] = False

        if A[i][trasa[0]] != float('inf') and  len(trasa) >1 \
                                          and (len(trasa)!=2 or trasa[0]<i):
                                          # arbitralna reguła antyduplikacyjna
          cy.append(trasa[:])

        i = 0
    else:
      if len(trasa) > 0:
        i = trasa.pop()
        czyWolne[i] = True
    i += 1

  return cy
