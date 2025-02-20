import openpyxl
import os
from openpyxl.cell import Cell


def txt_to_xlsx(txt_filepath, delimiter='\t'):
    data = []
    root, ext = os.path.splitext(txt_filepath)
    xlsx_filepath = root+".xlsx"
    try:
        with open(txt_filepath, 'r', encoding='utf-8') as txt_file:
            for line in txt_file:
                row = line.strip().split(delimiter)
                data.append(row)
        os.remove(txt_filepath)
    except FileNotFoundError:
        print(f"Ошибка: Файл {txt_filepath} не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла {txt_filepath}: {e}")
        return

    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                cell = Cell(sheet, row=row_index + 1, column=col_index + 1, value=cell_data)
                cell.data_type = 's'  # Явно указываем, что это текст
                sheet._cells[(row_index + 1, col_index + 1)] = cell # Присваиваем ячейку листу
        workbook.save(xlsx_filepath)
        print(f"Файл {txt_filepath} успешно конвертирован в {xlsx_filepath}")
    except Exception as e:
        print(f"Ошибка при записи в файл {xlsx_filepath}: {e}")