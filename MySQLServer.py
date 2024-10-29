import mysql.connector

try: 
    mydb = mysql.connector.connect (
        host = "local host",
        user = "root",
        password = "Melchizedekforever29*",
    )

    mycursor = mydb.cursor()

    mycursor.execute ("CREATE DATABASE IF NOT EXISTS alx_book_store")


    print ("Database 'alx_book_store' created successfully")
    mydb.commit()

except mysql.connector.Error:
    raise "Failed to connect to Database"
mycursor.close()
mydb.close()