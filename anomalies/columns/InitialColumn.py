from Column import Column
from common.constants import ANOMALIES_SHEET_NAME

class InitialColumn(Column):
    def __init__(self, raw, beta):
        sorted = raw.sort()
        super().__init__(self, sorted, beta)
    def putExcel(self, workbook):
        raise NotImplementedError()