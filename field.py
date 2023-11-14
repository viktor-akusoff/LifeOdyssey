import numpy as np
import operator
from enum import Enum
from PySide6.QtGui import QColor, QTransform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGraphicsRectItem,
    QApplication,
    QGraphicsScene,
    QProgressDialog
)


class Mode(Enum):
    DRAWING = 1
    ERASING = 2
    PLAYING = 3


class StateHolder:

    def __init__(self, width=80, height=80) -> None:
        self.mode = Mode.DRAWING
        self.prev_mode = None
        self.color = QColor(0, 0, 0)
        self.step = 0
        self.field = np.zeros(shape=(100, width, height, 3)) + 255

    def switchMode(self, mode):
        if self.mode != mode:
            self.prev_mode = self.mode
            self.mode = mode

    def restoreMode(self):
        if self.mode == Mode.PLAYING:
            self.mode, self.prev_mode = self.prev_mode, self.mode

    def setColor(self, color):
        self.color = color

    @staticmethod
    def count_living_neighbors(field, x, y):
        h = len(field) - 1
        w = len(field[0]) - 1
        central_cell = 0 if np.sum(field[x][y]) == 765 else 1
        min_x = max(x-1, 0)
        min_y = max(y-1, 0)
        max_x = min(x+1, w)
        max_y = min(y+1, h)
        square = np.sum(field[min_x:max_x+1, min_y:max_y+1], axis=2)
        return np.count_nonzero(square - 765) - central_cell

    def calc_cell(self, k, x, y, h, w):
        field = self.field[k]
        is_alive = False if np.sum(field[x][y]) == 765 else True
        min_x = max(x-1, 0)
        min_y = max(y-1, 0)
        max_x = min(x+1, w)
        max_y = min(y+1, h)
        slc = field[min_x:max_x+1, min_y:max_y+1]
        square = np.sum(field[min_x:max_x+1, min_y:max_y+1], axis=2)
        neighbors = np.count_nonzero(square - 765) - int(is_alive)
        colors_dict = {}
        for iy, ix in np.ndindex(square.shape):
            color_key = str(slc[iy, ix])
            if color_key == '[255. 255. 255.]':
                continue
            if color_key not in colors_dict.keys():
                colors_dict[color_key] = 0
            colors_dict[color_key] += 1
        if (
            (is_alive and neighbors in (2, 3)) or
            (not is_alive and neighbors == 3)
        ):
            most_frequent_color_k = max(
                colors_dict.items(),
                key=operator.itemgetter(1)
            )[0]
            most_frequent_color_s = most_frequent_color_k[1:-1].split('.')[:-1]
            most_frequent_color = [
                int(element) for element in most_frequent_color_s
            ]
            return QColor(*most_frequent_color)
        return QColor(255, 255, 255)

    def calcSteps(self):
        progress = QProgressDialog('Просчитывание итераций', 'Стоп', 1, 100)
        progress.setWindowTitle('Life Odyssey')
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        w = len(self.field[0]) - 1
        h = len(self.field[0][0]) - 1
        for k in range(1, 100):
            progress.setValue(k)
            for i in range(0, w-1):
                for j in range(0, h-1):
                    self.field[k][i][j] = self.calc_cell(
                        k-1,
                        i,
                        j,
                        h,
                        w,
                    ).toTuple()[:-1]  # type: ignore
            if progress.wasCanceled():
                break


class Field(QGraphicsScene):

    def mouseMoveEvent(self, event) -> None:
        button = event.buttons()
        obj = self.itemAt(event.scenePos(), QTransform())
        if obj is not None and button == Qt.LeftButton:
            obj.mouseDrawEvent(event)
        return super().mouseMoveEvent(event)


class Cell(QGraphicsRectItem):

    def __init__(self, x, y, w, h, state_holder, k=0):
        super().__init__(0, 0, w, h)
        self.setPos(x * w, y * h)
        self.state_holder = state_holder
        self.coord = (x, y)
        color = self.state_holder.field[k][x][y].tolist()
        self.setBrush(QColor(*color))
        self.setAcceptHoverEvents(True)

    def mouseDrawEvent(self, event) -> None:
        color = QColor()
        if self.state_holder.mode == Mode.DRAWING:
            color = self.state_holder.color
        elif self.state_holder.mode == Mode.ERASING:
            color = QColor(255, 255, 255)
        x, y = self.coord
        self.state_holder.field[0][x][y] = np.array(color.toTuple())[:-1]
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
