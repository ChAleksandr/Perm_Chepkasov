from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5 import uic
from random import randint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle_create.ui', self)
        self.flag = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBackgroundMode(1)
            self.draw_flag(qp)
            qp.end()
            self.flag = False

    def paint(self):
        self.flag = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(1, 150)
        qp.drawEllipse(200 - r // 2, 200 - r // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
