from template_filler import TemplateFiller


class Controller:
    def __init__(self):
        self.__template = None
        self.__workbook = None
        self.__sheet = None
        self.__template_filler = None
        self.variables = None
        self.columns = None

    def set_template(self, template):
        self.__template = template

    def set_workbook(self, workbook):
        self.__workbook = workbook

    def set_sheet(self, sheet):
        self.__sheet = sheet - 1

    def init_template_filler(self):
        obj = TemplateFiller(self.__template, self.__workbook, self.__sheet)
        self.__template_filler = obj

    def set_variables(self):
        self.variables = self.__template_filler.variables

    def set_columns(self):
        self.columns = self.__template_filler.columns

    def set_column_dict(self, dict):
        self.__template_filler.set_column_dict(dict)

    def set_merger_state(self, state):
        self.__template_filler.set_merger_state(state)

    def start_document_creation(self):
        self.__template_filler.create_documents()
