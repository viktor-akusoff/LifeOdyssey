from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsRectItem

class Cell(QGraphicsRectItem):

    def __init__(self, x, y, w, h):
        super().__init__(0, 0, w, h)
        self.setPos(x, y)
        self.coord = (x, y)
        self.setBrush(QColor(255, 255, 255))

    def mousePressEvent(self, event) -> None:
        self.setBrush(QColor(0, 0, 0))
        return super().mousePressEvent(event)