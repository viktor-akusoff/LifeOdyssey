import sys
import numpy as np
from pathlib import Path
from PySide6.QtCore import QTime, QTimer
from PySide6.QtGui import QIcon, QIntValidator
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QColorDialog,
    QFileDialog,
)
from field import Cell, StateHolder, Mode, Field
from ui_main import Ui_MainWindow
from ui_create import Ui_createDialog


class CreateDialog(QDialog):
    def __init__(self):
        super(CreateDialog, self).__init__()
        self.ui = Ui_createDialog()
        self.ui.setupUi(self)
        self.ui.lineWidth.setText('80')
        self.ui.lineHeight.setText('80')
        self.ui.lineHeight.setValidator(QIntValidator(0, 200))
        self.ui.lineWidth.setValidator(QIntValidator(0, 200))


class LifeOdyssey(QMainWindow):
    def __init__(self):
        super(LifeOdyssey, self).__init__()
        self.state_holder = StateHolder()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.iteration_number = 0
        self.curr_time = QTime(00, 00, 00)
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextIteration)
        self.is_playing = False
        self.draw_color = None

        self.initField()

        self.ui.paletteButton.setStyleSheet(
            'QPushButton {background-color: black;}'
        )

        stopButton = self.ui.stopButton
        stopButton.setCheckable(True)
        stopButton.clicked.connect(self.stopButton)

        playButton = self.ui.playButton
        playButton.setCheckable(True)
        playButton.clicked.connect(self.playButton)

        jumpForwardButton = self.ui.jumpForwardButton
        jumpForwardButton.setCheckable(True)
        jumpForwardButton.clicked.connect(self.jumpForwardButton)

        jumpBackwardButton = self.ui.jumpBackwardButton
        jumpBackwardButton.setCheckable(True)
        jumpBackwardButton.clicked.connect(self.jumpBackwardButton)

        paletteButton = self.ui.paletteButton
        paletteButton.setCheckable(True)
        paletteButton.clicked.connect(self.paletteButton)

        drawButton = self.ui.drawButton
        drawButton.setCheckable(True)
        drawButton.clicked.connect(self.drawButton)

        eraseButton = self.ui.eraseButton
        eraseButton.setCheckable(True)
        eraseButton.clicked.connect(self.eraseButton)

        frameSpinBox = self.ui.frameSpinBox
        frameSpinBox.valueChanged.connect(self.updateValue)

        saveFieldAction = self.ui.saveFieldAction
        saveFieldAction.triggered.connect(self.saveField)

        openFieldAction = self.ui.openFieldAction
        openFieldAction.triggered.connect(self.openField)

        newFieldAction = self.ui.newFieldAction
        newFieldAction.triggered.connect(self.newField)

        calcFieldAction = self.ui.calcFieldAction
        calcFieldAction.triggered.connect(self.calcField)

        cleanFieldAction = self.ui.cleanFieldAction
        cleanFieldAction.triggered.connect(self.cleanField)

    def initField(self, k=0):
        scene = Field()
        rows = len(self.state_holder.field[k])
        cols = len(self.state_holder.field[k][0])
        for i in range(0, rows-1):
            for j in range(0, cols-1):
                rect = Cell(i, j, 10, 10, self.state_holder, k)
                scene.addItem(rect)
        self.ui.fieldGraphicsView.setScene(scene)
        self.ui.fieldGraphicsView.show()

    def stopButton(self):
        self.stopPlaying()
        self.ui.frameSpinBox.setValue(0)
        self.restoreMode()
        self.updateModeIndicator()

    def setPlayMode(self):
        if self.state_holder.mode != Mode.PLAYING:
            self.switchMode(Mode.PLAYING)

    def playButton(self):
        self.switchMode(Mode.PLAYING)
        if self.is_playing:
            self.stopPlaying()
            return
        self.startPlaying()

    def startPlaying(self):
        self.is_playing = True
        self.timer.start(250)
        self.ui.playButton.setIcon(QIcon(u":/icons/icons/pause.svg"))

    def stopPlaying(self):
        self.is_playing = False
        self.timer.stop()
        self.ui.playButton.setIcon(QIcon(u":/icons/icons/play_arrow.svg"))

    def moveSpinbox(self, num):
        old_val = self.ui.frameSpinBox.value()
        self.ui.frameSpinBox.setValue(old_val + num)
        return old_val

    def jumpForwardButton(self):
        self.setPlayMode()
        old_val = self.moveSpinbox(5)
        if old_val > 94:
            self.ui.frameSpinBox.setValue(0)

    def jumpBackwardButton(self):
        self.setPlayMode()
        old_val = self.moveSpinbox(-5)
        if old_val < 5:
            self.ui.frameSpinBox.setValue(99)

    def paletteButton(self):
        color = QColorDialog.getColor()
        rgb_color = color.name()
        self.ui.paletteButton.setStyleSheet(
            f'QPushButton {{background-color: {rgb_color};}}'
        )
        self.state_holder.setColor(color)

    def drawButton(self):
        self.stopButton()
        self.switchMode(Mode.DRAWING)
        self.updateModeIndicator()

    def eraseButton(self):
        self.stopButton()
        self.switchMode(Mode.ERASING)
        self.updateModeIndicator()

    def updateValue(self):
        if self.state_holder.mode != Mode.PLAYING:
            self.switchMode(Mode.PLAYING)
        self.iteration_number = self.ui.frameSpinBox.value()
        self.initField(self.iteration_number)

    def nextIteration(self):
        self.curr_time = self.curr_time.addSecs(1)
        old_val = self.moveSpinbox(1)
        if old_val == 99:
            self.ui.frameSpinBox.setValue(0)

    def updateModeIndicator(self):
        mode = self.state_holder.mode
        if mode == Mode.DRAWING:
            self.ui.modeLabel.setText("Режим: рисование")
        elif mode == Mode.ERASING:
            self.ui.modeLabel.setText("Режим: стирание")
        elif mode == Mode.PLAYING:
            self.ui.modeLabel.setText("Режим: проигрывание")

    def switchMode(self, mode):
        self.state_holder.switchMode(mode)
        self.updateModeIndicator()

    def restoreMode(self):
        self.state_holder.restoreMode()
        self.updateModeIndicator()

    def saveField(self):
        address, _ = QFileDialog.getSaveFileName(
            None,  # type: ignore
            "Сохранить поле",
            str(Path.home()),
            "Бинарный файл NumPy (*.npy)"
        )
        data = self.state_holder.field[0]
        self.setWindowTitle(f'Life Odyssey - {address}')
        np.save(address, data)

    def openField(self):
        address, _ = QFileDialog.getOpenFileName(
            None,  # type: ignore
            "Открыть поле",
            str(Path.home()),
            "Бинарный файл NumPy (*.npy)"
        )
        data = np.load(address)
        h = len(data)
        w = len(data[0])
        self.state_holder.field = np.zeros(shape=(100, h, w, 3)) + 255
        self.state_holder.field[0] = data
        self.setWindowTitle(f'Life Odyssey - {address}')
        self.initField()

    def newField(self):
        dialog = CreateDialog()
        if dialog.exec():
            w = int(dialog.ui.lineWidth.text())
            h = int(dialog.ui.lineHeight.text())
            self.state_holder = StateHolder(w, h)
            self.setWindowTitle('Life Odyssey - Новое поле')
            self.initField()

    def calcField(self):
        self.state_holder.calcSteps()

    def cleanField(self):
        self.state_holder.field[0] = 255
        self.initField()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LifeOdyssey()
    window.show()

    sys.exit(app.exec())
