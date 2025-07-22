# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Library Catalog")
        self.setGeometry(100, 100, 800, 600)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LibraryApp()
    window.show()

    sys.exit(app.exec())