# Pandas - Panel Data - Data Analysis Library - used extensively for EDA (Exploratory Data Analysis)
# The core objects are Series and Dataframes

# Import libraries
import pandas as pd

# To create a dataframe:
#   - using collection object(list)
#   - by loading a file


list1 = [[1, 'John', 1000], [2, 'Arun', 2000]]
list1


# create a df from a list
empDataFrameFromList = pd.DataFrame(list1)
empDataFrameFromList

empDataFrameFromList.columns

empDataFrameFromList = pd.DataFrame(
    list1, columns=['E_id', 'Emp_Name', 'Emp_Sal'])
empDataFrameFromList


# Create df by file from working directory
employeeDataFrame = pd.read_csv("employee.csv", names=['eid', 'ename', 'esal'])
employeeDataFrame

# Using path
employeeDataFrame = pd.read_csv(
    "C:/Users/91903/Desktop/Pandas/employee.csv", names=['eid', 'ename', 'esal'])
employeeDataFrame

# Giving less column names than we have
employeeDataFrame = pd.read_csv("employee.csv", names=['eid', 'ename', 'esal'])
employeeDataFrame


# Import csv with header
empWithHeaderDF = pd.read_csv("employeeWithHeaders.csv")
empWithHeaderDF

# Get info about df
empWithHeaderDF.info()
employeeDataFrame

# change one column name
employeeDataFrame.rename({'eid': 'employeeID'}, axis=1, inplace=True)
# axis is to specify that you are doing this for columns
# axis=0 - by rows

employeeDataFrame

employeeDataFrame.replace({'Rahul': 'Preda'})

# Load data from remote path
irisFromRemote = pd.read_csv(
    "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
irisFromRemote

irisFromRemote.head(10)  # print first five records
irisFromRemote.tail(10)  # print last five records

# Import data from url
url = 'https://www.basketball-reference.com/leagues/NBA_2015_totals.html'
BB_data = pd.read_html(url)

type(BB_data)

type(BB_data[0])

# Copy data from clipboard
BB_data = pd.read_clipboard()
BB_data

# Series - one column of the dataframe
empWithHeaderDF.columns

# Return the column esal
empWithHeaderDF.esal

empWithHeaderDF['esal']

type(empWithHeaderDF['esal'])

# Series operations
empWithHeaderDF

yearlySalary = empWithHeaderDF.esal*1.2
yearlySalary

type(yearlySalary)

# Add a new column to the df
empWithHeaderDF['YearlySalary'] = yearlySalary
empWithHeaderDF

empWithHeaderDF['NewSalary_v2'] = empWithHeaderDF.esal*1.3
empWithHeaderDF

# Updating an existing column
empWithHeaderDF['esal'] = empWithHeaderDF['esal']*1.5
empWithHeaderDF

del empWithHeaderDF['YearlySalary']
# the change it's permanent

empWithHeaderDF

# Drop
empWithHeaderDF.drop(['NewSalary_v2'], axis=1, inplace=True)
# axis=1 - column wise
# inplace=True - permanent change
empWithHeaderDF

deptList = ['HR', 'OPs', '', '', 'OPs', 'HR']
deptList

empWithHeaderDF['Department'] = deptList
empWithHeaderDF

# Use-case: I want to create a new column called UpdatedYearlySalary based on
# the following increment/hike conditions:
# If the salary is less than equal to 1500, then inc the sal by 10%
# If the salary is between 1501 and 10000, then inc the sal by 5%
# If the salary is between 10001 and 20000, then inc the sal by 2.5%
# If the salary is greater than 20000, then no increment


def incrementSalary(salary):
    if salary <= 1500:
        newSal = salary * 1.1
    elif salary <= 10000:
        newSal = salary * 1.05
    elif salary <= 20000:
        newSal = salary * 1.025
    else:
        newSal = salary
    return int(newSal)


# Apply a function to a column:
empWithHeaderDF['UpdatedYearlySalary'] = empWithHeaderDF['esal'].apply(
    incrementSalary)
empWithHeaderDF

# Store the dataframe into a file
empWithHeaderDF.to_csv('OutputFileJan.csv', index=None)

df = pd.read_csv('OutputFileJan.csv')
df

df.index = ['a', 'b', 'c', 'd', 'e', 'f']
df

# Subset functions
# loc - location
# iloc- index location
