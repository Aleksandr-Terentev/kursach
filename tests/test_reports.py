from src.reports import decorator
import pandas as pd
import pytest


def test_decorator(spending_result_fix):
    @decorator()
    def test_dataframe():
        df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
        return df

    assert type(test_dataframe().to_dict()) == type(spending_result_fix)


@pytest.mark.parametrize("param, expected", [("test", "test_fixture_value")])
def test_spending_by_weekday(param, expected, some_fixture):
    result = param + "_" + some_fixture
    assert result == expected
