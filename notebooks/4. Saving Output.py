
# coding: utf-8

# In[1]:

from IPython.display import Markdown
Markdown(filename="../INDEX.md")


# ***
# ###4a. Save to text files

# In[2]:

#native version
import csv
#load data
with open("../data/iris_with_header.csv", "r") as f:
    reader = csv.reader(f, delimiter=",", quotechar=None)
    column_header = next(reader)
    data = [row for row in reader]

#write data
with open("../data/iris_out.csv", "w") as f:
    writer = csv.writer(f, delimiter = ",", quotechar = None)
    writer.writerow(column_header)
    for d in data:
        writer.writerow(d)


# In[3]:

#pandas version
import pandas as pd

#load data
data = pd.read_csv("../data/iris_with_header.csv", header=0)

#write data
data.to_csv("../data/iris_out.csv", sep=",")


# ***
# ###4b. Save to database

# In[4]:

import pandas as pd
from sqlalchemy import create_engine, text

#create in memory database
engine = create_engine("sqlite:///:memory:")

#load data
data = pd.read_csv("../data/iris_with_header.csv", header=0)

#write to database
data.to_sql("tbl_iris", engine, index=False)

