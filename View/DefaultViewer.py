import sys
from PySide6.QtWidgets import QApplication, QMainWindow ,QWidget, QVBoxLayout, QLineEdit
from TableViewer import TableViewer
from QueryTextBoxViewer import QueryTextBoxViewer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.TableWidget = TableViewer()
        self.QueryTextBoxWidget = QueryTextBoxViewer()
        

        self.setCentralWidget(self.QueryTextBoxWidget)
        self.setCentralWidget(self.TableWidget)

        
if __name__ == '__main__':
    app = QApplication([])
    Main = MainWindow()
    Main.show()
    sys.exit(app.exec())