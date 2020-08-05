def names_fix(name):
    '''This function takes repeated string values in a list and covert them into one single value
for each repeated values'''
    for k, v in list.items():
        if name.lower() in v:
            return k


"""
Some functions to help cleaning and handling dataframes.
"""
import pandas as pd
def report_missing_values(df):
    """Print a pretty report of missing values."""
    print(df.isnull())




class Person:
     def __init__(self, name, age):
         self.name = name
         self.name = age

     def introduceyourself(self):
         print("My name is " + self.name)
         print('My age is '+ str(self.age))

author = Person(input('Whats your name?')

