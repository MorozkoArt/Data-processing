from common.constants import ANOMALIES_SHEET_NAME

class Column:
    def __init__(self, data, beta):
        self.data = data
        self._beta = beta
    def paramCount(self):
        if "self._dataLength" not in locals():
            self._dataLength = len(self.data)
        return self._dataLength
    def paramAvg(self):
        if "self._dataAvg" not in locals():
            self._dataAvg = sum(self.data) / self.paramCount()
        return self._dataAvg
    def paramDeviation(self):
        if "self._dataDeviation" not in locals():
            sqrOffseted = map(lambda x: pow(x - self.paramAvg(), 2), self.data)
            self._dataDeviation = pow(sum(sqrOffseted) / (self.paramCount() - 1), 0.5)
        return self._dataDeviation
    def paramBeta(self):
        return self._beta
    def dataCounter(self):
        return list(range(1, self.paramCount() + 1))
    def dataSorted(self):
        raise NotImplementedError()
    def dataUi(self):
        return list(map(lambda x: abs((x - self.paramAvg()) / self.paramDeviation()), self.dataSorted()))
    def dataWithoutAnomalies(self):
        return list(filter(lambda x: abs((x - self.paramAvg()) / self.paramDeviation()) <= self._beta, self.data))
    