import datetime
import pandas as pd
import json
from external_api import get_currency_rates, get_stock_prices


def open_csv():
    file_scv = pd.read_csv("Data/operations.csv")
    return file_scv


def greeting():
    current_date_time = datetime.datetime.now()
    if 0 <= current_date_time.hour <= 8:
        return "Доброй ночи!"
    elif 9 <= current_date_time.hour <= 12:
        return "Доброе утро!"
    elif 13 <= current_date_time.hour <= 17:
        return "Добрый день!"
    else:
        return "Добрый вечер!"


def transactions(operations: pd.DataFrame) -> list[dict]:
    result = operations.groupby("Номер карты", as_index=False)
    total_sum_cashback = (
                          result.sum().loc)[:, ["Номер карты",
                                                "Сумма платежа",
                                                "Кэшбэк"]]

    return total_sum_cashback.to_dict(orient="records")


def five_transactions(operations: pd.DataFrame) -> list[dict]:
    top_five = operations.sort_values(by="Сумма платежа",
                                      ascending=False).head()
    result_top_five = top_five.loc[:, ["Дата платежа",
                                       "Сумма платежа",
                                       "Категория",
                                       "Описание"]]

    return result_top_five.to_dict(orient="records")

with open("user_settings.json", encoding="utf-8") as f:
    # открывает пользовательские настройки по акциям и валютам
    load_json_info = json.load(f)


def main(data):
    file = open_csv()
    date_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
    new_date_obj = date_obj.replace(day=1)

    slice_time_last = date_obj.strftime("%d.%m.%Y")
    slice_time_first = new_date_obj.strftime("%d.%m.%Y")

    slice_file_to_data = file[
        (file["Дата платежа"] >= slice_time_first) & (file["Дата платежа"] <= slice_time_last)
        ]
    main_dict = dict()
    main_dict['greeting'] = greeting()
    main_dict['cards'] = transactions(slice_file_to_data)
    main_dict['top_transactions'] = five_transactions(slice_file_to_data)
    main_dict['currency_rates'] = get_currency_rates(load_json_info['user_currencies'])
    main_dict['stock_prices'] = get_stock_prices(load_json_info['user_stocks'])
    return main_dict