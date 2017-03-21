#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Rysowanie grafów
Przykładowy input: [[0, 2, 0, 0, 3], [-2, 0, 7, 0, 0], [0, -7, 0, -6, -8], [0, 0, -6, 0, 5], [-3, 0, 8, -5, 0]]
Zamiast 1 - wagi.
"""

import sys, random, math
from PyQt4 import QtGui, QtCore

# Klasa punkt #
class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class Graph(QtGui.QWidget):

    def __init__(self, showWeights=True):
        super(Graph, self).__init__()
	self.pointList = []
	self.graphList = []
        self.initUI()
        self.showWeights = showWeights

    def initUI(self):
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Digraph graphic')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


# Funkcja przetwarzająca listę sąsiedztwa na listę współrzędnych punktów #
    def findList(self, li):
        self.graphList = li
        xm=(480-30)/2
        ym=(480-30)/2
        for i in range(len(self.graphList)):
            dpni = 2*(i-1) * math.pi / len(self.graphList)
            x = xm + 0.9 * xm * math.sin(dpni) + 15
            y = ym + 0.9 * ym * math.cos(dpni) + 15
            self.pointList.append(Point(x, y))




    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)

# Rysowanie linii #
        for i in range(len(self.graphList)):
            for j in range(len(self.graphList[i])):
                p = self.graphList[i][j]
		q = self.graphList[j][i]
		if p !=0:
                    self.drawLine(qp, self.pointList[i].x, self.pointList[i].y, self.pointList[j].x, self.pointList[j].y, p)


# Rysowanie punktów #
        for i in range(len(self.pointList)):
            self.drawPoint(qp, self.pointList[i].x, self.pointList[i].y, i)
        qp.end()



# Funkcja rysująca linie #
    def drawLine(self, qp, x1, y1, x2, y2, waga):
        if waga != float('inf'):
           pen = QtGui.QPen(QtCore.Qt.blue, 2, QtCore.Qt.SolidLine)

           qp.setPen(pen)
           qp.drawLine(x1, y1, x2, y2)
           xs = x1 + (x2-x1)/2
           ys = y1 + (y2-y1)/2
           cos = 0.866;
           sin = 0.500;

           xs = x1 + (xs-x1)/2
           ys = y1 + (ys-y1)/2

           arr1x = xs + (0.05*(x2-x1) * -cos + 0.05*(y2-y1) *  sin)
           arr1y = ys + (0.05*(x2-x1) * -sin + 0.05*(y2-y1) * -cos)

           arr2x = xs + (0.05*(x2-x1) * -cos + 0.05*(y2-y1) * -sin)
           arr2y = ys + (0.05*(x2-x1) *  sin + 0.05*(y2-y1) * -cos)
           qp.drawLine(xs, ys, arr1x, arr1y)
           qp.drawLine(xs, ys, arr2x, arr2y)


           qp.setPen(QtCore.Qt.red)
           qp.setFont(QtGui.QFont('Decorative', 10))
           if self.showWeights:
               qp.drawText ( xs-5, ys-5, str(waga))



# Funkcja rysująca punkty i ich numery #
    def drawPoint(self, qp, x, y, num):
        pen = QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine)
	qp.setPen(pen)
        size = self.size()
        qp.drawPoint(x, y)
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText ( x-5, y-5, str(num))


def wyswietl(li, showWeights=True):
    global app
    app = QtGui.QApplication.instance()
    if app is None:
        app = QtGui.QApplication([])
    ex = Graph(showWeights)
    ex.findList(li) # Tutaj wrzucacie listę sąsiedztwa #
    app.exit(app.exec_())



if __name__ == '__main__':
    wyswietl([[0, 2, 0, 0, -3], [2, 0, 7, 0, 0], [0, 0, 0, 6, -8], [0, 0, 0, 0, 5], [4, 0, 8, 5, 0]])