import os
import re
from Reading_xlsx import read_xlsx_data_openpyxl

def Data_create(root_dir, folder_name1, folder_name2, name):
    folder_paths = {}
    Data = {}
    found_count = 0
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            if item == folder_name1 or item == folder_name2:
                folder_paths[item] = item_path
                found_count += 1
                if found_count == 2:
                    break
    if len(folder_paths) != 2:
        print(f"Не удалось найти обе папки: {folder_name1} и {folder_name2} в папке {root_dir}")
        return
    run(folder_name1, folder_paths, name, Data)
    run(folder_name2, folder_paths, name, Data)
    return Data

def run(folder_name, folder_paths, name, Data):
    SYS_WAFERID = -1
    index = -1
    number = 0
    for filename in os.listdir(folder_paths[folder_name]):
        check = False
        index_helper = -1
        if re.search(r"ShortMap", filename, re.IGNORECASE) is None:
            filepath = os.path.join(folder_paths[folder_name], filename)
            if os.path.isfile(filepath):
                data = read_xlsx_data_openpyxl(filepath)
                for i in range(len(data)):
                    if data[i][0] == "SYS_WAFERID":
                        SYS_WAFERID = int(data[i][1])
                    if data[i][0] == "VarName":
                        for n in range(len(data[i])):
                            if name.lower() == data[i][n].lower():
                                check = True
                                index_helper = n
                                break
                        if check:
                            index = index_helper
                        else:
                            SYS_WAFERID = -1
                            index = -1
                            continue
                    if SYS_WAFERID != -1 and index != -1 and data[i][0] == "StdDevi":
                        list_data = []
                        j = i + 1
                        while j != len(data) and data[j][index] is not None:
                            list_data.append(float(data[j][index]))
                            j += 1
                        match = re.search(r"[_-]0(\d)", filename)
                        if match:
                            number = int(match.group(1))
                            if number == 8:
                                if folder_name == "PMinDie" and number == 8:
                                    number = 9
                                elif folder_name == "PM" and number == 8 and (SYS_WAFERID == 15 or SYS_WAFERID == 16 or SYS_WAFERID == 17):
                                    number = 9
                        Data[(number, folder_name, SYS_WAFERID)] = list_data
                        SYS_WAFERID = -1
                        index = -1
                        check = False
                        index_helper = -1