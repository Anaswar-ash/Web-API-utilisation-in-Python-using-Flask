
import pandas as pd
import numpy as np
from src.data_cleaner import clean_data

def test_remove_duplicates():
    data = {'A': [1, 2, 2, 3], 'B': ['x', 'y', 'y', 'z']}
    df = pd.DataFrame(data)
    cleaned_df = clean_data(df)
    assert len(cleaned_df) == 3

def test_fill_missing_values():
    data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]}
    df = pd.DataFrame(data)
    cleaned_df = clean_data(df)
    assert cleaned_df.isnull().sum().sum() == 0
    assert cleaned_df['A'].iloc[2] == np.mean([1, 2, 4])

def test_correct_data_type():
    data = {'A': [1, 2, 3], 'B': ['4', '5', '6']}
    df = pd.DataFrame(data)
    cleaned_df = clean_data(df, column_to_correct='B')
    assert pd.api.types.is_numeric_dtype(cleaned_df['B'])
