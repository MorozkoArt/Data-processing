from anomalies.AnomaliesFilter import AnomaliesFilter
from common.constants import SUBFOLDERS
from common.outputFilepath import outputFilePath
from converters.XLSXConverter import XLSXConverter
from parsing.DataParser import DataParser
from openpyxl import Workbook

def createExcel(param, root):
    workbook = Workbook()
    dataParser = DataParser(root, SUBFOLDERS, param, workbook)
    dataParser.logOutput()
    bigData = dataParser.getBigData()

    anomaliesFilter = AnomaliesFilter(bigData, workbook)
    anomaliesFilter.logOutput()

    workbook.save(outputFilePath(root, param))

def main():
    root = input("root: ") # move to lanch param
    while True:
        param = input("param: ") # move to launch param
        converter = XLSXConverter(root, SUBFOLDERS)
        converter.AD5TtoXLSX()
        createExcel(param, root)

if __name__ == "__main__":
    main()

