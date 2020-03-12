import pandas as pd
import matplotlib.pyplot as mpl  # tool for plotting

pd.options.display.float_format = '{:.2f}'.format # 2 decimals
pd.set_option('display.max_rows', 500) # show 500 max rows
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000) #shows 1000 max characters in 1 row.

dataset=pd.read_csv("50000 Sales Records.csv", nrows=10000, parse_dates=True, infer_datetime_format=True)
#read the first 10 rows; parse: if see a date, make it a date, not string; date format, xx/xx/xxxx

print(dataset)

#change the name of headers to a more readable way. Change "total revenue" to "total_revenue".

print(dataset.keys())  #get header

dataset.columns = dataset.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

print(dataset.columns) #get header

b=dataset.keys()
c=dataset.columns # b=c here, but we can WRITE with 'dataset.columns', we can only read/get values with 'dataset.keys().

print(dataset.unit_price.describe())  #describe the column of unit_price

print(dataset.country.describe())

print(dataset.unit_price.max())  #give me the max number in the column of unit_price
print(dataset.unit_price.sum())
print(int(dataset.unit_price.mean()))

print(dataset.region.value_counts())  #has to count STRING

print(dataset.region.unique()) # all unique regions

print(dataset.region.values) # the list of all values

print(dataset.total_revenue.describe())

print("#####")
print(dataset.describe(include=object)) # non-value types listed here; values are treated as object/string, not numercial
print("#####")
print(dataset.describe()) # value types listed here
print("#####")

#get aggregate value of region

print(dataset.groupby("region")["units_sold"].sum()["Europe"]) # sum for Europe


# plotting, way 1
a=dataset.groupby("region")["units_sold"].sum()    # extract units_sold, then generate sum

a.plot(kind='bar', x='region', y='units_sold')
mpl.show() # show the plot by calling mpl

a.plot(kind='pie', x='region', y='units_sold')
mpl.show()

#plotting, way 2


















