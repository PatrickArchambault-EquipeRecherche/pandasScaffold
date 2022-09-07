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

# Change the encoding of NotANumber on import - useful when your data has 
# inadvertent entries that are not null, like sodium (NA)

from pandas._libs.parsers import STR_NA_VALUES

disable_na_values = { "NA" }
my_default_na_values = STR_NA_VALUES - disable_na_values
df = pandas.read_csv( "myCSVfile.csv" , na_values = my_default_na_values )