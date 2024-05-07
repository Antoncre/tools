# tools
Useful tools for python applications

## csv_fill.py
The funciton will create a csv file with randomly generated values in a following structure: todays_date, number, random_set_of_characters
I am using this function to test behavior of my Finances application when there are too many elements to display

Usage:
the following code will create a file named 'Transactions.csv' and fill it with 450 lines of data in the structure mentioned above
```python
from csv.fill import fill_csv

fill_csv(450, 'Transactions.csv')
```

