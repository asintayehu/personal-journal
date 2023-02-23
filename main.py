# VERSION 1: SETTING EVERYTHING UP IN A GLOBAL SCOPE
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Sets up the foundation for a window that people can use with kbm
app = QApplication(sys.argv)

# Creates a window
window = QMainWindow()

# Sets title of the window
window.setWindowTitle("Our first MainWindow App!")

# Creates a pushable button that can do a task, its a command button
button = QPushButton()

# Sets the text of the button to "Press me!"
button.setText("Press Me!")


# Puts the button in the middle of the screen
window.setCentralWidget(button)

window.show()
app.exec()

"""

# VERSION 2: SETTING UP A SEPERATE CLASS
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Our title!")
        button = QPushButton("Press me!")

        # Set button as central widget
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()
"""


# VERSION 3: SEPERATE FILES
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()

window.show()
app.exec()
