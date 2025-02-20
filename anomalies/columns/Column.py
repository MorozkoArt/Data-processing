from common.constants import ANOMALIES_SHEET_NAME

class Column:
    def __init__(self, data, beta):
        self.data = data
        self.beta = beta
    def dataLength(self):
        if not self._dataLength:
            self._dataLength = len(self.data)
        return self._dataLength
    def dataAvg(self):
        if not self._dataAvg:
            self._dataAvg = sum(self.data) / self.dataLength()
        return self._dataAvg
    def dataDeviation(self):
        if not self._dataDeviation:
            sqrOffseted = map(lambda x: pow(x - self.dataAvg(), 2), self.data)
            self._dataDeviation = pow(sum(sqrOffseted) / (self.dataLength() - 1), 0.5)
        return self._dataDeviation
    def dataSorted(self):
        raise NotImplementedError()
    def dataUi(self):
        return map(lambda x: abs((x - self.dataAvg()) / self.dataDeviation()), self.dataSorted())
    