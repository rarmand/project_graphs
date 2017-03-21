#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import math
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
        self.layerList = []
        self.flowList = []
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Graph graphic')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


            # Funkcja przetwarzająca listę sąsiedztwa na listę współrzędnych punktów #

    def findList(self, li, lw, fm):
        self.graphList = li
        self.flowList = fm

        howMany = 600 / (len(lw) - 1)
        for i in range(len(lw)):
            self.layerList.append(20 + i * howMany)

        for i in range(len(self.layerList)):
            x = self.layerList[i]
            for j in range(1, lw[i] + 1):
                y = 40 + 400 / (lw[i] + 1) * j
                self.pointList.append(Point(x, y))

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)

        # Rysowanie warstw #
        self.drawLayers(qp)

        # Rysowanie linii #
        for i in xrange(len(self.graphList)):
            for j in xrange(len(self.graphList[i])):
                p = self.graphList[i][j]
                q =self.flowList[i][j]
                if p != 0:
                    self.drawLine(qp, self.pointList[i].x, self.pointList[i].y, self.pointList[j].x,
                                  self.pointList[j].y, p,q)


                    # Rysowanie punktów #
        for i in range(len(self.pointList)):
            self.drawPoint(qp, self.pointList[i].x, self.pointList[i].y, i)
        qp.end()

    # Funkcja rysująca warstwy #
    def drawLayers(self, qp):
        pen2 = QtGui.QPen(QtGui.QColor(191, 0, 191), 1, QtCore.Qt.CustomDashLine)
        pen2.setDashPattern([3, 5, 3, 5])
        qp.setPen(pen2)

        for i in range(len(self.layerList)):
            qp.drawLine(self.layerList[i], 40, self.layerList[i], 440)

            # Funkcja rysująca linie #

    def drawLine(self, qp, x1, y1, x2, y2, waga, flow):
        if waga != float('inf'):
            pen = QtGui.QPen(QtCore.Qt.blue, 2, QtCore.Qt.SolidLine)

            qp.setPen(pen)
            qp.drawLine(x1, y1, x2, y2)
            xs = x1 + (x2 - x1) / 2
            ys = y1 + (y2 - y1) / 2
            cos = 0.866;
            sin = 0.500;

            xs = x1 + (xs - x1) / 2
            ys = y1 + (ys - y1) / 2

            arr1x = xs + (0.05 * (x2 - x1) * -cos + 0.05 * (y2 - y1) * sin)
            arr1y = ys + (0.05 * (x2 - x1) * -sin + 0.05 * (y2 - y1) * -cos)

            arr2x = xs + (0.05 * (x2 - x1) * -cos + 0.05 * (y2 - y1) * -sin)
            arr2y = ys + (0.05 * (x2 - x1) * sin + 0.05 * (y2 - y1) * -cos)
            qp.drawLine(xs, ys, arr1x, arr1y)
            qp.drawLine(xs, ys, arr2x, arr2y)

            qp.setPen(QtCore.Qt.red)
            qp.setFont(QtGui.QFont('Decorative', 10))
            qp.drawText(xs - 5, ys - 5, str(waga))
            qp.setPen(QtCore.Qt.darkGreen)
            qp.drawText(xs - 15, ys - 15, str(flow))



            # Funkcja rysująca punkty i ich numery #

    def drawPoint(self, qp, x, y, num):
        pen = QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()
        qp.drawPoint(x, y)
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(x - 5, y - 5, str(num))


def wyswietl(li, lw, fm):
    global app
    app = QtGui.QApplication.instance()
    if app is None:
        app = QtGui.QApplication([])
    ex = Graph()
    ex.findList(li, lw, fm)  # Tutaj wrzucacie listę sąsiedztwa #
    app.exit(app.exec_())


if __name__ == '__main__':
    wyswietl([[0, 2, 0, 0, 3], [2, 0, 7, 0, 0], [0, 0, 0, 6, 8], [0, 0, 0, 0, 5], [4, 0, 8, 5, 0]],
             [1, 2, 2])  # Tutaj wrzucacie macierz sąsiedztwa oraz liczbę wierzchołków w warstwie#
