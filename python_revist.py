#sites referred is : https://www.dataquest.io/mission/2/if-statements-and-loops/
# assigning values to a (variable):
a=5
#print values
print(10)
#this will print the value 5 as a part of the output.
#printing a variable
print(variable_name)-- provided you store a value in that variable.

#types of variables are integer, string and float and float being more accurate and precise as it can store frcations.
#while assigning a string variable should be in double quotes(""):-)

#To check the type of a variable
type(variable_name) or type(10)--This will give the type as Integer. 

#To open a file we can use a Open function
open("File_name.csv","r")
#Where r is the read mode.

.read()-- this method Can be used to read the contents of a file into a variable.

List is a datatype
Python is zero indexing language
list can store any datatype aswell as mixed datatype.
["q",1,5.12]
or
[1,2,3] and so on.

And this can be then assigned to a variable.
example: a=[1,2,3]
Inorder to retrieve these values we can use the concept of indices.
0indices=1,1indices=2,2indices=3 in a list of [1,2,3]
a[0]=1 and a[1]=2 and so on.
We too can manipulate the values.
eg: a[0]+a[1]=1+2=3

string are also objects.
We can use .split method

logically we can open a file and read the data in a variable and then spilt it and store it in another variable.
.split takes character as a input and then turns a string into a list of string.

Loops:

for loop works in the order of the indexes.
say there is a varibale a with list data type.
then for i in a:
print(i) where i is a loop variable.

There can be multiple lines of for loop.

example:

the_list = [3,5,8,10,15,17,19]
sum = 0
for q in the_list:
    double_value = q * 3
    sum = sum + double_value
print(sum)

list inside a list.
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

# Pulls out the first element in the first list.
a = lolists[0][0]

# Pulls out the third element in the second list.
b = lolists[1][2]

# We can also directly do math with expressions.
c = lolists[0][2] + 10

# Any expression in python can be manipulated without first assigning it to a variable.
d = 10


Set e equal to d times the first element in the third inner list of lolists.
e = lolists[2][0]*d

Use a for loop to print the first element of each inner list.
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

for inner_list in lolists:
    # This will loop through and print each inner list, starting from the one at index 0.
    a=inner_list[0]
    print(a)
	
	
Appending

we can use .append method
basic example
c=[20,30]
>>> a=[]
>>> for i in c:
	a.append(i)
	print(a)
	
	
splitting a .csv file into list.
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
	
		output: ['1', '10', '15', '20']
		
		
#counting the number of columns#
say there is a list :
l=[[1,2,3],[3,4,5],[5,6,7]]
>>> first_row=l[0]
>>> count=0
>>> for column in first_row:
	count=count+1
	print(count)

example:

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
first_row = full_data[0]
count = 0
for column in first_row:
    count = count + 1	
	
******boolean*******
boolean checks true or false.



print("Andre the Giant" == "Short")
False
>>> 
KeyboardInterrupt
>>> print("Andre the Giant" == "Andre the Giant")
True
>>> print(type(True))
<class 'bool'>
>>> print(type(False))
<class 'bool'>

#for loop or if statement (:) means there is a indented statement below it which must be executed:
#indented means : 4 spaces to be maintained after the if or for statement header from the compound statement.

#if statement with variables that evaluates to true:
#example:
c = 15
if c==15:
    print("Much success!")
	# if statements with for loops.
#We can also use if statements inside for loops (or vice versa). 
#When this happens, we need to indent everything in the inner block another 4 spaces.
	
example:
the_list = [5, 10, 15, 20]
>>> for i in the_list:
	if i>5:
		print(i)

smallest_item = 1000
a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]
for item in a:
    if item < smallest_item:
        smallest_item = item		

		
#converting types
#we can convert between different datatypes.
#int() will work in this regard.
example:
c='10'
>>> c_int=int(c)
>>> print(c_int)
10

a = ['10', '15', '20', '35']
new_a = []
for item in a:
    item_list=int(item)
    new_a.append(item_list)
    print(new_a)


full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)	
	
		
lowest_crime_rate = 10000
for row in full_data:
    crime_rate = row[1]
    if crime_rate < lowest_crime_rate:
        lowest_crime_rate = crime_rate
		
		
		a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]
for item in a:
    if item == 78:
        print("Yes")
		
		
		lolist = [[1,5,7],[10,8,9],[7,10,11]]
>>> value=0
>>> for item in lolist:
	if item[0]==7:
		value= item[1]
		print(value)

#finding the lowest crime rate city		
		city = ""
for item in full_data:
    if item[1]==130:
        city=item[0]
        print(city)
		
		

#parsing File_name

weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)
#finding the second column
weather_column = []
for row in weather_data:
    weather_column.append(row[1])
	
	#slicing a list
	
	slice_me = [7,6,4,5,6]
slice1=slice_me[2:4]
slice2=slice_me[1:2]
slice3=slice_me[3:5]

#where slice_me[2:4] means from index 2 to 3 excluding 4
# if you want to skip the header just slice starting with 10

#dictionary

dictionary_two ={} 
dictionary_two["test"]=5 where test is called key and assigned a value=5
dictionary_two[10]="hello"

# indexing a dictionary
a = dictionary[10] 
it will assign a value for KEY 10 to a

# defining a dictionary with values
c={7:"raven",8:"goose",9:"duck"}
d={"morning":9,"afternoon":14,"evening":19,"night":23}
# where first value is the key and the second is its corresponding values

# the in clause can be used to check for values in list.

list2 = [8, 5.6, 70, 800]
c= 9 in list2
d= 8 in list2
e=-1 in list2
here we are assigning the values to a variable.

the same can be checked for dictionary too..


#else statement

# to find the counts
us_presidents = ["Adams", "Bush", "Clinton", "Obama", "Harrison", "Taft", "Bush", "Adams", "Wilson", "Roosevelt", "Roosevelt"]

us_president_counts = {}
for president in us_presidents:
    if president in us_president_counts:
        us_president_counts[president] = us_president_counts[president] + 1
    else:
        us_president_counts[president] = 1

		

		#functions and debugging.
		
# reading a file.

#f=open("file_name","r")
#and then if read a file and store it in a variable read()


#Tokenizing the file
#split the file into individual words.

tokenized_story = story.split(" ")
if splitting the file based on white space or space character.

#replacing punctuation:
#code below.
no_punctuation_tokens = []
for token in tokenized_story:
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    no_punctuation_tokens.append(token)
	#here replace function is used to replace with white space.
	
	#converting into lower case.
	
	lowercase_tokens = []
for p in no_punctuation_tokens:
    p=p.lower()
    lowercase_tokens.append(p)

		
#making a simple function.

def convert(degrees):
    return (degrees - 32)/1.8
celsius_100 = convert(100)
celsius_150 = convert(150)
		
 	
#Working with functions:
lowercase_me = "I wish I was in ALL lowercase"
def lowercase(text):
    return text.lower()

lowercased_string=lowercase(lowercase_me)	


#multiline functions:
#in case of complex multiline functions we should define a variable inside a function else it won't be accessible.
no_punctuation_tokens = []
def remove_punctuation(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    return token

for token in tokenized_story:
    token = remove_punctuation(token)
    no_punctuation_tokens.append(token)	
	
----------


normalized_tokens = []---make sure the list variable is declared before.
def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token
for token in tokenized_story:
     token=normalize(token)
     normalized_tokens.append(token)
	 
	 
	 #multiple argument functions
	 
	 def mul(x,y,z):
    return (x*y*z)
    
a=mul(10,3,5)
print(a)
b=mul(20,-1,3)
print(b)


#Reading in and normalizing the dictionary

def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

normalized_dictionary_tokens = []
f = open("dictionary.txt", 'r')
tokens = f.read().split(" ")
for token in tokens:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)
	
	
#finding words that aren't correctly spelled.	
potential_misspellings = []
correctly_spelled = []
for token in normalized_story_tokens:
    if token in normalized_dictionary_tokens:
        correctly_spelled.append(token)
    else:
        potential_misspellings.append(token)	


#here data is in normalized_story_tokens
# and dictionary is in 	normalized_dictionary_tokens and we compare and check if the data is correct.

# some useful sites:
https://www.quora.com/How-do-I-learn-python-10

#working with pandas.

#importing panda library.
import pandas
# read_csv() is the function (or feature) from pandas we want to use to load the file into memory
housing_2013 = pandas.read_csv("Hud_2013.csv")
# .head(num_of_rows) is a method that displays the first few (num_of_rows) rows, not counting column headers
housing_2013.head(5)

num_columns= len(housing_2013.columns)
print("Number of columns:  " + str(num_columns))

#Formatting Data

Of the 6 columns, let's filter the dataset down to just 3 columns that looks especially interesting: AGE1, TOTSAL, and FMR. In Excel, this would mean making a new worksheet tab and copying and pasting manually the columns we want or hiding the columns we don't want. Both methods add unnecessary complexity and more things to keep track of...let's see how Pandas manages this.
# the bracket notation [ ] is how we specify the the list of columns we want to select
filtered_housing_2013 = housing_2013[[ 'AGE1', 'FMR','TOTSAL' ]]
filtered_housing_2013


#plotting histogram

filtered_housing_2013.hist(column='FMR', bins=20)

# Introduction to Conditional Filtering
this means that we can filter the rows that can meet the certain criteria's.

filtered_housing_2013['AGE1'] > 0
our filter should evaluate to True whenever the AGE1 value for a row is greater than 0, and False whenever it's less than 0. We can express that criteria in Python:

#example
evaluted_row_numbers = []
evaluated_row_numbers = filtered_housing_2013['AGE1'] > 0
print(evaluated_row_numbers)

filtered_housing_2013 = housing_2013[[ 'AGE1', 'BURDEN', 'FMR', 'FMTBEDRMS', 'FMTBUILT', 'TOTSAL' ]]

cleaned_housing_2013 = filtered_housing_2013[evaluated_row_numbers]





#cleaned_housing_2013 = filtered_housing_2013[evaluated_row_numbers]

# Preview the first 10 rows
cleaned_housing_2013.head(10)


#Calculating the Difference in DataFrames

filtered_count = len(filtered_housing_2013)
print(filtered_count)
cleaned_count = len(cleaned_housing_2013)
print(filtered_count - cleaned_count)



13: Verifying the Cleanup

4438 closely matches the initial guess we had of 4500 while eyeballing the histogram. To verify the cleanup further, let's write and apply a filter that verifies that there are no rows left with a negative value for AGE1. Our filter criteria needs to be the opposite of the one we wrote earlier, since we want the filter to evaluate to True when AGE1 is negative and False when positive. 
Then, we'll evaluate the filter on cleaned_housing_2013 and assign the resulting DataFrame to negative_housing_2013. 
Finally, let's print the length of the resulting DataFrame using len().
#example
negative_row_numbers = cleaned_housing_2013['AGE1'] < 0
negative_housing_2013 = cleaned_housing_2013[negative_row_numbers]
print(len(negative_housing_2013))



#reading the dataset into the dataframe objects/variables:

import pandas
housing_2007=pandas.read_csv("Hud_2007.csv")
housing_2005=pandas.read_csv("Hud_2005.csv")


data_frames_list = []
# Adding a year column to each DataFrame, so we can easily keep track easier later
housing_2005['year'] = '2005'
housing_2007['year'] = '2007'# .append() adds the specified object to the end of the list
data_frames_list.append(housing_2005)
data_frames_list.append(housing_2007)

# the list now contains 2 objects, the respective DataFrames for 2005 and 2007
print(len(data_frames_list))


#Column Filtering

columns = []
filtered_housing_2007 = []
columns=['AGE1', 'FMR', 'TOTSAL', 'year']
filtered_housing_2007=housing_2007[columns]



#Functions:

def filter_columns(data_frames_list):
    # Final list we want to return, starts out empty
    new_df_list = list()

    # Use a "for" loop to iterate through each DataFrame. For every DataFrame ("df") in the list: data_frames_list
    for df in data_frames_list:
        # Use a list to specify the columns we want
        columns = ['AGE1', 'FMR', 'TOTSAL', 'year']
        # Filter the current dataframe we are iterating through to have only the columns we want
        filtered_df = df[columns]
        # Add the filtered dataframe object to the empty list we created in the beginning on the function
        new_df_list.append(filtered_df)
    # Functions require a "return" value, which is the result of what happened inside
    return new_df_list

filtered_data_frames_list = filter_columns(data_frames_list)

 
Another abstraction we could implement would be to modify the function 
and specify the columns we want filtered every time by adding it 
as an input to the function (alongside data_frames_list). 
This way, 
instead of always using a specific set of columns within the function, 
the user can now specify in the input which columns they prefer to filter their DataFrames.

#Column Filtering Verification
for df in filtered_data_frames_list:
    # print that DataFrame's columns
    print(df.columns)


#Multiple Dataset Analysis
for df in filtered_data_frames_list:
    # Get the year
    year = df['year'][0]
    # Only the rows with negative age values
    negative_age_count = df['AGE1'] < 0
    # Custom print formatting
    print( str(year) + " - " + str(len( negative_age_count ) ) + " rows")
	
	
	
Output

2005 - 46853 rows
2007 - 42729 rows

#data cleansing

def clean_rows(filtered_data_frames_list):
    # Create a new empty list
    cleaned_list = list()
    
    for df in filtered_data_frames_list:
        cleaned_df = df[ df ['AGE1'] > 0 ] 
        cleaned_list.append(cleaned_df)
    return cleaned_list

cleaned_data_frames_list = clean_rows(filtered_data_frames_list)

https://www.dataquest.io/mission/2/if-statements-and-loops/

#data verification:

def verify_cleanup(data_frames_list):
    # Use a count to keep track of negative rows found
    negative_rows_count = 0
    
    for df in data_frames_list:
        # Add the number of negative rows found to negative_rows_count
        v_count=len(df[df['AGE1']<0])
        return v_count
        #negative_rows_count =negative_rows_count + v_count
    #return negative_rows_count

verification_count = verify_cleanup(cleaned_data_frames_list)


#https://www.dataquest.io/mission/99/plotting-the-rise-of-computers/


#https://www.techopedia.com/2/31300/technology-trends/big-data/how-can-we-handle-the-internet-of-things-generated-data-ethically


Reading the data:

import pandas
apple_stock=pandas.read_csv("AAPL_historical_stock.csv")

microsoft_stock = pandas.read_csv("MSFT_historical_stock.csv")

#First 10 records.

microsoft_stock.head(10)



#Columns

# Using pandas.to_datetime() to convert both datasets' Date columns
microsoft_stock['Date'] = pandas.to_datetime(microsoft_stock['Date'])
apple_stock['Date'] = pandas.to_datetime(apple_stock['Date'])

# Use .dtypes and filter to info on ['Date'] column
microsoft_date_datatype = microsoft_stock.dtypes['Date']
apple_date_datatype = apple_stock.dtypes['Date']
# here .dtypes are used to get the datatype of the column 'date' 

print("Microsoft Date Datatype:  " + str(microsoft_date_datatype))
print("Apple Date Datatype:  " + str(apple_date_datatype))


#plotting something like trading volume:


# Here we use "color=___" to specify color
plt.plot(microsoft_stock['Date'], microsoft_stock['Volume'], color="blue")
plt.title("Microsoft: Trading Volume")
plt.show()

# Repeat for Apple!
plt.plot(apple_stock['Date'], apple_stock['Volume'], color="green")
plt.title("Apple: Trading Volume")
plt.show()






output---


Microsoft Date Datatype:  datetime64[ns]
Apple Date Datatype:  datetime64[ns]



#plotting columns

# Importing the pyplot sub-library from matplotlib library and referring to it as "plt"
import matplotlib.pyplot as plt

# plt.plot() tells Python to create a new plot and what the X (first argument) and Y (second argument) axes are
plt.plot(microsoft_stock['Date'], microsoft_stock['Close'])
# plt.title() details how we want the current plot to be titled
plt.title("Microsoft: Historical Closing Stock Price Until Jul 1, 2015")
# plt.show() reveals the plot we've been specifying
plt.show()

# New plot, repeat for Apple as we did with Microsoft
plt.plot(apple_stock['Date'], apple_stock['Close'])
plt.title("Apple: Historical Closing Stock Price Until Jul 1, 2015")
plt.show()






import matplotlib.dates as mdates

# Filter dates to be greater than Jan 1, 1999 but less than Jan 1, 2002
microsoft_bubble = microsoft_stock[(microsoft_stock['Date'] > '1999-01-01') & (microsoft_stock['Date'] < '2002-01-01')]
plt.plot(microsoft_bubble['Date'], microsoft_bubble['Volume'])

# .gcf() - returns the current figure (or plot)
fig_msft = plt.gcf()
# autofmt_xdate():  auto-format X-axis to look nice
plt.gcf().autofmt_xdate()
plt.title("Microsoft Stock: Dot Com Crash")
plt.show()

# Repeat for Apple!
apple_bubble = apple_stock[(apple_stock['Date'] > '1999-01-01') & (apple_stock['Date'] < '2002-01-01')]
plt.plot(apple_bubble['Date'], apple_bubble['Volume'])

# .gcf() - returns the current figure (or plot)
fig_aapl = plt.gcf()
# autofmt_xdate():  auto-format X-axis to look nice
fig_aapl.autofmt_xdate()
plt.title("Apple Stock: Dot Com Crash")
plt.show()



#https://www.dataquest.io/mission/100/cleaning-data/
