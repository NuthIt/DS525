# 1. python packages requirement

numpy 1.23.2
psycopg2 2.9.3
python-dateutil 2.8.2
pytz 2022.2.1
six 1.16.0


#  2.AWS : Redshift
## Cluster configuration
<h4>Cluster identifier</h4>

redshift-cluster-1

<h4>Node type</h4>
ra3.xlplus

<h4>Admin user name</h4>
awsuser

<h4>Admin user password</h4>
dummyPassword123

<h4>Associate IAM roles</h4>
LabRole

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1028051541816512582/52531.png)


# 3. AWS : S3

## Bucket Name
ds525project3temp1

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1028052400143073370/52532.png)

## Note

Bucket must be public bucket

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1028052400646402119/52533.png)

## Files
events_json_path.json
github_events_01.json

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1028052401032269906/52534.png)
# 4.ETL (ETL.ipynb)
<h4>Edit redshift address</h4>

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1028058632820105287/52539.png)

<h4>Edit file path (S3)</h4>

![alt text](https://cdn.discordapp.com/attachments/953573962519031848/1028052402491895868/52537.png)

# 5. Cleanup (Redshift + S3)
