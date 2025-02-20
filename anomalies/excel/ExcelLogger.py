from common.constants import ANOMALIES_BLOCKS_OFFSETS, ANOMALIES_DATA_HEADINGS, ANOMALIES_DATA_VALUES, ANOMALIES_PARAMS_HEADINGS, ANOMALIES_PARAMS_VALUES

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
            self.sheet.cell(row=1+offset["row"],column=1+index+offset["col"], value=heading)
        offset["row"] += 1
        for index, function in enumerate(ANOMALIES_PARAMS_VALUES):
            value = getattr(self.column, function)()
            self.sheet.cell(row=1+offset["row"],column=1+index+offset["col"], value=value)
    def logData(self):
        offset = ANOMALIES_BLOCKS_OFFSETS[type(self.column).__name__]["data"]
        for index, heading in enumerate(ANOMALIES_DATA_HEADINGS[type(self.column).__name__]):
            self.sheet.cell(row=1+offset["row"],column=1+index+offset["col"], value=heading)
        offset["row"] += 1
        print(offset)
        for functionIndex, function in enumerate(ANOMALIES_DATA_VALUES[type(self.column).__name__]):
            list = getattr(self.column, function)()
            for valueIndex, value in enumerate(list):
                self.sheet.cell(row=1+valueIndex+offset["row"],column=1+functionIndex+offset["col"], value=value)