#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections

def listaSkladowych(A):
    N = len(A)
    vers = [i for i in range(N)]
    spojne = []

    for v in vers:
        #    z wierzchołków 0..index(v)-1 już szukano sąsiadów
        #    z wierzchołków index(v)..last jeszcze nie szukano sąsiadów
        #    do wierzchołka index(v) nie da się dotrzeć z żadnego z wierzchołków 0..index(v)-1
        #    (czyli spójnych składowych jest tyle, ile iteracji)
        sp = [v]
        spojne.append(sp)

        # tworzymy kolejkę FIFO wierzchołków w sp, które trzeba przeszukać
        in_sp = collections.deque([v])

        while len(in_sp) != 0:
            ver = in_sp.popleft()

            for i in range(N):  # szukamy sąsiadów elementu
                if A[ver][i] == 1  and  i not in sp:
                    sp.append(i)  # można do niego dotrzeć

                    # indeks większy niż v oznacza, że i nie był jeszcze przeszukiwany w głównej pętli
                    if v < i:
                       in_sp.append(i)  # być może można z niego dojść dalej
                       vers.remove(i)   # dla zachowania niezmiennika pętli należy go usunąć
    return spojne



def najwiekszaSpojna(A):
    '''znajdź największą spójną składową'''
    # najdosłowniej z listy spójnych składowych wybiera tą o największej liczbie elementów
    spojne = listaSkladowych(A)

    max_l = 0
    max_s = None
    for s in spojne:
        if len(s) > max_l:
            max_l = len(s)
            max_s = s
    max_s.sort()

    # zwraca długość oraz zbiór wierzchołków
    return (max_l, max_s)

if __name__=='__main__':
    # składnia:
    #    python ./spojne.py '0 1 1; 1 0 1; 1 1 0'
    import sys

    mac = [[0,1,0], [1,0,0], [0,0,0]] \
            if len(sys.argv) < 2 else [[int(j) for j in i.split(' ')] for i in sys.argv[1].split('; ')]

    print mac
    print najwiekszaSpojna(mac)
