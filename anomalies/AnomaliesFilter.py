from anomalies.columns.IterationalColumn import IterationalColumn
from anomalies.columns.InitialColumn import InitialColumn
from anomalies.excel.ExcelLogger import ExcelLogger
from common.constants import ANOMALIES_BETA, ANOMALIES_DATA_HEADINGS, ANOMALIES_DATA_VALUES, ANOMALIES_PARAMS_HEADINGS, ANOMALIES_PARAMS_VALUES, ANOMALIES_SHEET_NAME


class AnomaliesFilter:
    def __init__(self, data, workbook):
        self.data = data
        self.sheet = workbook.create_sheet(ANOMALIES_SHEET_NAME)
        self.offset = {
            "row": 0,
            "col": 0
        }
    def logOutput(self):
        initialColumn = InitialColumn(self.data, ANOMALIES_BETA)
        self.logColumn(initialColumn)
        column = IterationalColumn(self.data, ANOMALIES_BETA)
        while not self.processEnd(column):
            self.logColumn(column)
            column = IterationalColumn(self.data, ANOMALIES_BETA)
        self.logColumn(column)
    def logColumn(self, column):
        initialColumnLogger = ExcelLogger(column, self.sheet, self.offset)
        initialColumnLogger.logColumn()
        self.data = column.dataWithoutAnomalies()
        self.offset["col"] += self.columnOffset(column) + 1
    def processEnd(self, column):
        return len(self.data) == len(column.dataWithoutAnomalies())
    def columnOffset(self, column):
        columnType = type(column).__name__
        return max(
            len(ANOMALIES_PARAMS_HEADINGS),
            len(ANOMALIES_PARAMS_VALUES),
            len(ANOMALIES_DATA_HEADINGS[columnType]),
            len(ANOMALIES_DATA_VALUES[columnType])
        )