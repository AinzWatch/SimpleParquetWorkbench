import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit

class QueryTextBoxViewer(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 400)

if __name__ == '__main__':
    app = QApplication([])
    widget = QueryTextBoxViewer()
    widget.show()
    app.exec_()