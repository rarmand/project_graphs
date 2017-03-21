
def matrixToList(Mac):
  N = len(Mac)
  List = [[] for x in range(N)]
  for i in range(N):
    for j in range(N):
      m = Mac[i][j]
      if m != 0 and m != float('inf'): # jest polaczenie, wiec zapisz sasiada
        List[i].append(j)
  return List

def listToMatrix(List):
  N = len(List)
  Matrix = [[0 for x in range(N)] for x in range(N)]
  for i in range(N):
    for elem in List[i]: # polacz z kazdym sasiadem
      Matrix[i][elem] = 1
  return Matrix

def matSasToMatIn(MatSas):
  K = len(MatSas)
  N = len(MatSas[0])
  MatIn = []
  for i in range(N):
    for j in range(i+1,N):
      if MatSas[i][j] == 1:
        MatIn.append([0 for x in range(N)]) # nowy wiersz z krawedzia
        MatIn[-1][i] = 1 # zaznaczyc, co takiego laczy
        MatIn[-1][j] = 1
  return MatIn

def matInToMatSas(MatIn):
  N = len(MatIn[0])
  MatSas = [[0 for x in range(N)] for x in range(N)]
  for kr in MatIn:
    i = kr.index(1)
    j = kr[(i+1):].index(1) + i+1
    MatSas[i][j] = 1
    MatSas[j][i] = 1
  return MatSas

def listToMatIn(List):
  N = len(List)
  MatIn = []
  for n in range(N):
    for e in List[n]:
      if n < e: # odpowiednik `j in range(i+1,N)`
        MatIn.append([0 for x in range(N)])
        MatIn[-1][n] = 1
        MatIn[-1][e] = 1
  return MatIn

def matInToList(MatIn):
  N = len(MatIn[0])
  List = [[] for x in range(N)]
  for kr in MatIn:
    i = kr.index(1)
    j = kr[(i+1):].index(1) + i+1
    List[i].append(j)
    List[j].append(i)
  return List


if __name__=='__main__':
    from printCosts   import *
    from GraphDigital import *

    #startGraf()

    am = [[0,1,1,0,0], [1,0,0,0,1], [1,0,0,0,0], [0,0,0,0,0], [0,1,0,0,0]]
    printCosts(am)
    al = matrixToList(am)
    am = listToMatrix(al)
    print '\n', 'Lista z Macierzy:', al

    wyswietl(al)

    print 'Macierz z Listy:'
    printCosts(am)

    ai = matSasToMatIn(am)
    print '\n', 'Incydencji z Macierzy:', ai, '\n'
    am = matInToMatSas(ai)
    printCosts(am)
    print '\n\n', 'Lista:', al
    wyswietl(al)
    ai = listToMatIn(al)
    print '\n', 'Incydencji z Listy:', ai
    al = matInToList(ai)
    print '\n', 'Lista z Incydencji:', al

    wyswietl(al)

    #stopGraf()
