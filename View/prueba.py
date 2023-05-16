from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTableWidget, QTableWidgetItem

class MyTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(3)
        self.setRowCount(4)
        self.setHorizontalHeaderLabels(['Name', 'Age', 'Gender'])
        self.populate_table()

    def populate_table(self):
        data = [
            ['Alice', '25', 'Female'],
            ['Bob', '32', 'Male'],
            ['Charlie', '47', 'Male'],
            ['Diana', '19', 'Female']
        ]
        for row, values in enumerate(data):
            for col, value in enumerate(values):
                item = QTableWidgetItem(value)
                self.setItem(row, col, item)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana Principal")
        self.setGeometry(0, 0, 600, 400)

        # Agregar un widget de MyWidget a la ventana principal
        self.mywidget = MyTableWidget()
        self.setCentralWidget(self.mywidget)

if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()