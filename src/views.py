import datetime
import json
import logging

import pandas as pd

from external_api import get_currency_rates, get_stock_prices
from utils import get_info_cards, greeting, top_transactions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/views.txt",
    filemode="w",
)

opening_logger = logging.getLogger("opening_file")
views_logger = logging.getLogger("views")


def opening_file(path_file: str) -> pd.DataFrame:
    """Функция читает файл формата xlsx и возвращает DataFrame"""
    operations_xlsx = pd.read_excel(path_file)

    opening_logger.info("Функция отработала")

    return operations_xlsx


def views(data: str) -> str:
    """
    принимает строку с датой, возвращает инфо по операциям с начала месяца по текущую дату
    """
    info_file = opening_file("../data/operations.xlsx")  # Открываем файл с операциями
    sort_file = info_file.sort_values(by="Дата платежа", ascending=True)

    views_logger.info("открытие файла успешно, opening_file отработал")

    date_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
    new_date_obj = date_obj.replace(day=1)

    slice_time_last = date_obj.strftime("%d.%m.%Y")
    slice_time_first = new_date_obj.strftime("%d.%m.%Y")

    slice_file_to_data = sort_file[
        (sort_file["Дата платежа"] >= slice_time_first) & (sort_file["Дата платежа"] <= slice_time_last)
    ]

    views_logger.info("сортировка файла по графе дата платежа")

    with open("../user_settings.json", encoding="utf-8") as f:  # открываем польз. настройки по акциям и валютам
        load_json_info = json.load(f)

    views_logger.info("открытие файла польз. настроек Успешно")

    informations_user = dict()

    informations_user["greeting"] = greeting()  # функция приветствия
    views_logger.info("greeting отработал")

    informations_user["cards"] = get_info_cards(slice_file_to_data)  # функция получения инфо по параметрам из файла
    views_logger.info("get_info_cards отработал")

    informations_user["top_transactions"] = top_transactions(slice_file_to_data)  # вывод топ транзакций по сумме
    views_logger.info("top_transactions отработал")

    informations_user["currency_rates"] = get_currency_rates(load_json_info["user_currencies"])  # функция
    # получения текущего курса валют(валюты из польз. настроек)
    views_logger.info("get_currency_rates отработал")

    informations_user["stock_prices"] = get_stock_prices(load_json_info["user_stocks"])  # функция получения текущего
    # курса стоимости акций (акции из польз. настроек)
    views_logger.info("get_stock_prices отработал")

    return json.dumps(informations_user, ensure_ascii=False, indent=4)


if __name__ == 'main':
    print(views('01.01.2021'))