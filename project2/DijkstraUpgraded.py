edgeWeights = {'e1': 1, 'e2': 2, 'e3': 3}

print(edgeWeights)


def Neighbours(ver1, ver2):
    return 1

def Weight(ver1, ver2):
    return 2

def DijkstraUpgraded(StartVertexes, Tab):
    for v in StartVertexes:
        for w in Tab.v:
            if Neighbours(v,w) and (Tab[v].w + Weight(v,w)) < Tab[w].w :
                Tab[w].w = Tab[v].w + Weight(v,w)
                Tab[w].s = v
    return Tab

def DijkstraAllUpgraded():
    matrix = []
    for vex in GetVertexList():
        matrix[ver][ver] = (0,0)
        d = DijkstraUpgraded(matrix[ver][ver+1:], [(ver,100, 0) for v in range(firstVer, ver-1)])
        matrix[ver][:ver] = d
        matrix[ver+1:][ver] = d