import pandas as pd

#Q1.Load a CSV file into a DataFrame and print the first 10 rows, shape, and column names.
df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/Recently Funded Startups In India 2026.csv')
# print(df.head(10))
# print(df.shape)
# print(df.columns)

#Q2.Check the data type of each column and identify which columns need type conversion.
# print(df.dtypes) #Funding amount needs to be converted 

#Q3.Count the number of missing values in each column and display them sorted in descending order.
# print(df.isnull().sum().sort_values(ascending=False))

#Q4.Drop all rows where more than 2 columns have missing values.
# print(df.dropna(thresh=len(df.columns) - 2))

#Q5.Fill missing values in a numeric column with the column median, and in a string column with 'Unknown'.
cleaned = df['Funding Amount (USD)'].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
df['Funding Amount (USD)'] = pd.to_numeric(cleaned, errors='coerce')
# median = df['Funding Amount (USD)'].median()
# df['Funding Amount (USD)'] = df['Funding Amount (USD)'].fillna(median)

#Q6.Rename columns to snake_case — e.g. 'Startup Name' → 'startup_name'.
# df.columns = df.columns.str.lower().str.replace(" ", "_")
# print(df.columns)

#Q7.Filter rows where the city is 'Bengaluru' and funding amount is greater than 5 crore.
# filt = (df['Country'] == 'India') & (df['Funding Amount (USD)'] >= 5000000)
# print(df[filt])

#Q8.Find the top 5 most frequent values in the 'sector' column.
df['Industry'] = (df['Industry']
                  .str.split(",")
                  .explode('Industry')
                  .str.strip())
# print(df['Industry'].value_counts())


#Q9.Select all rows where the startup stage is either 'Seed' or 'Pre-Seed'.
# filt = (df['Funding Type'] == 'Seed') | (df['Funding Type'] == 'Pre-Seed')
# print(df[filt])

#Q10.Filter rows where the investor name contains the substring 'Sequoia' (case-insensitive).
# filt = df['Industry'].str.contains('Artificial Intelligence')
# print(df[filt])

#Q11.Sort the DataFrame by funding amount in descending order and reset the index.
# print(df['Funding Amount (USD)'].sort_values(ascending=False))
# df = df.set_index('Name')
# print(df)

#Q12.Create a new column 'funding_in_crore' by converting a USD funding column using a fixed exchange rate.
# fixed_exchange_rate = 94.57
# df['funding_in_crore'] = round(df['Funding Amount (USD)'] * fixed_exchange_rate)
# print(df['funding_in_crore'])

#Q13.Group by 'sector' and calculate total funding, average funding, and deal count for each.
