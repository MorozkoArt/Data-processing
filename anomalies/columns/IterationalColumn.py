from Column import Column
from common.constants import ANOMALIES_SHEET_NAME

class IterationalColumn(Column):
    def __init__(self, data, beta):
        super().__init__(self, data, beta)
    def dataSorted(self):
        return self.data