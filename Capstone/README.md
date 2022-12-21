# ETL Documaent
## Packages Reqirements
Python3
numpy
pandas
boto3
psycopg2
## S3
![enter image description here](https://media.discordapp.net/attachments/953573962519031848/1054981465202499614/S3_pandas.png?width=1058&height=578)

ในส่วนของ s3 นั้นจะดึงไฟล์จาก s3 และดาวดหลดที่ตัวเครื่อง (หรือ EC2) และอ่านไฟล์ดดย pandas และ convert ประเภทข้อมูลให้พร้อมกับการใส่ใน Redshift
## Redshift Drop Table
![enter image description here](https://cdn.discordapp.com/attachments/953573962519031848/1054981480239071382/REDSHIFT1.png)
ในการเขียนการ drop table นั้นไม่สามารถใช้งานเงื่อนไข IF EXIST ได้จึงต้องใช้งาน try / catch แทน
## Redshift Create Table
![enter image description here](https://cdn.discordapp.com/attachments/953573962519031848/1054981491496587346/REDSHIFT2.png)
การสร้างข้อมูลนั้นภายใน code ได้ออกแบบข้อมูลประเภทข้อมูลดังนี้

id INTEGER PRIMARY KEY
Year INTEGER
Period VARCHAR(50)
Avg_hrs_per_day_sleeping FLOAT
Standard_Error FLOAT
Type_of_Days VARCHAR(50)
Age_Group VARCHAR(50)
Activity VARCHAR(50)
Sex VARCHAR(50)
## Redshift Insert Table
![enter image description here](https://cdn.discordapp.com/attachments/953573962519031848/1054981500866658324/REDSHIFT3.png)
การ insert ข้อมูลนั้นจะเป็นการใช้งาน loop เพื่อการ insert ทีละบรรทัดใน dataframe เมื่อครบแล้วจึง commit
## .sh File
![enter image description here](https://cdn.discordapp.com/attachments/953573962519031848/1054981520588296254/SHFILE.png)
ไฟล์ .sh นั้น เป็นชุดรวมคำสั่งการติดตั้ง package ที่จำเป็นได้แก่
Python3
Numpy
pandas
boto3
psycpog2

คำสั่ง crontab โดยการสั่งให้ python ทำงานในทุก 15 นาที

Reboot เครื่องเมื่อทุกอย่างเสร็จสิ้น

## Dashbaord
![enter image description here](https://cdn.discordapp.com/attachments/953573962519031848/1054986072859344916/6.png)