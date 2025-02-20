from anomalies.columns.IterationalColumn import IterationalColumn
from anomalies.columns.InitialColumn import InitialColumn
from anomalies.excel.ExcelLogger import ExcelLogger
from common.constants import ANOMALIES_BETA, ANOMALIES_SHEET_NAME


class AnomaliesFilter:
    def __init__(self, data, workbook):
        self.data = data
        self.sheet = workbook.create_sheet(ANOMALIES_SHEET_NAME)
    def logOutput(self):
        self.logColumn(InitialColumn(self.data, ANOMALIES_BETA))
        column = None
        while not self.processEnd(column):
            column = IterationalColumn(self.data, ANOMALIES_BETA)
            self.logColumn(column)
    def logColumn(self, column):
        initialColumnLogger = ExcelLogger(column, self.sheet)
        initialColumnLogger.logColumn()
        self.data = column.dataWithoutAnomalies()
    def processEnd(self, column):
        if column == None:
            return False
        return len(self.data) == len(column.dataWithoutAnomalies())