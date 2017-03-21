#!/usr/bin/env python3.4
import random
import Gnl

def RandomizeGraph(A, ip):
  n = len(A)
  for i in range(ip):
    a,b,c,d = 0,1,2,3
    czujnik1 = 0
    while a==c or b==d or a==d or b==c or ((A[a][c] == 0) and (A[b][d] == 0)) or ((A[a][d] == 0) and (A[b][c] == 0)):
      a = random.randint(0,n-1)
      b = random.randint(0,n-1)
      c = random.randint(0,n-1)
      d = random.randint(0,n-1)
      czujnik2 = 0
      while (a == b) or (A[a][b] == 0):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        czujnik2 += 1
        if(czujnik2 > 1000):
          raise Exception("To na pewno randomizowalne, lol?")
      czujnik2 = 0
      while (c == d) or (A[c][d] == 0):
        c = random.randint(0,n-1)
        d = random.randint(0,n-1)
        czujnik2 += 1
        if(czujnik2 > 1000):
          raise Exception("To na pewno randomizowalne, lol?")
      czujnik1 += 1
      if(czujnik1 > 1000):
        raise Exception("To na pewno randomizowalne, lol?")
     
    if (A[a][c] == 0) and (A[b][d] == 0):
      A[a][c] = A[c][a] = 1
      A[b][d] = A[d][b] = 1
    else:
      A[a][d] = A[d][a] = 1
      A[b][c] = A[c][b] = 1
  
    A[a][b] = A[b][a] = 0
    A[c][d] = A[d][c] = 0
  return A

if __name__=="__main__":
  a = Gnl.G(10,12)
  print(RandomizeGraph(a, 4))
