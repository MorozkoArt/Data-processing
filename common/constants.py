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