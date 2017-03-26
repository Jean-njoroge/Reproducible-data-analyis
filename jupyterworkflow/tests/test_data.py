from jupyterworkflow.data import get_fremont_data
import pandas as pd

# unit test function using pytest

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance (data.index, pd.DatetimeIndex)

