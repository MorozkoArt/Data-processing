from pathlib import Path
import os

def convertTo_txt(path_str):
    path = Path(path_str)
    if path.exists():
        new_name = path.with_suffix('.txt')
        try:
            os.rename(path, new_name)
            return new_name
        except OSError as e:
            print(f"Ошибка при переименовании файла: {e}")
    else:
        print(f"Файл {path} не существует.")
