import pandas as pd
import datetime


def decorator(path_file: str = "../data/test.csv"):
    def writing_to_file(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result.to_csv(path_file)

            return result
        return wrapper
    return writing_to_file


trans = pd.read_excel("../data/operations.xlsx")


@decorator()
def spending_by_weekday(transactions: pd.DataFrame,
                        date: str = datetime.datetime.now()) -> pd.DataFrame:
    """
    Функция возвращает средние траты
    в каждый из дней недели за последние три месяца (от переданной даты)
    """
    date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
    month = int(date_obj.month) - 3
    today_3_months_ago = date_obj.replace(month=month).strftime("%d-%m-%Y")
    date_str = date_obj.strftime("%d-%m-%Y")

    filtred_trans = (
        transactions.loc)[(transactions["Дата платежа"] >= today_3_months_ago) | (transactions["Дата платежа"] <=
                                                                                  date_str)]

    result = (filtred_trans.groupby("Дата платежа")
              .agg({"Сумма операции": ["mean"]}))

    return result
