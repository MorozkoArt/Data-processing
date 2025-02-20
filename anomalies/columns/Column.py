from common.constants import ANOMALIES_SHEET_NAME

class Column:
    def __init__(self, data, beta):
        self.sorted = data
        self.beta = beta
    def putExcel(self, workbook):
        raise NotImplementedError()