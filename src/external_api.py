import json
import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_CURRENCY = os.getenv("API_KEY_CURRENCY")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/external_api.txt",
    filemode="w",
)

open_logger = logging.getLogger("open_file")
get_currency_logger = logging.getLogger("get_currency_rates")
get_stock_logger = logging.getLogger("get_stock_prices")


try:
    with open("../user_settings.json", encoding="utf-8") as f:
        # открывает пользовательские настройки по акциям и валютам
        load_json_info = json.load(f)
        open_logger.info("Файл открыт для чтения")
except FileNotFoundError:
    open_logger.error("Путь/файл некорректный")


def get_currency_rates(currencies: list) -> list[dict]:
    """
    Функция принимает список валют из пользовательских настроек
    делает запрос и возвращает список
    со стоимостью каждой валюты по курсу на сегодня
    """
    rates = []
    try:
        for currency in currencies:
            response = (requests.get
                        (f"https://v6.exchangerate-api.com/v6/"
                         f"{API_KEY_CURRENCY}/latest/{currency}"))

            status_code = response.status_code
            get_currency_logger.info(f"Статус код запроса {status_code}")

            try:
                data = response.json()
                (rates.append
                 ({"currency": currency,
                   "rate": data["conversion_rates"]["RUB"]}))
            except KeyError:
                (get_currency_logger.error
                 ("не найден ключ. keyerror"))

        get_currency_logger.info("Сделали запрос, "
                                 "получили стоимость валют из польз. настроек")

        return rates
    except ExceptionGroup:
        get_currency_logger.warning("ошибка в запросе")
        return rates


def get_stock_prices(stocks: list) -> list[dict]:
    """
    Принимает пользовательские настройки (выбор акций)
     и возвращает стоимость акций
    в $ на начало текущего дня
    """
    prices = []
    try:
        for stock in stocks:
            params = {
                "apikey": f"{API_KEY}",
                "interval": "1day",
                "format": "JSON",
                "type": "stock",
                "symbol": f"{stock}",
                "outputsize": 1,
                "timezone": "Europe/Moscow",
            }

            response = requests.get("https://api.twelvedata.com/time_series",
                                    params=params)
            get_stock_logger.info("запрос статус = 200, отработал")

            data = response.json()
            prices.append({"stock": stock, "price": data["values"][0]["close"]})

        return prices
    except ExceptionGroup:
        get_stock_logger.warning("ошибка в запросе")


print(get_currency_rates(load_json_info['user_currencies']))
#print(get_stock_prices(load_json_info['user_stocks']))
#print(load_json_info)
