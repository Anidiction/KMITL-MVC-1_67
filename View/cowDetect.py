from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)

from Model.cowHandle import canMilkCow
from Model.updateTeats import update_teats
from Model.milkProduction import calculate_milk

class CowDetectView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cow Detected")
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.infoLabel = QLabel("A cow has been detected!")
        layout.addWidget(self.infoLabel)

        self.calBtn = QPushButton("Calculate Milk")
        self.calBtn.clicked.connect(self.calBtnClicked)
        layout.addWidget(self.calBtn)

        self.resultLabel = QLabel("")
        layout.addWidget(self.resultLabel)

        self.cowId = None

    def setCowId(self, cowId):
        self.cowId = cowId

    def calBtnClicked(self):
        try:
            result = canMilkCow(self.cowId)
            if result:
                update_teats(self.cowId)
                milk_amount = calculate_milk(self.cowId)
                QMessageBox.information(
                    self,
                    "Success",
                    f"The cow has produced {milk_amount} liters of milk.",
                )
            else:
                update_teats(self.cowId)
                QMessageBox.warning(self, "Error", "Cow cannot be milked.")
        except ValueError as e:
            self.resultLabel.setText(str(e))
            self.resultLabel.setStyleSheet("color: red")

        self.parent().setCurrentWidget(self.parent().input_page)