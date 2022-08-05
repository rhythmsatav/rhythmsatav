import pandas as pd
import dash


#product, sales(qauntity*price), region

df = pd.read_csv('C:\Users\rhyth\Quantium Virtual Experience\daily_sales_data_0.csv')

#selecting only the pink morsel
df = [df['product'].str.contains('pink morsel')]


df['sales'] = df['quantity'] * df['price']


#delete price column
df.pop('price')
df.pop('quantity')


# rename quantity to sales

# df.rename(columns={"quantity": "sales"}, inplace=True)


#delete product column
df.pop('product')

print(df)