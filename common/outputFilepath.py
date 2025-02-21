import os
from common.constants import RESULT_FOLDER

def outputFilePath(root, param):
    filename = "ТК-ТХ503___Расчет___"+param+".xlsx"
    full_path = os.path.join(root, RESULT_FOLDER)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return os.path.join(full_path, filename)