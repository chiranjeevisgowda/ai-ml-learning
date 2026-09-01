import pandas as pd
# df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/netflix_titles.csv')
# print(df.head(8))
# print(df.tail(8))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info)
# print(df['title'])
# print(df['director'])
# print(df['country'])
# print(df.iloc[15:26,[1,2,7]])
# print(df[df['type']=='Movie'])
# print(df[df['type']=='TV Show'])
# print(df.loc[df['release_year'] > 2018, ['title', 'release_year']])
# print(df.loc[df['country'] == 'India', ['title','type' , 'country']])
# print(df.loc[df['release_year'] == 2020, ['title', 'rating', 'duration']])
# print(df.loc[100 : 110, ['title', 'director', 'rating']])
# pd.set_option('display.max_rows', None)
# print(df.loc[df['rating']=='TV-MA', ['title']])
# print(df.query("type == 'Movie' and release_year > 2015 and country == 'India'")[['title', 'release_year', 'duration']])
# print(df.query("release_year > 2009 or release_year < 2016"))
# print(df.iloc[50:71, [2,7,8,9]])
# print(df.query("type == 'Movie' and rating == 'PG-13'"))
#6131 movies in total
#2676 TV Show in total
# freq = {}
# for year in df['release_year']:
#     if year not in freq:
#         freq[year] = 1
#     else:
#         freq[year] += 1
# highest_key = max(freq, key=freq.get)
# print(highest_key)

#1st Question
# filt = ((df['type'] == 'Movie') & (df['release_year'] >= 2019) & ((df['country'] == 'India') | (df['country'] == 'South Korea') | (df['country'] == 'Japan')))
# print(df.loc[filt])

# #2nd Question
# Documentaries = ((df['listed_in'].str.contains('Documentaries', na=False)) & (df['rating'] == 'TV-MA'))
# print(df.loc[Documentaries])

# #3rd Question
# df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/netflix_titles.csv', index_col='show_id')
# print(df.loc[['s150', 's151'], ['title', 'director']])


# people = {
#     'name' : ['Chiru', 'Priya', 'Prema'],
#     'last' : ['Gowda', 'gowda', 'CG'],
#     'email' : ['chiru@gmail.com', 'priya@gmail.com', 'prema@gmail.com']
# }

# df = pd.DataFrame(people)
# df.columns = df.columns.str.replace(' ', '_')
# df.rename(columns={'name' : 'first_name', 'email' : 'email_address'}, inplace=True)
# filt = df['last'] == 'Gowda'
# df.loc[filt, 'first_name'] = 'John'
# print(df['email_address'].apply(lambda x:len(x)))
# df['full_name'] = df['first_name'] + " " + df['last'] 
# df.drop(['first_name', 'last'], axis=1, inplace=True) #I aslo tried to assign it directly to df and it worked but i then shifted to inplace it seemed natural 
# new_row = pd.DataFrame([{'full_name': 'Jane Doe', 'email': 'jane@email.com'}])
# df = pd.concat([df, new_row], ignore_index=True)
# print(df)