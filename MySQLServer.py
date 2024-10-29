import mysql.connector

try: 
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "your_username",
        password = "your_password",
    )

    mycursor = mydb.cursor()

    mycursor.execute ("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print ("Database 'alx_book_store' created successfully")
    mydb.commit()

except mysql.connector.Error:
    raise "Failed to connect to Database"

finally:
    if mycursor:
        mycursor.close()
