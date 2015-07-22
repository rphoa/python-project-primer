
# coding: utf-8

# In[1]:

from IPython.display import Markdown
Markdown(filename="../INDEX.md")


# ***
# ##1a. Load data from text file *without* column headers

# In[2]:

#native version
import csv

#define file path and line separator
with open("../data/iris_without_header.csv") as f:
    #define delimter and quote character
    reader = csv.reader(f, delimiter=",", quotechar=None)
    #loop thorugh file and append data to list
    data = [row for row in reader]

#print first 5 rows of data set
for x in data[:5]: print (x)


# In[3]:

#pandas version
import pandas as pd

#manually set column headers or read from somewhere
column_header = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "type"]

#read csv file into dataframe, set header = None if you do not wish to define any column headers
data = pd.read_csv("../data/iris_without_header.csv", names=column_header)

#print first 5 rows of data set
for x in data[:5].values.tolist(): print (x)


# ***
# ##1b. Load data from text file *with* column headers

# In[4]:

#native version
import csv

#define file path and line separator
with open("../data/iris_with_header.csv") as f:
    #define delimter and quote character
    reader = csv.reader(f, delimiter=",", quotechar=None)
    column_header = next(reader)
    #loop thorugh file and append data to list
    data = [row for row in reader]

#print first 5 rows of data set
for x in data[:5]: print (x)


# In[5]:

#pandas version
import pandas as pd

#header indicates which line is the column header located, usually it is the first line. this is based on 0 based indexing.
data = pd.read_csv("../data/iris_with_header.csv", header=0)

#print first 5 rows of data set
for x in data[:5].values.tolist(): print (x)


# ***
# ##1c. Load data from database

# In[6]:

import pandas as pd
from sqlalchemy import create_engine, text

#create in memory database
engine = create_engine("sqlite:///:memory:")
#load data
data = pd.read_csv("../data/iris_with_header.csv", header=0)
#write to database
data.to_sql("tbl_iris", engine, index=False)

#query database
query = text("SELECT * FROM tbl_iris where type = :type").bindparams(type="setosa")
result = pd.read_sql_query(query, engine)

#print first 5 rows of results
for x in result[:5].values.tolist(): print (x)

