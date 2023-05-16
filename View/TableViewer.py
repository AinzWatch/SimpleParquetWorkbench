import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

class TableViewer(QTableWidget):
    def __init__(self, parent=None):
        super().__init__()
        #
        self.TableSizeConfiguration()
        self.DataTableViewer()
        
        
    def TableSizeConfiguration(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Establecer el tamaño de la ventana
        self.resize(int(screen_width * .8), int(screen_height * .8))
        self.setWindowTitle("Datos de Tabla")
        
    def DataTableViewer(self):
        # Agregar encabezados de columna
        encabezados = ['Columna 1', 'Columna 2', 'Columna 3']
        self.setColumnCount(len(encabezados)) # set number of columns found in Table
        
        self.setHorizontalHeaderLabels(encabezados)

        # Agregar datos a la tabla
        datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
        self.setRowCount(len(datos))# set number of rows found in Table
        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                celda = QTableWidgetItem(str(dato))
                self.setItem(fila, columna, celda)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TableViewer()
    ventana.show()
    sys.exit(app.exec_())


