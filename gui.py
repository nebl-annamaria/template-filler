import sys

from pathlib import Path

from controller import Controller
from file_selection_dialog import FileSelectionDialog
from column_selection_dialog import ColumnSelectionDialog

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QMainWindow,
    QFileDialog,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
)

from PyQt6.QtGui import QIntValidator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.controller = Controller()
        self.template_filler_initialized = False
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Template Filler")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        main_label = QLabel("Push the button to fill a new template")
        select_file_button = QPushButton("1. Select files")
        select_file_button.clicked.connect(self.openFileSelectionDialog)

        second_label = QLabel("Push the button to select data columns")
        select_col_btn = QPushButton("2. Select columns")
        select_col_btn.clicked.connect(self.openColumnSelectionDialog)

        third_label = QLabel("Push the button to start creating documents")
        start_btn = QPushButton("3. Start")
        start_btn.clicked.connect(self.startDocumentGeneration)

        self.pg1 = QVBoxLayout()
        self.pg1.addWidget(main_label)
        self.pg1.addWidget(select_file_button)
        self.pg1_container = QWidget()
        self.pg1_container.setLayout(self.pg1)

        self.pg2 = QVBoxLayout()
        self.pg2.addWidget(second_label)
        self.pg2.addWidget(select_col_btn)
        self.pg2_container = QWidget()
        self.pg2_container.setLayout(self.pg2)

        self.pg3 = QVBoxLayout()
        self.pg3.addWidget(third_label)
        self.pg3.addWidget(start_btn)
        self.pg3_container = QWidget()
        self.pg3_container.setLayout(self.pg3)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.pg1_container)
        self.stacked_layout.addWidget(self.pg2_container)
        self.stacked_layout.addWidget(self.pg3_container)

        main_v_box = QVBoxLayout()
        main_v_box.addLayout(self.stacked_layout)

        self.setLayout(main_v_box)

    def changeLayout(self, index):
        self.stacked_layout.setCurrentIndex(index)

    def openFileSelectionDialog(self):
        self.file_selection_dialog = FileSelectionDialog(self)
        self.file_selection_dialog.show()

    def openColumnSelectionDialog(self):
        self.column_selection_dialog = ColumnSelectionDialog(self)
        self.column_selection_dialog.show()

    def startDocumentGeneration(self):
        self.controller.start_document_creation()
        self.changeLayout(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
