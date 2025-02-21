import os
import re
import openpyxl
from common.subfolderPaths import subfolderPaths


class Parser:
    def __init__(self, root, subfolders, param):
        self.root = root
        self.subfolders = subfolders
        self.param = param
    def convertToBigData(self, parsed=None):
        if parsed is None:
            parsed = self.parseParamData()
        bigData = []
        for key in parsed:
            for i in range(len(parsed[key])):
                bigData.append(parsed[key][i])
        return bigData
    def parseParamData(self):
        subPaths = subfolderPaths(self.root, self.subfolders)
        data = {}
        for subPath in subPaths:
            for filename in os.listdir(subPath):
                path = os.path.join(subPath, filename)
                data.update(self.parseParamDataFromFile(path, filename))
        return data
    def parseParamDataFromFile(self, path, filename):
        if re.search(r"ShortMap", filename, re.IGNORECASE) is not None:
            return {}
        if not os.path.isfile(path):
            return {}
        rawData = self.readXLSX(path)
        parsed = {}
        waferId = -1
        colIndex = -1
        for row in range(len(rawData)):
            if rawData[row][0] == "SYS_WAFERID":
                waferId = int(rawData[row][1])
            if rawData[row][0] == "VarName":
                for col in range(len(rawData[row])):
                    if self.param.lower() == rawData[row][col].lower():
                        colIndex = col
                        break
            if waferId != -1 and colIndex != -1 and rawData[row][0] == "StdDevi":
                chunk = []
                index = row + 1
                while index != len(rawData) and rawData[index][colIndex] is not None:
                    chunk.append(float(rawData[index][colIndex]))
                    index += 1
                match = re.search(r"[_-]0(\d)", filename)
                folderPath = os.path.dirname(path)
                folderName = os.path.basename(folderPath)
                if match:
                    category = int(match.group(1))
                    if category == 8:
                        if folderName == "PMinDie" and category == 8:
                            category = 9
                        elif folderName == "PM" and category == 8 and waferId in [15, 16, 17]:
                            category = 9
                parsed[(str(category), folderName, str(waferId))] = chunk
                waferId = -1
                colIndex = -1
        return parsed
    def readXLSX(self, path):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))
        return data