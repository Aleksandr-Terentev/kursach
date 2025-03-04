import pytest


@pytest.fixture
def get_currency_usd():
    return {'currency': 'USD', 'rate': 88.1883}


@pytest.fixture
def get_currency_eur():
    return {'currency': 'EUR', 'rate': 96.2559}


@pytest.fixture
def get_stocks_aapl():
    return [{'stock': 'AAPL', 'price': '224.58350'}]


@pytest.fixture
def get_requests_aapl():
    return {
        'meta': {
            'symbol': 'AAPL',
            'interval': '1day',
            'currency': 'USD',
            'exchange_timezone': 'America/New_York',
            'exchange': 'NASDAQ',
            'mic_code': 'XNGS',
            'type': 'Common Stock'
        },
        'values':
        [
            {
                'datetime': '2024-07-19',
                'open': '224.85201',
                'high': '226.80000',
                'low': '223.27499',
                'close': '224.58350',
                'volume': '34289484'
            }
        ],
        'status': 'ok'
    }


@pytest.fixture
def spending_result_fix():
    return {'Yes': [50, 21], 'No': [131, 2]}


@pytest.fixture
def result_spending_by_category():
    return {
        'MCC': {},
        'Бонусы (включая кэшбэк)': {},
        'Валюта операции': {},
        'Валюта платежа': {},
        'Дата операции': {},
        'Дата платежа': {},
        'Категория': {},
        'Кэшбэк': {},
        'Номер карты': {},
        'Округление на инвесткопилку': {},
        'Описание': {},
        'Статус': {},
        'Сумма операции': {},
        'Сумма операции с округлением': {},
        'Сумма платежа': {}
    }


@pytest.fixture
def some_fixture():
    return "fixture_value"


@pytest.fixture
def result_spending_by_category_():
    return {}
