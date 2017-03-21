#!/usr/bin/env python
# -*- coding: utf-8 -*-

from konwersje import *
import copy

def szukajPetli(li, u, S, k=None):
   if k == None:
      k = u

   if li[u] == []:
      return None

   S.append(u)
   if k in li[u]:
      # S jest znalezioną pętlą
      return S
   else:
      for i in li[u]:
         # szukamy pętli z sąsiada i
         li[u].remove(i)
         li[i].remove(u)
         newS = szukajPetli(li,i,S,k)
         li[u].append(i)
         li[i].append(u)

         # jeśli znaleziono jakąś kontynuację, zwracamy ją dalej
         if newS != None:
            break
      else:
         return None
   return newS

def Euler(li, u=0):
   '''zwraca cykl Eulera bądź None, gdy taki nie istnieje'''

   li = copy.deepcopy(li)  # dla bezpieczeństwa
   cykl = []

   while 1:
      S = []
      petla = szukajPetli(li, u, S, u)
      if petla == None:
         return None

      # wyrzucamy połączenia pomiędzy sąsiednimi elementami pętli
      petla.append(petla[0])
      reduce(lambda i,j: [li[i].remove(j), li[j].remove(i), j][-1], petla)
      petla.pop()

      if cykl == []:  # jeśli cyklu nie było, pętla jest całym cyklem
         cykl = petla
      else:           # jeśli cykl był, dodajemy go w rozpatrywanym wierzchołku
         ind = cykl.index(u)
         cykl = cykl[:ind] + petla + cykl[ind:]

      # jeśli sprawdzono już wszystkie krawędzie, zwróć uzyskany cykl
      if li == [[] for x in li]:
         return cykl

      # za nowego kandydata wybierz kolejny wierzchołek, dla którego są niesprawdzone krawędzie
      u = next((i for i,x in enumerate(li) if x != []), u)
   return cykl


if __name__=='__main__':
   l = [[0,1,1,0,1,1],
        [1,0,1,0,0,0],
        [1,1,0,1,1,0],
        [0,0,1,0,1,0],
        [1,0,1,1,0,1],
        [1,0,0,0,1,0]]

   l = matrixToList(l)

   print Euler(l)