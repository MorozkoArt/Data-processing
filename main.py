from Converters.Converter_ad5t_To_xlsx import ad5t_TO_xlsx
from Extract_data import Data_create
from Create_Excel import Create_excel

def Generation_BigDate(Data1):
    Biiig_Data_list = []
    for key in Data1:
        for i in range(len(Data1[key])):
            Biiig_Data_list.append(Data1[key][i])
    return Biiig_Data_list

folder_1_name = "PM"
folder_2_name = "PMinDie"
root_directory = input("Введите путь к директории, в которой хранятся папки: \"PM\" и \"PMinDie\": ")

while True:
    name = input("Введите название из списка параметров (Для завершения введите \"End\"): ")
    if name == "End":
        exit()
    # -------Если файлы не в .xlsx, то конвертируем
    ad5t_TO_xlsx(root_directory, folder_1_name, folder_2_name)

    # -------Извлекаем необходимые данные из файлов и переносим их в новый xlsx файл
    Data = Data_create(root_directory, folder_1_name, folder_2_name, name)
    Biiig_Data = Generation_BigDate(Data)  # Список со всеми значениями
    Create_excel(Data, name, root_directory)



