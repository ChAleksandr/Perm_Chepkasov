from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5 import uic
from random import randint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle_create.ui', self)
        self.btn.clicked.connect(self.paint)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.flag = False

    def paint(self):
        self.flag = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 255))
        qp.drawEllipse(200, 200, randint(10, 150), randint(10, 150))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
