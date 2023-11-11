from enum import Enum
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsRectItem, QApplication


class Mode(Enum):
    DRAWING = 1
    ERASING = 2
    PLAYING = 3


class StateHolder:

    def __init__(self) -> None:
        self.mode = Mode.DRAWING
        self.prev_mode = None
        self.color = QColor(0, 0, 0)

    def switch_mode(self, mode):
        if self.mode != mode:
            self.prev_mode = self.mode
            self.mode = mode

    def restore_mode(self):
        if self.mode == Mode.PLAYING:
            self.mode, self.prev_mode = self.prev_mode, self.mode

    def set_color(self, color):
        self.color = color


class Cell(QGraphicsRectItem):

    def __init__(self, x, y, w, h, state_holder):
        super().__init__(0, 0, w, h)
        self.setPos(x, y)
        self.state_holder = state_holder
        self.coord = (x, y)
        self.setBrush(QColor(255, 255, 255))
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event) -> None:
        if self.state_holder.mode == Mode.DRAWING:
            self.setBrush(self.state_holder.color)
        elif self.state_holder.mode == Mode.ERASING:
            self.setBrush(QColor(255, 255, 255))
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
