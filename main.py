import sys
from enum import Enum
from PySide6.QtCore import QSize, QTime, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow


class Mode(Enum):
    DRAWING = 1
    ERASING = 2
    PLAYING = 3


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
        self.mode = Mode.DRAWING
        self.prev_mode = None

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

        frameSpinBox = self.ui.frameSpinBox
        frameSpinBox.valueChanged.connect(self.update_value)

    def stop_button(self):
        self.stop_playing()
        self.ui.frameSpinBox.setValue(0)
        self.restore_mode()
        self.update_mode_indicator()

    def set_play_mode(self):
        if self.mode != Mode.PLAYING:
            self.switch_mode(Mode.PLAYING)

    def play_button(self):
        self.switch_mode(Mode.PLAYING)
        if self.is_playing:
            self.stop_playing()
            return
        self.start_playing()

    def start_playing(self):
        self.is_playing = True
        self.timer.start(250)
        self.ui.playButton.setIcon(QIcon(u":/icons/icons/pause.svg"))

    def stop_playing(self):
        self.is_playing = False
        self.timer.stop()
        self.ui.playButton.setIcon(QIcon(u":/icons/icons/play_arrow.svg"))

    def move_spinbox(self, num):
        old_val = self.ui.frameSpinBox.value()
        self.ui.frameSpinBox.setValue(old_val + num)
        return old_val

    def jump_forward_button(self):
        self.set_play_mode()
        old_val = self.move_spinbox(5)
        if old_val > 94:
            self.ui.frameSpinBox.setValue(0)

    def jump_backward_button(self):
        self.set_play_mode()
        old_val = self.move_spinbox(-5)
        if old_val < 5:
            self.ui.frameSpinBox.setValue(99)

    def palette_button(self):
        print("PALETTE")

    def draw_button(self):
        self.stop_button()
        self.switch_mode(Mode.DRAWING)
        self.update_mode_indicator()

    def erase_button(self):
        self.stop_button()
        self.switch_mode(Mode.ERASING)
        self.update_mode_indicator()

    def update_value(self):
        if self.mode != Mode.PLAYING:
            self.switch_mode(Mode.PLAYING)
        self.iteration_number = self.ui.frameSpinBox.value()

    def next_iteration(self):
        self.curr_time = self.curr_time.addSecs(1)
        old_val = self.move_spinbox(1)
        if old_val == 99:
            self.ui.frameSpinBox.setValue(0)

    def update_mode_indicator(self):
        if self.mode == Mode.DRAWING:
            self.ui.modeLabel.setText("Режим: рисование")
        elif self.mode == Mode.ERASING:
            self.ui.modeLabel.setText("Режим: стирание")
        elif self.mode == Mode.PLAYING:
            self.ui.modeLabel.setText("Режим: проигрывание")

    def switch_mode(self, mode):
        if self.mode != mode:
            self.prev_mode = self.mode
            self.mode = mode
            self.update_mode_indicator()

    def restore_mode(self):
        if self.mode == Mode.PLAYING:
            self.mode, self.prev_mode = self.prev_mode, self.mode


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LifeOdyssey()
    window.show()

    sys.exit(app.exec())
