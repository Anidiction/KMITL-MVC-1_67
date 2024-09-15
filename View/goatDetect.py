from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class GoatDetectView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goat Detected")
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.infoLabel = QLabel("A goat has been detected!")
        layout.addWidget(self.infoLabel)

        self.instructionsLabel = QLabel("Click the button to send the goat to the mountain.")
        layout.addWidget(self.instructionsLabel)

        self.sendBtn = QPushButton("Send Goat")
        self.sendBtn.clicked.connect(self.sendBtnClicked)
        layout.addWidget(self.sendBtn)

    def sendBtnClicked(self):
        self.parent().setCurrentWidget(self.parent().input_page)