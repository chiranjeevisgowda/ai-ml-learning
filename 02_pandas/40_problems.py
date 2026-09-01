import pandas as pd

#1.Load a CSV file into a DataFrame and print the first 10 rows, shape, and column names.
df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/survey_results_public.csv')
# print(df.head(10))
# print(df.shape)
# print(df.columns)

#2.Check the data type of each column and identify which columns need type conversion.
# print(df.dtypes) #Age needs type conversion to int instead of float

#3.Count the number of missing values in each column and display them sorted in descending order.
# print(df.isnull().sum().sort_values(ascending=False))

#4.Drop all rows where more than 2 columns have missing values.
# df = df.dropna(thresh=df.shape[1] - 2)
# print(df)

#5.Fill missing values in a numeric column with the column median, and in a string column with 'Unknown'.