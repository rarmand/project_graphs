import copy


B = [[0,1,0,0,1,0],
     [1,0,1,0,1,0],
     [0,1,0,1,0,0],
     [0,0,1,0,1,1],
     [1,1,0,1,0,0],
     [0,0,0,1,0,0]]

bv = [1,2,3,4,5,6]

vertex = [1,2,3]

A = [[0,1,0],
     [1,0,1],
     [0,1,0]]


cv = [1,2,3,4]

C = [[0,1,1,0],
     [1,0,0,0],
     [1,0,0,0],
     [0,0,0,0]]


HAM = [[0,1,0,0],
       [1,0,1,0],
       [0,1,2,0],
       [0,0,0,0]]

vHAM = [1,2,3,4]

def IsHamFromVer(vertex, vertexList, A, checkList):

    flag = False
    checkList.append(vertex)

    #do listy wierzchołków cyklu hamiltona dodajemy badany wierzchołek
    print(checkList)
    print(len(checkList))

    #sytuacja gdy dochodzimy do "końca" listy (zostaje tylko jeden wierzchołek do sprawdzenia)
    if len(vertexList) == 1:
        if A[vertex-1][vertexList[0] - 1] == 1:
            return True
        return False

    #sprawdzanie listy wierzchołków ile mają połączeń z innymi wierzchołkami w macierzy sąsiedztwa A
    for v in vertexList:
        if A[vertex-1][v-1] == 1:
            #kopiujemy listę badanych wierzchołków i podajemy funkcji rekurencyjnej
            copyVList = copy.deepcopy(vertexList)
            copyVList.remove(v)

            #funkcja rekurencyjna
            check = IsHamFromVer(v, copyVList, A, checkList)

            ''' jesli z wierzchołka v do sprawdzanego wierzchołka vertex prowadzi tylko jedno połączenie
                to flag zmienia wartość na True i pętla zostaje przerwana;
                funkcja zwraca flag '''
            if check == True:
                flag = True
                break

    ''' jeśli vertex nie ma wspólnego węzła z v to flag pozostaje bez zmian = False
        rozpatrywany vertex zostaje usunięty '''
    if flag == False:
        checkList.remove(vertex)
    return flag

''' funkcja sprawdza czy graf jest hamiltonowski '''
''' pobiera listę wierzchołków i macierz sąsiedztwa '''
def IsHamiltonian(vertexList, A):

    #lista w której zbierane są kolejne wierzchołki cyklu
    checkList = []

    for elem in vertexList:
        copyVList = copy.deepcopy(vertexList)
        copyVList.remove(elem)

        check = IsHamFromVer(elem, copyVList, A, checkList)
        if check == False:
            checkList.clear()
        else:
            return True
    #jeśli nie odnaleziono cyklu to funkcja zwraca False
    if len(checkList) == 0:
        return False



getter = IsHamiltonian(vHAM, HAM)
print(getter)