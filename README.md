# Incubyte_Assessment

This code is implemented in python by connecting to MySQL database.

In this assessment, I have created a text file with the given data.

With the python's mysql connector, created the database "incubyte_customer_data" and then added the table "RECORD" to the database with the given descriptions.

And then with the help of python read the data in the text file and then inserted the records into the table.

Then with the query SELECT Country FROM RECORDS selected the countries that are present in the table.

After that with the query CREATE TABLE Table_%s AS (SELECT * FROM RECORDS WHERE Country = %s" %(country,country) created the tables for the country-wise data of the customers.
