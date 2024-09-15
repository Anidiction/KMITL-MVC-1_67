from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys
from View.inputPage import MainWindow
from View.goatDetect import GoatDetectView
from View.cowDetect import CowDetectView

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()  

        # Initialize views
        self.input_page = MainWindow()
        self.goat_page = GoatDetectView()
        self.cow_page = CowDetectView()

        # Set the parent of the input page so it can switch views
        self.input_page.setParent(self)

        # Add widgets to the stack
        self.addWidget(self.input_page)
        self.addWidget(self.goat_page)
        self.addWidget(self.cow_page)

        self.setCurrentWidget(self.input_page)

    def switchView(self, result):
        if result:
            self.setCurrentWidget(self.cow_page)
        else:
            self.setCurrentWidget(self.goat_page)

def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()