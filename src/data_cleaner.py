
import pandas as pd

def clean_data(df, column_to_correct=None):
    """Cleans the DataFrame by removing duplicates, correcting data types, and filling missing values."""
    df = df.copy()
    df = df.drop_duplicates()
    
    if column_to_correct and column_to_correct in df.columns:
        df[column_to_correct] = pd.to_numeric(df[column_to_correct], errors='coerce')
        
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())
        
    return df
