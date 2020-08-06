"""
Some functions to help cleaning and handling dataframes.
"""

import pandas as pd


def report_missing_values(df):
    """Print a pretty report of missing values."""
    print(pd.DataFrame.isnull())


def values_fix(value):
    '''This function takes repeated string values in a list and covert them into one single value
for each repeated values'''
    for k, v in list.items():
        if value.lower() in v:
            return k
