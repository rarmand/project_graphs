#!/usr/bin/env python3.4
    
def CanBeDrawn(lista):
  '''sprawdza, czy dany graf da sie narysowac, a jesli tak, zwraca przykladowa macierz sasiedztwa'''
  suma = 0
  for elem in lista:
    suma += elem
  if suma%2 != 0:
    return False
  lista.sort()

  n = len(lista)
  A = [[0] * n for i in range(n)]
  i = 0
  k = n-1
  li = [[elem,i] for i,elem in enumerate(lista)]
  while k > 0:
    ile = li[k][0]
    if k-ile < 0:
      return False
    for j in range(k-ile, k):
      li[j][0] -= 1
      if li[j][0] < 0:
        return False
      A[ li[k][1] ][ li[j][1] ] = 1
      A[ li[j][1] ][ li[k][1] ] = 1
    k -= 1
    lista.sort()
  return A


if __name__=="__main__":
  listaMa = [4,2,2,3,1]
  print(CanBeDrawn(listaMa))


