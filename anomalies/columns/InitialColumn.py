from anomalies.columns.Column import Column

class InitialColumn(Column):
    def __init__(self, raw, beta):
        super().__init__(raw, beta)
    def dataRaw(self):
        return self.data
    def dataSorted(self):
        if "self._dataSorted" not in locals():
            self._dataSorted = sorted(self.data)
        return self._dataSorted
    