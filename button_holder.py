from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Our title!")
        button = QPushButton("Press me!")

        # Set button as central widget
        self.setCentralWidget(button)
