#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Drawing lines for graph
"""

import sys, random, math
from PyQt4 import QtGui, QtCore

# Klasa punkt #
class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class Graph(QtGui.QWidget):

    def __init__(self):
        super(Graph, self).__init__()
	    self.pointList = []
	    self.graphList = []
        self.initUI()

    def initUI(self):      
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Graph graphic')
        self.show()


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
                self.drawLine(qp, self.pointList[i].x, self.pointList[i].y, self.pointList[p].x, self.pointList[p].y)


# Rysowanie punktów #
        for i in range(len(self.pointList)):
            self.drawPoint(qp, self.pointList[i].x, self.pointList[i].y, i)
        qp.end()
        


# Funkcja rysująca linie #
    def drawLine(self, qp, x1, y1, x2, y2):
      
        pen = QtGui.QPen(QtCore.Qt.blue, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(x1, y1, x2, y2)
              

# Funkcja rysująca punkty i ich numery # 
    def drawPoint(self, qp, x, y, num):
        pen = QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine)
	qp.setPen(pen)
        size = self.size()
        qp.drawPoint(x, y)
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText ( x-5, y-5, str(num))           

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Graph()
    ex.findList([[1], [2], [3, 5, 1], [4], [5, 6, 1], [6], [0]]) # Tutaj wrzucacie listę sąsiedztwa #
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

