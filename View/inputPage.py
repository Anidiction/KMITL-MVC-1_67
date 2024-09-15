from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from Controller.inputValidator import validateInput
from Model.checkCow import IsCow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cow Milking App")
        self.setGeometry(100, 100, 600, 500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.idInputLabel = QLabel("Enter Cow ID:")
        self.layout.addWidget(self.idInputLabel)

        self.idInput = QLineEdit()
        self.idInput.setPlaceholderText("Enter 8-digit Cow ID")
        self.layout.addWidget(self.idInput)

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.submitClicked)
        self.layout.addWidget(self.submitButton)

    def submitClicked(self):
        cowId = self.idInput.text()
        if validateInput(cowId):
            try:
                result = IsCow(cowId)
                if result:
                    self.parent().cow_page.setCowId(cowId)
                    self.parent().switchView(True)
                else:
                    self.parent().switchView(False)
            except ValueError as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.critical(self, "Error", "Invalid Cow ID")