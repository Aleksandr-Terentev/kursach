import datetime
import pandas as pd


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
