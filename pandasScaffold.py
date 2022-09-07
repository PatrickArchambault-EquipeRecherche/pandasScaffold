#!/usr/bin/python

"""A set of functions to make working with Python Pandas a little easier, or 
to collect idioms and patterns that are useful."""

import pandas

###### Functions ######

# Index on datetime column
def make_dt_index( dataframe , columnname ):
    """
    Usage example:
    hr = make_dt_index( pandas.read_csv("myCSVfile.csv"), "nameOfDateTimeColumnToIdexOn" )
    """
    dataframe[columnname] = pandas.to_datetime( dataframe[columnname] )
    dataframe = dataframe.set_index( dataframe[columnname] )

    return dataframe



###### Patterns ######

# Connect two or more dataframes together that probably overlap, dropping 
# whatever is duplicated
newDataFrame = pandas.concat( [firstDataFrame , secondDataFrame] ).drop_duplicates()