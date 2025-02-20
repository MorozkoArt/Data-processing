import openpyxl

def read_xlsx_data_openpyxl(filename):
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(list(row))
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        return None