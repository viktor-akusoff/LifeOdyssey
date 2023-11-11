import sys
from PySide6.QtCore import QTime, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QColorDialog,
    QGraphicsScene
)
from field import Cell, StateHolder, Mode
from ui_main import Ui_MainWindow


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
        self.timer.timeout.connect(self.next_iteration)
        self.is_playing = False
        self.draw_color = None

        self.init_field(80, 80, 10)

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

    def init_field(self, cols, rows, cell_size):
        scene = QGraphicsScene()
        width = cols * cell_size
        height = rows * cell_size
        for i in range(0, width, cell_size):
            for j in range(0, height, cell_size):
                rect = Cell(i, j, cell_size, cell_size, self.state_holder)
                scene.addItem(rect)
        scene.mousePressEvent
        self.ui.fieldGraphicsView.setScene(scene)
        self.ui.fieldGraphicsView.show()

    def stop_button(self):
        self.stop_playing()
        self.ui.frameSpinBox.setValue(0)
        self.restore_mode()
        self.update_mode_indicator()

    def set_play_mode(self):
        if self.state_holder.mode != Mode.PLAYING:
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
        color = QColorDialog.getColor()
        self.state_holder.set_color(color)

    def draw_button(self):
        self.stop_button()
        self.switch_mode(Mode.DRAWING)
        self.update_mode_indicator()

    def erase_button(self):
        self.stop_button()
        self.switch_mode(Mode.ERASING)
        self.update_mode_indicator()

    def update_value(self):
        if self.state_holder.mode != Mode.PLAYING:
            self.switch_mode(Mode.PLAYING)
        self.iteration_number = self.ui.frameSpinBox.value()

    def next_iteration(self):
        self.curr_time = self.curr_time.addSecs(1)
        old_val = self.move_spinbox(1)
        if old_val == 99:
            self.ui.frameSpinBox.setValue(0)

    def update_mode_indicator(self):
        mode = self.state_holder.mode
        if mode == Mode.DRAWING:
            self.ui.modeLabel.setText("Режим: рисование")
        elif mode == Mode.ERASING:
            self.ui.modeLabel.setText("Режим: стирание")
        elif mode == Mode.PLAYING:
            self.ui.modeLabel.setText("Режим: проигрывание")

    def switch_mode(self, mode):
        self.state_holder.switch_mode(mode)
        self.update_mode_indicator()

    def restore_mode(self):
        self.state_holder.restore_mode()
        self.update_mode_indicator()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LifeOdyssey()
    window.show()

    sys.exit(app.exec())
