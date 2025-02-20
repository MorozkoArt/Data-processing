from Column import Column
from common.constants import ANOMALIES_SHEET_NAME

class InitialColumn(Column):
    def __init__(self, raw, beta):
        super().__init__(self, raw, beta)
    def dataSorted(self):
        if not self._dataSorted:
            self._dataSorted = self.data.sort()
        return self._dataSorted
    