import numpy as np
from enum import Enum
from PySide6.QtGui import QColor, QTransform
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGraphicsRectItem,
    QApplication,
    QGraphicsScene,
    QProgressDialog
)
from numpy.lib.stride_tricks import as_strided


class Mode(Enum):
    DRAWING = 1
    ERASING = 2
    PLAYING = 3


rule_of_life_alive = np.zeros(8+1, np.uint8)
rule_of_life_alive[[2, 3]] = 1

rule_of_life_dead = np.zeros(8+1, np.uint8)
rule_of_life_dead[3] = 1


def rgb_to_int(color):
    r, g, b = color
    return (r << 16) + (g << 8) + (b)


def int_to_rgb(number):
    inum = int(number)
    r = (inum & 0xff0000) >> 16
    g = (inum & 0x00ff00) >> 8
    b = (inum & 0x0000ff)
    return (r, g, b)


WHITE = rgb_to_int((255, 255, 255))
BLACK = rgb_to_int((0, 0, 0))


def neighborhoods(arr):
    assert all(_len > 2 for _len in arr.shape)

    nDims = len(arr.shape)
    newShape = [_len-2 for _len in arr.shape]
    newShape.extend([3] * nDims)

    newStrides = arr.strides + arr.strides
    return as_strided(arr, shape=newShape, strides=newStrides)


class StateHolder:

    def __init__(self, width=80, height=80, frames=100):
        self.frames = frames
        self.mode = Mode.DRAWING
        self.prev_mode = None
        self.color = BLACK
        self.step = 0
        self.initBoard(width, height)

    def initBoard(self, width=80, height=80):
        self.field = np.zeros(shape=(self.frames, width, height, 3)) + 255
        board_size = (self.frames-2, height, width)
        full_size = tuple(i+2 for i in board_size)
        self.full = np.zeros(full_size, dtype=np.uint8) + WHITE
        self.board = self.full[:, 1:-1, 1:-1]
        self.ndims = len(self.board.shape)

    def switchMode(self, mode):
        if self.mode != mode:
            self.prev_mode = self.mode
            self.mode = mode

    def restoreMode(self):
        if self.mode == Mode.PLAYING:
            self.mode, self.prev_mode = self.prev_mode, self.mode

    def setColor(self, color):
        self.color = color

    def calcNewState(self, frame, bg=WHITE):
        values = np.unique(self.board[frame-1])
        new_shape = (len(values), *np.shape(self.board[frame-1]))
        layers = np.zeros(shape=new_shape, dtype=np.uint32) + 0
        for i, value in enumerate(values):
            if value == bg:
                continue
            bw = np.copy(self.full[frame-1])
            bw[bw == WHITE] = WHITE + 1
            bw[bw != value] = WHITE + 1
            bw[bw == value] = 1
            bw[bw == WHITE + 1] = 0
            bw_neighborhoods = neighborhoods(bw)
            sum_over = tuple(-(i+1) for i in range(len(bw.shape)))
            color_sum = np.sum(bw_neighborhoods, sum_over) - bw[1:-1, 1:-1]
            layers[i] = color_sum
        k, m = layers.shape[1:]
        colors = np.zeros(shape=(k, m), dtype=np.uint32)
        for i in range(k):
            for j in range(m):
                colors[i][j] = values[np.argmax(layers[:, i, j])]
        bw = np.copy(self.full[frame-1])
        bw[bw != WHITE] = 1
        bw[bw == WHITE] = 0
        bw_neighborhoods = neighborhoods(bw)
        sum_over = tuple(-(i+1) for i in range(len(bw.shape)))
        neighbors_sum = np.sum(bw_neighborhoods, sum_over) - bw[1:-1, 1:-1]
        board = bw[1:-1, 1:-1]
        board[:] = np.where(
            board,
            rule_of_life_alive[neighbors_sum],
            rule_of_life_dead[neighbors_sum]
        )
        self.board[frame][board == 0] = WHITE
        self.board[frame][board != 0] = colors[board != 0]

    def calcSteps(self):
        progress = QProgressDialog('Просчитывание итераций', 'Стоп', 1, self.frames-1)
        progress.setWindowTitle('Life Odyssey')
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        for k in range(1, self.frames-1):
            progress.setValue(k)
            self.calcNewState(k, bg=WHITE)
            if progress.wasCanceled():
                break


class Field(QGraphicsScene):

    def mouseMoveEvent(self, event) -> None:
        button = event.buttons()
        obj = self.itemAt(event.scenePos(), QTransform())
        if obj is not None and button == Qt.LeftButton:
            obj.mouseDrawEvent(event)
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event) -> None:
        obj = self.itemAt(event.scenePos(), QTransform())
        obj.mouseDrawEvent(event)
        return super().mousePressEvent(event)


class Cell(QGraphicsRectItem):

    def __init__(self, x, y, w, h, state_holder, k=0):
        super().__init__(0, 0, w, h)
        self.setPos(x * w, y * h)
        self.state_holder = state_holder
        self.coord = (x, y)
        color = int_to_rgb(self.state_holder.board[k][y][x])
        self.setBrush(QColor(*color))
        self.setAcceptHoverEvents(True)

    def mouseDrawEvent(self, event) -> None:
        color = WHITE
        if self.state_holder.mode == Mode.DRAWING:
            color = self.state_holder.color
        elif self.state_holder.mode == Mode.ERASING:
            color = WHITE
        x, y = self.coord
        self.state_holder.board[0][y][x] = color
        qcolor = QColor(*int_to_rgb(color))
        self.setBrush(qcolor)
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
