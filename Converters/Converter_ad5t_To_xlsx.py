import os
from Converters.ConvertTo_xlsx import txt_to_xlsx
from Converters.ConverterTo_txt import convertTo_txt

def ad5t_TO_xlsx(root_dir, folder_name1, folder_name2):
    folder_paths = {}
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

    for filename in os.listdir(folder_paths[folder_name1]):
        filepath = os.path.join(folder_paths[folder_name1], filename)
        if os.path.isfile(filepath):
            root, ext = os.path.splitext(filepath)
            if ext.lower()!='.xlsx':
                new_txt_filepath = convertTo_txt(filepath)
                txt_to_xlsx(new_txt_filepath)

    for filename in os.listdir(folder_paths[folder_name2]):
        filepath = os.path.join(folder_paths[folder_name2], filename)
        if os.path.isfile(filepath):
            root, ext = os.path.splitext(filepath)
            if ext.lower() != '.xlsx':
                new_txt_filepath = convertTo_txt(filepath)
                txt_to_xlsx(new_txt_filepath)