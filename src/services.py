import logging

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/services.txt",
    filemode="w",
)

search_logger = logging.getLogger("filtering_by_search")

file_operation = pd.read_excel("../data/operations.xlsx")


def filtering_by_search(search_string: str) -> pd.DataFrame:
    """Фильтруем транзакции по строке поиска"""
    try:
        search_operations = file_operation.loc[
            (file_operation["Категория"] == search_string.title())
            | (file_operation["Описание"] == search_string.title())
        ]
        search_logger.info("Функция отработала корректно")

        return search_operations
    except ExceptionGroup:
        search_logger.warning("функция не отработала, ошибка")