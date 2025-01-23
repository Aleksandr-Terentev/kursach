import json
import datetime
from src.views import greeting, transactions, open_csv, five_transactions
from src.external_api import get_currency_rates, get_stock_prices



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


#print(main('15.12.2021'))


