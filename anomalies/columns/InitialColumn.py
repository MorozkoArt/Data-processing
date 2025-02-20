from anomalies.columns.Column import Column

class InitialColumn(Column):
    def __init__(self, raw, beta):
        super().__init__(raw, beta)
    def dataSorted(self):
        if not self._dataSorted:
            self._dataSorted = self.data.sort()
        return self._dataSorted
    