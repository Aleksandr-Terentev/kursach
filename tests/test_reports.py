from src.reports import decorator, spending_by_weekday
import pandas as pd


def test_decorator(spending_result_fix):
    @decorator()
    def test_dataframe():
        df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
        return df

    assert type(test_dataframe().to_dict()) == type(spending_result_fix)


def test_spending_by_weekday(result_spending_by_weekday):
    assert result_spending_by_weekday == {}


