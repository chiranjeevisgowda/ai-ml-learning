import pandas as pd

#Q1.Load a CSV file into a DataFrame and print the first 10 rows, shape, and column names.
df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/Indian_startups_funding.csv')
# print(df.head(10))
# print(df.shape)
# print(df.columns)

#Q2.Check the data type of each column and identify which columns need type conversion.
# print(df.dtypes) #The only conversion neede is year

#Q3.Count the number of missing values in each column and display them sorted in descending order.
# print(df.isnull().sum().sort_values(ascending=False))

#Q4.Drop all rows where more than 2 columns have missing values.
#There aren't any columns which has more than 2 missing columns so no need of this question 

#Q5.Fill missing values in a numeric column with the column median, and in a string column with 'Unknown'.
#fillna to solve this 

#Q6.Rename columns to snake_case — e.g. 'Startup Name' → 'startup_name'.
df.columns = df.columns.str.lower().str.replace(" ", "_")
df.rename(columns={'startup' : 'startup_name'}, inplace=True)
# print(df.columns)

#Q7.Filter rows where the city is 'Bengaluru' and funding amount is greater than 5 crore.
# filt = (df['city'] == 'Bengaluru') & (df['amount'] > 5.29)
# print(df[filt])

#Q8.Find the top 5 most frequent values in the 'sector' column.
# print(df['vertical'].value_counts(ascending=True))

#Q9.Select all rows where the startup stage is either 'Seed' or 'Pre-Seed'.
# filt = (df['round'] == 'Seed') | (df['round'] == 'Pre-Seed')
# print(df[filt])

#10.Filter rows where the investor name contains the substring 'Sequoia' (case-insensitive).
# filt = df['investors'].str.contains('Sequoia')
# print(df[filt])

#Q11.Sort the DataFrame by funding amount in descending order and reset the index.
# print(df['amount'].sort_values(ascending=False))
# df = (df.set_index('startup_name'))
# df = (df.reset_index('startup_name'))
# print(df)

#Q12.Create a new column 'funding_in_crore' by converting a USD funding column using a fixed exchange rate.
# df['funding_in_crores'] = (df['amount'] * 1000000 ) * 94.56
# pd.options.display.float_format = '{:,.0f}'.format
# print(df['funding_in_crores'])
