import mysql.connector

'''creating a file
'''
# file=open('data/file1.txt','a')
# file.close()

''' writing the given sample data into the file
'''

# f = open("data/file1.txt", "a")
# f.write("|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active\n")
# f.write("|D|Alex|123457|20101012|20121013|MVD|Paul|SA|USA|06031987|A\n")
# f.write("|D|John|123458|20101012|20121013|MVD|Paul|TN|IND|06031987|A\n|D|Mathew|123459|20101012|20121013|MVD|Paul|WAS|PHIL|06031987|A\n")
# f.write("|D|Matt|12345|20101012|20121013|MVD|Paul|BOS|NYC|06031987|A\n|D|Jacob|1256|20101012|20121013|MVD|Paul|VIC|AU|06031987|A\n")
# f.close()


'''connecting the cursor
'''

cursor = connection.cursor()

'''creating the database
'''

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE incubyte_customer_data"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

'''connecting to the database
'''

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="incubyte_customer_data",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

'''creating the table RECORDS
'''

create_RECORDS_table_query = """
CREATE TABLE RECORDS(
    Customer_Name VARCHAR(255) PRIMARY KEY,
    Customer_ID VARCHAR(18) NOT NULL,
    Customer_Opendate DATE(8) NOT NULL,
    Last_Consulteddate DATE(8),
    Vaccination_Type CHAR(5),
    Doctor_Consulted CHAR(255),
    State CHAR(5),
    Country CHAR(5),
    Postcode INT(5),
    Date_of_Birth DATE(8),
    Active_Customer CHAR(1)
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_RECORDS_table_query)
    connection.commit()

'''insert records into the table
'''

file=open('data/file1.txt','r')
lines-file.readlines()
for line in lines[1:]:
    line=line.split("|")
    line=line[1:]
    line[-1]=line[-1][0]
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO RECORDS(Customer_Name,Customer_ID,Customer_Opendata,Last_Consulteddate,Vaccination_Type,Doctor_Consulted,State,Country,Postcode,Date_of_Birth,Active_Customer) 
                          VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s))
                          """,line)
        connection.commit()
'''selecting coutries from the table
'''

select_country_query="SELECT Country from RECORDS"
with connection.cursor() as cursor:
    cursor.execute(select_country_query)
    countries = cursor.fetchall()

'''creating seperate tables for the country wise data
'''

for country in countries:
    create_country_table_query="CREATE TABLE Table_%s AS (SELECT * FROM RECORDS WHERE Country = %s" %(country,country)
    with connection.cursor() as cursor:
        cursor.execute(create_country_table_query)
        connection.commit()
        