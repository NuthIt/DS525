import boto3
import pandas as pd
import numpy as np


# Replace ACCESS_KEY_ID and SECRET_ACCESS_KEY with your own values
s3 = boto3.client('s3'
                  , aws_access_key_id='XXXXX'
                  ,aws_secret_access_key='XXXXX'
                  ,aws_session_token='XXXXX')

s3.download_file('thelabbucketswuproject2', 'datafile.csv', 'datafile.csv')

df = pd.read_csv('datafile.csv')

df['id'] = pd.to_numeric(df['id'], downcast='integer')
df['Year'] = pd.to_numeric(df['Year'], downcast='integer')
df['Avg_hrs_per_day_sleeping'] = pd.to_numeric(df['Avg_hrs_per_day_sleeping'], downcast='float')
df['Standard_Error'] = pd.to_numeric(df['Standard_Error'], downcast='float')


df['Period'] = df['Period'].apply(str)
df['Type_of_Days'] = df['Type_of_Days'].apply(str)
df['Age_Group'] = df['Age_Group'].apply(str)
df['Activity'] = df['Activity'].apply(str)
df['Sex'] = df['Sex'].apply(str)


#--------------------------------------------------------------------------------------


import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="XXXXX",
    port=5439,
    user="XXXXX",
    password="XXXXX",
    dbname="XXXXX"
)

# Create a cursor
cur = conn.cursor()

# Use a TRY/CATCH block to handle the error that occurs if the table does not exist
try:
    # Execute the DROP TABLE statement
    cur.execute("DROP TABLE contents")
    # If the DROP TABLE statement succeeds, commit the changes to the database
    conn.commit()
except psycopg2.errors.UndefinedTable:
    # If the table does not exist, do nothing
    pass

# Close the cursor and connection
cur.close()
conn.close()


#--------------------------------------------------------------------------------------


import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="XXXXX",
    port=5439,
    user="XXXXX",
    password="XXXXX",
    dbname="XXXXX"
)

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE contents (id INTEGER PRIMARY KEY, Year INTEGER, Period VARCHAR(50), Avg_hrs_per_day_sleeping FLOAT, Standard_Error FLOAT, Type_of_Days VARCHAR(50), Age_Group VARCHAR(50), Activity VARCHAR(50), Sex VARCHAR(50))")

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

#--------------------------------------------------------------------------------------

import psycopg2

# Connect to the Redshift cluster
conn = psycopg2.connect(
    host="XXXXX",
    port=5439,
    user="XXXXX",
    password="XXXXX",
    dbname="XXXXX"
)

# Create a cursor
cur = conn.cursor()

# Load the data from the Pandas dataframe into Redshift
loopcount = 0
for index, row in df.iterrows():
    if loopcount % 100 ==0 :
        print (loopcount)
    values = (int(df['id'][loopcount]),
              int(df['Year'][loopcount]),
              df['Period'][loopcount],
              float(df['Avg_hrs_per_day_sleeping'][loopcount]),
              float(df['Standard_Error'][loopcount]),
              df['Type_of_Days'][loopcount],
              df['Age_Group'][loopcount],
              df['Activity'][loopcount],
              df['Sex'][loopcount])
    cur.execute("INSERT INTO contents (id, Year, Period,Avg_hrs_per_day_sleeping,Standard_Error,Type_of_Days,Age_Group,Activity,Sex) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);", (int(df['id'][loopcount]),
              int(df['Year'][loopcount]),
              df['Period'][loopcount],
              float(df['Avg_hrs_per_day_sleeping'][loopcount]),
              float(df['Standard_Error'][loopcount]),
              df['Type_of_Days'][loopcount],
              df['Age_Group'][loopcount],
              df['Activity'][loopcount],
              df['Sex'][loopcount]))
    loopcount += 1
# Commit the transaction
conn.commit()
del loopcount
# Close the cursor and connection
cur.close()
conn.close()