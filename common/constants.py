SUBFOLDERS=["PM", "PMinDie"]
RESULT_FOLDER="Results"

ANOMALIES_SHEET_NAME="Аномалии"
ANOMALIES_BETA=3
ANOMALIES_PARAMS_HEADINGS = ["N", "Ср.знач", "Ср.кв.откл", "β"]
ANOMALIES_PARAMS_VALUES = ["paramCount", "paramAvg", "paramDeviation", "paramBeta"]
ANOMALIES_DATA_HEADINGS = {
    "InitialColumn": ["№", "Выборка", "Вариац.ряд", "Ui"],
    "IterationalColumn": ["№", "Вариац.ряд", "Ui"]
}
ANOMALIES_DATA_VALUES = {
    "InitialColumn": ["dataCounter", "dataRaw", "dataSorted", "dataUi"],
    "IterationalColumn": ["dataCounter", "dataSorted", "dataUi"]
}
ANOMALIES_BLOCKS_OFFSETS = {
    "InitialColumn": {
        "params": {
            "col": 0,
            "row": 0
        },
        "data": {
            "col": 0,
            "row": 2
        }
    },
    "IterationalColumn": {
        "params": {
            "col": 0,
            "row": 0
        },
        "data": {
            "col": 0,
            "row": 2
        }
    }
}
ANOMALIES_COMPARABLE_FUNC="dataUi"
ANOMALIES_NUMBER_FORMAT_CONDITIONS={
    "from": 0.01,
    "to": 10000
}
ANOMALIES_NORMAL_NUMBER_FORMAT="0.00"
ANOMALIES_STRICT_NUMBER_FORMAT="0.00E+00"
ANOMALIES_ERROR_TEXT_COLOR="FFFFFF"
ANOMALIES_ERROR_BACKGROUND_COLOR="FF0000"
ANOMALIES_SUCCESS_TEXT_COLOR="000000"
ANOMALIES_SUCCESS_BACKGROUND_COLOR="00FF00"

PARSED_SHEET_NAME="Данные"
PARSED_HEADINGS={
    "4": {
        "PMinDie": ["1", "2"],
        "PM": ["3", "4"]
    },
    "8": {
        "PM": ["2", "3", "4"]
    },
    "9": {
        "PMinDie": ["1", "2", "3"],
        "PM": ["15", "16", "17"]
    },
}
PARSED_NUMBER_FORMAT="0.00E+00"