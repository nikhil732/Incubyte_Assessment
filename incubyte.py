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


# '''connecting the cursor
# '''

# cursor = connection.cursor()

'''creating the database
'''

from getpass import getpass
from mysql.connector import connect, Error

# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#     ) as connection:
#         print("Connected successfully")
#         create_db_query = "CREATE DATABASE incubyte_customer_database"
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
# except Error as e:
#     print(e)

# '''connecting to the database
# '''

# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#         database="incubyte's_customer_data",
#     ) as connection:
#         print(connection)
#         show_db_query="SHOW DATABASES"
#         with connection.cursor() as cursor:
#             cursor.execute(show_db_query)
#             for db in cursor:
#                 print(db)
# except Error as e:
#     print(e)


'''creating the table RECORDS
'''

create_RECORDS_table_query = """
CREATE TABLE RECORDS(
    Customer_Name VARCHAR(255) PRIMARY KEY,
    Customer_ID VARCHAR(18) NOT NULL,
    Customer_Opendate DATE NOT NULL,
    Last_Consulteddate DATE,
    Vaccination_Type CHAR(5),
    Doctor_Consulted CHAR(255),
    State CHAR(5),
    Country CHAR(5),
    Date_of_Birth DATE,
    Active_Customer CHAR(1)
)
"""

# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#         database="incubyte_customer_database",
#     ) as connection:
#         print(connection)
#         with connection.cursor() as cursor:
#             cursor.execute(create_RECORDS_table_query)
#             connection.commit()
# except Error as e:
#     print(e)


'''insert records into the table
'''

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="incubyte_customer_database",
    ) as connection:
        print(connection)
        file=open('data/file1.txt','r')
        lines=file.readlines()
        for line in lines[1:-1]:
            line=line.split("|")
            print(line)
            line=line[2:]
            y=line[-2][4:]
            m=line[-2][2:4]
            d=line[-2][0:2]
            line[-2]=y+m+d
            # print(line)
            # print(line[-1])
            line[-1]=line[-1][0]
            print(line)
            # with connection.cursor() as cursor:
            #     cursor.execute("""INSERT INTO RECORDS(Customer_Name,Customer_ID,Customer_Opendate,Last_Consulteddate,Vaccination_Type,Doctor_Consulted,State,Country,Date_of_Birth,Active_Customer) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",line)
            #     connection.commit()
        
        show_rows="SELECT * FROM RECORDS"
        with connection.cursor() as cursor:
            cursor.execute(show_rows)
            for row in cursor:
                print(row)

        select_country_query="SELECT Country FROM RECORDS"
        print(select_country_query)
        with connection.cursor() as cursor:
            cursor.execute(select_country_query)
            countries=cursor.fetchall()
        print(countries)

        for country in countries:
            print(country[0])
            s=str(country[0])
            create_country_table_query="CREATE TABLE Table_"+s+" AS (SELECT * FROM RECORDS WHERE Country = '"+s+"')"
            print(create_country_table_query)
            with connection.cursor() as cursor:
                cursor.execute(create_country_table_query)
                connection.commit()

        show_rows="SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(show_rows)
            for row in cursor:
                print(row)

        


except Error as e:
    print(e)
        
