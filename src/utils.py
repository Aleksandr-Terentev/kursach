import datetime
import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/utils.txt",
    filemode="w",
)

greeting_logger = logging.getLogger("greeting")
info_cards_logger = logging.getLogger("get_info_cards")
top_transactions_logger = logging.getLogger("top_transactions")


def greeting() -> str:
    """возвращает приветствие, в зависимости от времени"""

    time = datetime.datetime.now().hour
    greeting_logger.info("функция отработала")
    if time in range(0, 7):
        return "Доброй ночи"
    elif time in range(6, 13):
        return "Доброе утро"
    if time in range(12, 19):
        return "Добрый день"
    else:
        return "Добрый вечер"


def get_info_cards(operations_xlsx: pd.DataFrame) -> list[dict]:
    """принимает DataFrame и сортирует по параметрам"""
    group_card = operations_xlsx.groupby("Номер карты", as_index=False)

    total_sum_cashback = group_card.sum().loc[:, ["Номер карты", "Сумма платежа", "Кэшбэк"]]

    return total_sum_cashback.to_dict(orient="records")


def top_transactions(operations_xlsx: pd.DataFrame) -> list[dict]:
    """принимает DataFrame и выводит топ 5 транзакций"""
    top_5_operation = operations_xlsx.sort_values(by="Сумма платежа").head()
    information = top_5_operation.loc[:, ["Дата платежа", "Сумма платежа", "Категория", "Описание"]]

    top_transactions_logger.info("Функция отработала")

    return information.to_dict(orient="records")
