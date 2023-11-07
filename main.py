import sys
from PySide6.QtCore import QSize, QTime, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow


class LifeOdyssey(QMainWindow):
    def __init__(self):
        super(LifeOdyssey, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(800, 800))

        self.iteration_number = 0
        self.curr_time = QTime(00, 00, 00)
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_iteration)
        self.is_playing = False

        stopButton = self.ui.stopButton
        stopButton.setCheckable(True)
        stopButton.clicked.connect(self.stop_button)

        playButton = self.ui.playButton
        playButton.setCheckable(True)
        playButton.clicked.connect(self.play_button)

        jumpForwardButton = self.ui.jumpForwardButton
        jumpForwardButton.setCheckable(True)
        jumpForwardButton.clicked.connect(self.jump_forward_button)

        jumpBackwardButton = self.ui.jumpBackwardButton
        jumpBackwardButton.setCheckable(True)
        jumpBackwardButton.clicked.connect(self.jump_backward_button)

        paletteButton = self.ui.paletteButton
        paletteButton.setCheckable(True)
        paletteButton.clicked.connect(self.palette_button)

        drawButton = self.ui.drawButton
        drawButton.setCheckable(True)
        drawButton.clicked.connect(self.draw_button)

        eraseButton = self.ui.eraseButton
        eraseButton.setCheckable(True)
        eraseButton.clicked.connect(self.erase_button)

    def stop_button(self):
        self.iteration_number = 0
        self.update_frame()

    def play_button(self):
        if self.is_playing:
            self.is_playing = False
            self.timer.stop()
            self.ui.playButton.setIcon(QIcon(u":/icons/icons/play_arrow.svg"))
            return
        self.ui.playButton.setIcon(QIcon(u":/icons/icons/pause.svg"))
        self.is_playing = True
        self.timer.start(250)

    def jump_forward_button(self):
        self.iteration_number += 5
        if self.iteration_number > 99:
            self.iteration_number = 99
        self.update_frame()

    def jump_backward_button(self):
        self.iteration_number -= 5
        if self.iteration_number < 0:
            self.iteration_number = 0
        self.update_frame()

    def palette_button(self):
        print("PALETTE")

    def draw_button(self):
        print("DRAW")

    def erase_button(self):
        print("ERASE")

    def update_frame(self):
        self.ui.frameSpinBox.setValue(self.iteration_number)

    def next_iteration(self):
        self.curr_time = self.curr_time.addSecs(0.25)
        self.iteration_number += 1
        if self.iteration_number > 99:
            self.iteration_number = 0
        self.update_frame()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LifeOdyssey()
    window.show()

    sys.exit(app.exec())
