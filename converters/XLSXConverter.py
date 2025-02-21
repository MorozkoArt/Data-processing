import os
from pathlib import Path
import shutil
import openpyxl
from common.subfolderPaths import subfolderPaths


class XLSXConverter:
    def __init__(self, root, subfolders):
        self.root = root
        self.subfolders = subfolders
    def AD5TtoXLSX(self):
        subPaths = subfolderPaths(self.root, self.subfolders)
        for subPath in subPaths:
            for file in os.listdir(subPath):
                path = os.path.join(subPath, file)
                if os.path.isfile(path):
                    name, ext = os.path.splitext(path)
                    if ext.lower() == ".ad5t":
                        txtFile = self.AD5TtoTXT(path)
                        self.TXTtoXLSX(txtFile)
    def TXTtoXLSX(self, txtPath):
        data = []
        name, ext = os.path.splitext(txtPath)
        xlsxPath = name + ".xlsx"
        with open(txtPath, 'r', encoding='utf-8') as txtFile:
                for line in txtFile:
                    row = line.strip().split("\t")
                    data.append(row)
        os.remove(txtPath)
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for rowIndex, rowData in enumerate(data):
            for colIndex, value in enumerate(rowData):
                cell = sheet.cell(row=1+rowIndex, column=1+colIndex, value=value)
                cell.data_type = 's'
        workbook.save(xlsxPath)         
    def AD5TtoTXT(self, ad5tPath):
        path = Path(ad5tPath)
        if path.exists():
            txtPath = path.with_suffix('.txt')
            shutil.copyfile(path, txtPath)
            return txtPath