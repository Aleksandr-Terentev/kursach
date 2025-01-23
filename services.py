from src.views import open_csv


def easy_search(user_str: str) -> list[dict]:
    transactions = open_csv()
    result = transactions.loc[(user_str.title() == transactions['Категория']) | (user_str.title() == transactions['Описание'])]
    return result

print(easy_search('Колхоз'))