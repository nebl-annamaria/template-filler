import sys

from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QLabel,
    QMessageBox,
    QFormLayout,
    QFileDialog,
    QLineEdit,
    QVBoxLayout,
    QComboBox,
)


class ColumnSelectionDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.controller = main_window.controller
        self.columns = self.controller.columns
        self.variables = self.controller.variables
        self.column_dict = {}
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Column Selection")
        self.setUpWindow()

    def setUpWindow(self):
        v_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        for i in self.variables:
            self.column_dict[i] = None
            combo = QComboBox()
            combo.setObjectName(i)
            combo.addItems(self.columns)
            combo.currentIndexChanged.connect(self.onSelectionChange)
            self.column_dict[i] = self.columns[combo.currentIndex()]
            form_layout.addRow(i, combo)

        v_layout.addLayout(form_layout)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.onOkPress)
        v_layout.addWidget(ok_button)

    def onSelectionChange(self, i):
        self.column_dict[self.sender().objectName()] = self.columns[i]

    def onOkPress(self):
        dict = self.column_dict
        self.controller.set_column_dict(dict)
        self.main_window.changeLayout(
            self.main_window.stacked_layout.currentIndex() + 1
        )
        self.close()
