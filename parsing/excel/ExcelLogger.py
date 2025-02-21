class ExcelLogger:
    def __init__(self, parsed):
        self.parsed = parsed
    def logParsed(self):
        self.logHeadings()
        self.logData()
    def logHeadings(self):
        pass
    def logData(self):
        pass