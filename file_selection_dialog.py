import sys
from controller import Controller

from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QLabel,
    QMessageBox,
    QFormLayout,
    QFileDialog,
    QLineEdit,
    QVBoxLayout,
)

from PyQt6.QtGui import QIntValidator


class FileSelectionDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.controller = main_window.controller
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("File Selection")
        self.setUpWindow()

    def setUpWindow(self):
        template_select_btn = QPushButton("Browse")
        template_select_btn.setObjectName("template")
        template_select_btn.clicked.connect(self.getFilePath)

        workbook_select_btn = QPushButton("Browse")
        workbook_select_btn.setObjectName("workbook")
        workbook_select_btn.clicked.connect(self.getFilePath)

        sheet_input = QLineEdit()
        onlyInt = QIntValidator()
        sheet_input.setValidator(onlyInt)
        sheet_input.textChanged.connect(self.getInput)

        v_layout = QVBoxLayout(self)

        form = QFormLayout()
        form.addRow("template:", template_select_btn)
        form.addRow("workbook:", workbook_select_btn)
        form.addRow("sheet:", sheet_input)

        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.onOkPress)

        v_layout.addLayout(form)
        v_layout.addWidget(ok_btn)

    # TODO: filter by file extensions, error checking
    def getFilePath(self):
        sender = self.sender().objectName()
        path = QFileDialog().getOpenFileUrl()[0].path()
        if sender == "template":
            self.controller.set_template(path)
        elif sender == "workbook":
            self.controller.set_workbook(path)

    # TODO: validation
    def getInput(self):
        text = self.sender().text()
        self.controller.set_sheet(int(text))

    # TODO: error checking
    def onOkPress(self):
        self.controller.init_template_filler()
        self.controller.set_columns()
        self.controller.set_variables()
        self.main_window.changeLayout(
            self.main_window.stacked_layout.currentIndex() + 1
        )
        self.close()
