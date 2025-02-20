from common.constants import ANOMALIES_BLOCKS_OFFSETS, ANOMALIES_DATA_HEADINGS, ANOMALIES_PARAMS_HEADINGS

class ExcelLogger:
    def __init__(self, column, sheet):
        self.column = column
        self.sheet = sheet
    def logColumn(self):
        self.logParams()
        self.logData()
    def logParams(self):
        offset = ANOMALIES_BLOCKS_OFFSETS[type(self.column).__name__]["params"]
        for index, heading in enumerate(ANOMALIES_PARAMS_HEADINGS):
            self.sheet.cell(row=1+offset["row"],column=1+offset["col"] + index, value=heading)
    def logData(self):
        offset = ANOMALIES_BLOCKS_OFFSETS[type(self.column).__name__]["data"]
        for index, heading in enumerate(ANOMALIES_DATA_HEADINGS):
            self.sheet.cell(row=1+offset["row"],column=1+offset["col"] + index, value=heading)