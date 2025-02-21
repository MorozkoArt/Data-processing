import os
from pathlib import Path
import shutil
import openpyxl
from openpyxl.cell import Cell
from common.utils import subfolderNotFoundWarning


class XLSXConverter:
    def __init__(self, root, subfolders):
        self.root = root
        self.subfolders = subfolders
    def AD5TtoXLSX(self):
        subPaths = self.subfolderPaths()
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
    def subfolderPaths(self):
        left = self.subfolders.copy()
        paths = []
        for item in os.listdir(self.root):
            path = os.path.join(self.root, item)
            if os.path.isdir(path):
                if item in self.subfolders:
                    paths.append(path)
                    left.remove(item)
        for item in left:
            subfolderNotFoundWarning(item)
        return paths