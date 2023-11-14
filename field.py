import numpy as np
from enum import Enum
from PySide6.QtGui import QColor, QTransform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsRectItem, QApplication, QGraphicsScene


class Mode(Enum):
    DRAWING = 1
    ERASING = 2
    PLAYING = 3


class StateHolder:

    def __init__(self, width=80, height=80) -> None:
        self.mode = Mode.DRAWING
        self.prev_mode = None
        self.color = QColor(0, 0, 0)
        self.field = np.zeros(shape=(width, height, 3)) + 255

    def switch_mode(self, mode):
        if self.mode != mode:
            self.prev_mode = self.mode
            self.mode = mode

    def restore_mode(self):
        if self.mode == Mode.PLAYING:
            self.mode, self.prev_mode = self.prev_mode, self.mode

    def set_color(self, color):
        self.color = color


class Field(QGraphicsScene):

    def mouseMoveEvent(self, event) -> None:
        button = event.buttons()
        obj = self.itemAt(event.scenePos(), QTransform())
        if obj is not None and button == Qt.LeftButton:
            obj.mouseDrawEvent(event)
        return super().mouseMoveEvent(event)


class Cell(QGraphicsRectItem):

    def __init__(self, x, y, w, h, state_holder):
        super().__init__(0, 0, w, h)
        self.setPos(x * w, y * h)
        self.state_holder = state_holder
        self.coord = (x, y)
        color = self.state_holder.field[x][y].tolist()
        self.setBrush(QColor(*color))
        self.setAcceptHoverEvents(True)

    def mouseDrawEvent(self, event) -> None:
        color = QColor()
        if self.state_holder.mode == Mode.DRAWING:
            color = self.state_holder.color
        elif self.state_holder.mode == Mode.ERASING:
            color = QColor(255, 255, 255)
        x, y = self.coord
        self.state_holder.field[x][y] = np.array(color.toTuple())[:-1]
        self.setBrush(color)
        return super().mousePressEvent(event)

    def hoverEnterEvent(self, event) -> None:
        if self.state_holder.mode == Mode.DRAWING:
            QApplication.setOverrideCursor(Qt.PointingHandCursor)
        elif self.state_holder.mode == Mode.ERASING:
            QApplication.setOverrideCursor(Qt.CrossCursor)
        return super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event) -> None:
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        return super().hoverLeaveEvent(event)
