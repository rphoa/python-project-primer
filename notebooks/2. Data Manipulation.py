
# coding: utf-8

# In[1]:

from IPython.display import Markdown
Markdown(filename="../INDEX.md")


# ***
# ## 2.a Selecting

# ####[pandas] Select single columns by column name or index

# In[2]:

import pandas as pd

data = pd.read_csv("../data/iris_with_header.csv", header=0)

#select by column name
sepal_length_by_column = data["sepal length (cm)"]

#select by index
sepal_length_by_index = data.iloc[:,0]

print ("Single column by column name: \t", sepal_length_by_column[:5].values.tolist())
print ("Single column by index: \t", sepal_length_by_index[:5].values.tolist())
print ()


# ####[pandas] Select multiple columns by column name or index

# In[3]:

#select by column name
sepal_length_by_column = data[["sepal length (cm)", "petal length (cm)"]]

#select by index
sepal_length_by_index = data.iloc[:, [0,2]]

#print first 5 rows of data set from column name and index - row version
print ("Multi column by column name - row version: \t", sepal_length_by_column[:5].values.tolist())
print ("Multi column by index - row version: \t\t", sepal_length_by_index[:5].values.tolist())
print ()

#print first 5 rows of data set from column name and index - column version (numpy style)
print ("Multi column by column name (1) - column version: \t", sepal_length_by_column[:5].values.T[0,:].tolist())
print ("Multi column by index name (1) - column version: \t", sepal_length_by_index[:5].values.T[0,:].tolist())
print ("Multi column by column name (2) - column version: \t", sepal_length_by_column[:5].values.T[1,:].tolist())
print ("Multi column by index name (2) - column version: \t", sepal_length_by_index[:5].values.T[1,:].tolist())


# ***
# ## 2.b Slicing

# In[4]:

#required imports
import pandas as pd

data = pd.read_csv("../data/iris_with_header.csv", header=0)

#select first 5 rows, all columns
print (data[:5].to_string())
print ()

#select first 10 rows of every 5th row
print (data[::5][:10].to_string())
print ()

#select third to tenth row
print (data[3:10].to_string())
print ()

#select fifth to tenth row and second to forth column by index
print (data.iloc[5:10, 2:4].to_string())
print ()

#select fifth to tenth row and second to forth column by column name
print (data.loc[5:10, "petal length (cm)":"petal width (cm)"].to_string())
print ()


# ***
# ## 2.c Filtering

# In[5]:

#required imports
import pandas as pd

data = pd.read_csv("../data/iris_with_header.csv", header=0)

#select only setosa type
print (data[data["type"] == "versicolor"][:5].to_string())
print ()

#select only versicolor type with sepal length more than 6.5cm 
print (data[(data["type"] == "versicolor") & (data["sepal length (cm)"] > 6.5)][:5].to_string())
print ()

#select setosa and versicolor type with sepal length more than 6.5cm 
print (data[(data["type"].isin(["setosa", "versicolor"])) & (data["sepal length (cm)"] > 5.5)][:5].to_string())
print ()


# ***
# ## 2.d Transformation

# In[6]:

#required imports
import pandas as pd

data = pd.read_csv("../data/iris_with_header.csv", header=0)

data["sepal area"] = data["sepal length (cm)"] * data["sepal width (cm)"]

def set_color(x):
    if (x == "setosa"):
        return "red"
    elif (x == "versicolor"):
        return "blue"
    elif (x == "virginica"):
        return "green"

data["color"] = data["type"].apply(set_color)

print (data[:5].to_string())
print ()


print (data.groupby("type").nth(0).to_string())
print ()

