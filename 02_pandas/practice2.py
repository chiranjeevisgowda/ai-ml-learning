import pandas as pd
people = {
    'name' : ['Chiru', 'Priya', 'Prema'],
    'last' : ['Gowda', 'gowda', 'CG'],
    'email' : ['chiru@gmail.com', 'priya@gmail.com', 'prema@gmail.com']
}

# df1 = pd.DataFrame(people)
# # # print(df.set_index('email'))
# # filt = (df['last'] == 'Gowda') | (df['name'] == 'Chiru')
# # print(df.loc[filt, 'email'])

# # df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/netflix_titles.csv')
# # pd.set_option('display.max_columns', 85)
# # # pd.set_option('display.max_rows', None)
# # # release_year = (df['release_year'] == 2020)
# # # print(df.loc[release_year, ['title' , 'country']])
# # countries = ('United States', 'India')
# # filt = df['country'].isin(countries)
# # print(df.loc[filt, 'country'])


# #So basically we can set custome indexs for better access of the data so to do that \ 
# #Inplace specifies that the email is set as the main index for the entire data whenever we print the data 
# #it is useful for searching and other purpose using loc
# df1.set_index('email', inplace=True)
# # print(df1)

# #For example if i want to search the other deatils of the person with the index we have specified we can just input the index value to get the output 
# print(df1.loc['chiru@gmail.com'])
# #If we jsut want the last name or any other specific column value of the person we could just input that also 
# print(df1.loc['chiru@gmail.com', 'last'])
# #If we have already set the index then we cannot use the traditional index value such as 0 and n numbers to access the value to do that we can stil ues iloc 
# print(df1.iloc[0, 0])
# #So if we want to have the index to be normal again no custom index then we can jsut use the reset index method to do so 
# df1.reset_index(inplace=True)
# #so if we use the custom index value after we reset the custom index then we get an error 
# # try:
# #     print(df1.loc['chiru@gmail.com'])
# # except KeyError:
# #     print("Custom index not valid")
# #So we can even set custom indexs at the start of the program where we define the variable to do so we can use index_col 
# df = pd.read_csv('/Users/chiru/Code Playground/Python/ai-ml-learning/02_pandas/Data/StudentsPerformance.csv', index_col='race/ethnicity')
# print(df.loc['group A'])
# #So as for the real world example given by Corey Schafer is when we the schema dataset for the data set if we want to know what the column actually
# #represents instead of remembering the index value of the column we can jsut set the column as the main index and just type the name of the column which we want to get the deatils off


# #So we can also use a method which is used to sort the index which is sort_index as simple and if we want the index to be in descending value we input the value ascending = False
# print(df.sort_index())
# print(df.sort_index(ascending=False))
# #So one more thing inplcae is something which we can use on a regualr basis to tell the system that it should be permanent until i change it myself


# #So now we start with the data FILTERING how to use logical operators and others on the data to get the value more properly 
# #So if we jsut use this the we get the output in the boolean format if we want the actual columns of the condition we can either assign the value to a variabale for example
# filt = df1['last'] == 'Gowda'
# print(df1['last'] == 'Gowda')
# #Then call that variable 
# print(df1[filt])
# #Else we can just directly input it when printing the value instead of creating a separate variable for it 
# print(df1[df1['last'] == 'Gowda'])
# #In pandas as I mentioned we can use logical or and logical and for comparison and cleaning data for example 
# #So if the value is not present then we the no error instead we get that the datafram is empty and it gives out the colums and index[]
# filt1 = (df1['last'] == 'Gowda') & (df1['name'] == '')
# print(df1.loc[filt1])

# #So lets apply this filtering on the real data such as student performance data set
# #so i want a specific studnet who has score in all three subjects lets see if i can find someone like that 
# genius = (df['math score'] == 90) & (df['reading score'] == 90) & (df['writing score'] == 90)
# print(df.loc[genius])
# #So basically there is not a single student who has scored 90 in all three subjects So now we will check for a studnet who has score atleast 90 in either one of the subjects 
# semi_genius = (df['math score'] == 90) | (df['reading score'] == 90) | (df['writing score'] == 90)
# print(df.loc[semi_genius])
# #So there are many studnets who have scored atleast 90 in either of the subjects 
# lunch_type = ['free/reduced']
# print(df[df['lunch'].isin(lunch_type)])
# #So suppose i want to filter some based on something which the users has exclusively so to do that i can use str contains 
# degree_filt = df['parental level of education'].str.contains("bachelor's", na=False)
# print(df.loc[degree_filt])
# #So i am going to attempt to filter students based on everything i have filtered so far lets see
# final_filt = (((df['math score'] == 90) | (df['reading score'] == 90) | (df['writing score'] == 90)) & (df['lunch'] == 'free/reduced') & (df['parental level of education'] == "bachelor's degree"))
# print(df.loc[final_filt])
# #So i successfully implemented the multiple parameters search 


#29/08/1016

df = pd.DataFrame(people)
#So to type out the columns of a dataframe we use .columns to get all the colums in a data
print(df.columns)
#So the new thing i got to know that is that we can manipulate the columns name however we want by using simple functions such as
#So to do that first we need to assign the value of the colums to a variable so that would be easier 
df.columns = ['first name', 'last_name', 'email']
df.columns = [x.lower() for x in df.columns]
#So if we want to like change the name or how the column is given so that everything is uniform so that it will be easier to use those column name we can change specifics we want 
df.columns = df.columns.str.replace(' ', '_')
#So if i am going to use df.email or anything similar if the column name is like first space name then i cant get it to give output since it would be invalid syntax
#So next thing if i want to cahnge the name of a particular column or a list of colums of my choice i could just give a dict of column which i want to cahnge
df.rename(columns={'first_name' : 'first', 'last_name' : 'last'}, inplace=True)
#And we need to use inplace to gurantee that it is set for the entire dataframe not just a single time this is same as set index 
#So now i am learning about changing values in the data so to do that i can use loc or iloc to me loc is more preferred lets see an example
df.loc[0] = ['Chiranjeevi S Gowda', 'Chiru', 'Chiru123@gmail.com']
#But this method is not preferred since if i want to change the value of a data with ex 85 columns i cant exactly type in all the 85 values 
#So we locate the column values which we want to change same as looking for the column values using the loc 
df.loc[0, 'first'] = ["Chiranjeevi"]
#Another method which we can use is at feature 
df.at[0, 'first'] = 'Chiru'
df.at[0, 'last'] = 'Gowda'
#Suppose i have filter and i want to change the value of that filter
filt = (df['email']) == 'Chiru123@gmail.com'
df.loc[filt, 'email'] = 'chiru@gmail.com' 
#Suppose i want to change the value of the entire column to upper or lower case so that it would be uniform in this example i would do uppercase for all the main sicne i already have all of them in lower case
df['email'] = df['email'].str.upper()
#Now i am going to learn about apply, map, replace lets see and document it 
#First i found a cool way of using apply function lets go with the basic till the end 
# print(df.apply(len)) #This one is to get the len of the overall length if i want the lenght of a particular column we could simply do 
# print(df['email'].apply(len))
#So if we want to use the len function on suppose the entire columns not the default rows
df.apply(len, axis='columns')
#Next we could use custom function too in the apply function example function
def update_email(email):
    return email.lower()
print(df['email'].apply(update_email))
#Actually he introduced about lamda function but didnt got in deep and I just applied the same which he did 
print(df['email'].apply(lambda x:x.upper()))
#what i got to know is lamda is a anyonomus function and the x defines the input it receives and x.upper indicates that the input should be converted to upper case
#Next i got to know is apply method works on just a series of data whereas applymap is applied on the entire dataframe rather than a series example # Got into a little confusion when applymap was not working and i got to know that the newer versions just use the map method instead of applymap
print(df.map(len))
#another example for using map is using it on a entire dataframe rather than series #according to what i have written i think my entire data frame will be converted to upper case lets see what happens 
print(df.map(lambda x:x.upper())) #So the conclusion i have reached until now is that map is used to manipulate the entire dataframe rather than a series and apply is used to modify single series or list of series
#So now we are gonna use replace method when we want to replace a series with the values we want then we can use the replace method ex
print(df['first'].replace({'Chiru' : 'Chiranjeevi', 'Prema' : 'Premi'}))
#if we want to manipulate the entire data not just the current output then we can assign the same to df['first'] = the code above 

#NEXT VIDEO
#So first i got to know how i can combine two columns into one cloumn and we will try our own thing which makes it learning 
print(df['first'] + " " + df['last']) # so suppose i want to make this get applied to main dataset then i can just give a new name and then make it to the main dataset
df['name'] = (df['first'] + " " + df['last'])
#So now the little twist i want to add of my own is i want to check if i can change the main index of the data set to name instead of the default index number
# df = df.set_index('name') #With the output i received i could confirm that yes we could do that 
#So since i have combined the first and the last so now i have no need of them then i can just use drop to remove those columns and if i am satisfied with the result then i can just use inplace to make it permanent
df.drop(columns=['first', 'last'], inplace=True)
#So since we have comined both the first and the last but suppose in a real data set there is a column which is already combined and we want to separate them or split into different columns we could just do
df['name'].str.split(' ', expand=True)
df[['first', 'last']] = df['name'].str.split(' ', expand=True) #One thing i noticed since we made the name as the main index we were not able to perform this action on the datframe since name was the main index
#So he inroduced a method append and we could jsut append values to the existing dataframe and the value we dont insert will be left nan but before we do that we need to confirm True for ignore_index
#Oooo no got to know one more thing we cant simply use append now it is also removed from the moder python I think the newer version is a bit more time consuming than the older append version but also i want to try a simple thing apart from append 
# print(df.map({'first' : 'chiran'})) #Wanted to experiment with map if it worked as append but no it doesnt 
#So if we want to drop any columns we could just use drop
df.drop(index=2)
#We can even use conditional to drop the rows such as we used filt previously 
print(df)
