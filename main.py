from common.constants import SUBFOLDERS
from Extract_data import Data_create
from Create_Excel import Create_excel
from converters.XLSXConverter import XLSXConverter

def Generation_BigDate(Data1):
    Biiig_Data_list = []
    for key in Data1:
        for i in range(len(Data1[key])):
            Biiig_Data_list.append(Data1[key][i])
    return Biiig_Data_list

def main():
    root = input("root: ") # move to lanch param
    while True:
        name = input("param: ") # move to launch param
        converter = XLSXConverter(root, SUBFOLDERS)
        converter.AD5TtoXLSX()
        return

        # -------Извлекаем необходимые данные из файлов и переносим их в новый xlsx файл
        Data = Data_create(root, folder_1_name, folder_2_name, name)
        BigData = Generation_BigDate(Data)  # Список со всеми значениями
        Create_excel(Data, BigData, name, root)


if __name__ == "__main__":
    main()

