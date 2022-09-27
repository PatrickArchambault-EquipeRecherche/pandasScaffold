# scaffold-pandas
Helper functions to do common things in Pandas

These are things I learned how to do in Python Pandas, and want to more easily, but it will also include examples of code that helps explain useful ways of solving problems.

## Functions Included:

`scaffold-pandas`.`**byType**`(`*series, printout=False*`)
Returns a dictionary which includes the contents of the series divided into six lists, which are "integers", "strings", "floats", "booleans", "nones", and "others". If the "printout" flag is True, it also prints the counts of each type.

Mostly used to tell you useful things about a column, and enable other tools like returning minimum and maximum values.


