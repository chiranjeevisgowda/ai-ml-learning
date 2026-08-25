import pandas as pd
people = {
    'name' : ['Chiru', 'Priya', 'Prema'],
    'last' : ['Gowda', 'gowda', 'CG'],
    'email' : ['chiru@gmail.com', 'priya@gmail.com', 'prema@gmail.com']
}

df1 = pd.DataFrame(people)
# # print(df.set_index('email'))
# filt = (df['last'] == 'Gowda') | (df['name'] == 'Chiru')
# print(df.loc[filt, 'email'])

# df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/netflix_titles.csv')
# pd.set_option('display.max_columns', 85)
# # pd.set_option('display.max_rows', None)
# # release_year = (df['release_year'] == 2020)
# # print(df.loc[release_year, ['title' , 'country']])
# countries = ('United States', 'India')
# filt = df['country'].isin(countries)
# print(df.loc[filt, 'country'])


#So basically we can set custome indexs for better access of the data so to do that \ 
#Inplace specifies that the email is set as the main index for the entire data whenever we print the data 
#it is useful for searching and other purpose using loc
df1.set_index('email', inplace=True)
# print(df1)

#For example if i want to search the other deatils of the person with the index we have specified we can just input the index value to get the output 
print(df1.loc['chiru@gmail.com'])
#If we jsut want the last name or any other specific column value of the person we could just input that also 
print(df1.loc['chiru@gmail.com', 'last'])
#If we have already set the index then we cannot use the traditional index value such as 0 and n numbers to access the value to do that we can stil ues iloc 
print(df1.iloc[0, 0])
#So if we want to have the index to be normal again no custom index then we can jsut use the reset index method to do so 
df1.reset_index(inplace=True)
#so if we use the custom index value after we reset the custom index then we get an error 
# try:
#     print(df1.loc['chiru@gmail.com'])
# except KeyError:
#     print("Custom index not valid")
#So we can even set custom indexs at the start of the program where we define the variable to do so we can use index_col 
df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/StudentsPerformance.csv', index_col='race/ethnicity')
print(df.loc['group A'])
#So as for the real world example given by Corey Schafer is when we the schema dataset for the data set if we want to know what the column actually
#represents instead of remembering the index value of the column we can jsut set the column as the main index and just type the name of the column which we want to get the deatils off


#So we can also use a method which is used to sort the index which is sort_index as simple and if we want the index to be in descending value we input the value ascending = False
print(df.sort_index())
print(df.sort_index(ascending=False))
#So one more thing inplcae is something which we can use on a regualr basis to tell the system that it should be permanent until i change it myself


#So now we start with the data FILTERING how to use logical operators and others on the data to get the value more properly 
#So if we jsut use this the we get the output in the boolean format if we want the actual columns of the condition we can either assign the value to a variabale for example
filt = df1['last'] == 'Gowda'
print(df1['last'] == 'Gowda')
#Then call that variable 
print(df1[filt])
#Else we can just directly input it when printing the value instead of creating a separate variable for it 
print(df1[df1['last'] == 'Gowda'])
#In pandas as I mentioned we can use logical or and logical and for comparison and cleaning data for example 
#So if the value is not present then we the no error instead we get that the datafram is empty and it gives out the colums and index[]
filt1 = (df1['last'] == 'Gowda') & (df1['name'] == '')
print(df1.loc[filt1])

#So lets apply this filtering on the real data such as student performance data set
#so i want a specific studnet who has score in all three subjects lets see if i can find someone like that 
genius = (df['math score'] == 90) & (df['reading score'] == 90) & (df['writing score'] == 90)
print(df.loc[genius])
#So basically there is not a single student who has scored 90 in all three subjects So now we will check for a studnet who has score atleast 90 in either one of the subjects 
semi_genius = (df['math score'] == 90) | (df['reading score'] == 90) | (df['writing score'] == 90)
print(df.loc[semi_genius])
#So there are many studnets who have scored atleast 90 in either of the subjects 
lunch_type = ['free/reduced']
print(df[df['lunch'].isin(lunch_type)])
#So suppose i want to filter some based on something which the users has exclusively so to do that i can use str contains 
degree_filt = df['parental level of education'].str.contains("bachelor's", na=False)
print(df.loc[degree_filt])
#So i am going to attempt to filter students based on everything i have filtered so far lets see
final_filt = (((df['math score'] == 90) | (df['reading score'] == 90) | (df['writing score'] == 90)) & (df['lunch'] == 'free/reduced') & (df['parental level of education'] == "bachelor's degree"))
print(df.loc[final_filt])
#So i successfully implemented the multiple parameters search 
