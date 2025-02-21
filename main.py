from common.constants import SUBFOLDERS
from Create_Excel import Create_excel
from converters.XLSXConverter import XLSXConverter
from parsing.DataParser import DataParser

def main():
    root = input("root: ") # move to lanch param
    while True:
        param = input("param: ") # move to launch param
        converter = XLSXConverter(root, SUBFOLDERS)
        converter.AD5TtoXLSX()

        parser = DataParser(root, SUBFOLDERS, param)
        parsed = parser.parseParamData()
        bigData = parser.convertToBigData(parsed)

        Create_excel(parsed, bigData, param, root)

if __name__ == "__main__":
    main()

