import glob, os

from openpyxl import load_workbook
from docx import Document
from docxtpl import DocxTemplate
from docx2pdf import convert
import pandas as pd


class TemplateFiller:
    def __init__(self, template, workbook, sheet):
        self.__template_path = template
        self.__workbook_path = workbook
        self.__workbook_sheet = sheet
        self.__template = self.__open_template()
        self.variables = self.__list_variables()
        self.__df = self.__open_workbook()
        self.columns = self.__list_columns()
        self.__column_dict = None
        self.__render_dict = None

    def __open_template(self):
        template = DocxTemplate(self.__template_path)
        return template

    def __list_variables(self):
        template_variables = [
            var for var in self.__template.get_undeclared_template_variables()
        ]
        return template_variables

    def __open_workbook(self):
        df = pd.read_excel(self.__workbook_path, sheet_name=self.__workbook_sheet)
        return df

    def __list_columns(self):
        df = self.__df
        columns = [col for col in df.columns]
        for col in columns:
            if df[col].dtype == "datetime64[ns]":
                df[col] = df[col].dt.date
        return columns

    def set_column_dict(self, dict):
        self.__column_dict = dict

    def __build_render_dict(self):
        column_dict = self.__column_dict
        dict = {}

        for i in column_dict:
            dict[i] = None

        self.__render_dict = dict

    def create_documents(self):
        self.__build_render_dict()
        template = self.__template
        df = self.__df
        column_dict = self.__column_dict
        render_dict = self.__render_dict
        filename = "tempdoc.docx"
        for index, row in df.iterrows():
            for i in column_dict:
                render_dict[i] = row[column_dict[i]]
            template.render(render_dict)
            template.save(filename)
            os.chmod(filename, 0o777)
            convert(filename, f"{render_dict['name']}.pdf")
        os.remove(filename)
