import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class My(QMainWindow):
    def __init__(self):
        super().__init__()

        self.draw_btn: QPushButton
        self.perform_draw = False

        with open("UI.ui") as f:
            uic.loadUi(f, self)
        self.draw_btn.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.perform_draw = True
        self.update()

    def paintEvent(self, _):
        if not self.perform_draw:
            return

        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor("#fc0"))

        radius = randint(10, int(min(self.height(), self.width()) / 2.5))
        center = QPointF(self.width() / 2, self.height() / 2)
        qp.drawEllipse(center, radius, radius)

        qp.end()
        self.perform_draw = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = My()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
