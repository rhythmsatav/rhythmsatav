import pandas as pd
import dash


#product, sales(qauntity*price), region

df = pandas.read_csv('daily_sales_data_0.csv')

#selecting only the pink morsel
df = [df['product'].str.contains('pink morsel')]

print(df)