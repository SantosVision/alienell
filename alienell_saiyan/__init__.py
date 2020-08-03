def names_fix(name):
    '''This function takes repeated string values in a column and covert them into one single values '''
    for k, v in cult.items():
        if name.lower() in v:
            return k


"""
Some functions to help cleaning and handling dataframes.
"""
import pandas as pd
def reporting_missing_values(df):
    """Print a pretty report of missing values."""
    print(pd.DataFrame().isnull())
