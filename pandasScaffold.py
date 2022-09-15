#!/usr/bin/python

"""A set of functions to make working with Python Pandas a little easier, or 
to collect idioms and patterns that are useful."""

import pandas

###### Functions ######

# Find outliers in a column, characterize the data, count outliers, nulls
def inspect_column( columnname ):
    desc = f"""{columnname}\n
    Nulls: {columnname.isna().sum()}"""


    return desc


# Index on datetime column
def make_dt_index( dataframe , columnname ):
    """
    Usage example:
    hr = make_dt_index( pandas.read_csv("myCSVfile.csv"), "nameOfDateTimeColumnToIndexOn" )
    """
    dataframe[columnname] = pandas.to_datetime( dataframe[columnname] )
    dataframe = dataframe.set_index( dataframe[columnname] )

    return dataframe


# Plot rows over time, based on a rows-per-interval approach
def plotRowsOverTime( dataframe , frequency ):
    """
    The dataframe has to be using a datetime column as the index.
    You then specify the frequency that you are looking for results on, i.e.
    day, month, year, etc.
    Day = D
    Month = M
    Read "pandas Grouper" documentation for details.
    """
    dataframe.groupby(pandas.Grouper(freq=frequency)).size().plot()


###### Patterns ######

# Connect two or more dataframes together that probably overlap, dropping 
# whatever is duplicated
firstDataFrame = pandas.DataFrame()
secondDataFrame = pandas.DataFrame()
newDataFrame = pandas.concat( [firstDataFrame , firstDataFrame] ).drop_duplicates()


# Change the encoding of NotANumber on import - useful when your data has 
# inadvertent entries that are not null, like sodium (NA)
from pandas._libs.parsers import STR_NA_VALUES

disable_na_values = { "NA" }
my_default_na_values = STR_NA_VALUES - disable_na_values
df = pandas.read_csv( "myCSVfile.csv" , na_values = my_default_na_values )


# Pad out values with 4 leading zeros on pandas.read_csv()
df = pandas.read_csv("myCSVfile.csv", converters={'UnpaddedColumn1': '{:0>4}'.format, 'UnpaddedColumn2': '{:0>4}'.format}) 

# Filter a dataframe into a subset that all meets a criteria.
# In the example case, we use pandas.factorize() to get all of the values, 
# because it _should_ be a small set, but there are mispellings, other 
# weirdness that we have to find, so this pattern lets us group all rows 
# that have the set of values in the list
pos = ['DÉTECTÉ', 'DÉTEDÉTECTÉ', 'detecté', 'detecte', '03DÉTECTÉ']

posCases = labsDF[labsDF["RESULTAT"].isin(pos)]

