import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Pass@123',
        auth_plugin='mysql_native_password',  # Specify the authentication plugin
        database = 'united'
    )
    mycursor = conn.cursor()
    print("Connection Established")
except Exception as e:
    print("Error:", e)

# create database on DB Server
#
# mycursor.execute("CREATE DATABASE UNITED")
# conn.commit()

# Create Table
# airport -> airport_id | code | name
# mycursor.execute(
#     """
#     CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
#     )
#     """
# )
# conn.commit()

# Insert data to the table

# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,'DEL','NEW DELHI', 'IGIA'),
# (2,'CCU','KOLKATA', 'NSCA'),
# (3,'BOM','MUMBAI', 'CSMA')
# """)
# conn.commit()


# Search / Retrive
mycursor.execute("SELECT * From airport where airport_id = 1")
data = mycursor.fetchall()
print(data)

# Update
mycursor.execute(" UPDATE airport set name = 'ABC' where airport_id = 3  ")

# Search / Retrive
mycursor.execute("SELECT * From airport")
data = mycursor.fetchall()
print(data)

mycursor.execute('delete from airport where airport_id = 3')
conn.commit()  # use it for all write operation