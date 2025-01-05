import sqlite3 as sql

def connection():
    connection = sql.connect("customer.db")
    cursor = connection.cursor()
    return connection, cursor

def executeCreateAndInsert(connection,cursor):
        cursor.execute("""CREATE TABLE Customers(
            f_name text,
            l_name text,
            email text,
            age integer,
            city text,
            state text,
            zip integer,
            phone integer
            )
            """)
        
        Customers =  [
            ('Amit', 'Sharma', 'amit.sharma89@gmail.com', 30, 'Mumbai', 'Maharashtra', 400001, 9812345678),
            ('Priya', 'Singh', 'priya.singh77@yahoo.com', 27, 'Bangalore', 'Karnataka', 560001, 9987654321),
            ('Rahul', 'Verma', 'rahul.verma91@hotmail.com', 32, 'Chennai', 'Tamil Nadu', 600001, 8876543210),
            ('Sneha', 'Patel', 'sneha.patel123@gmail.com', 25, 'Ahmedabad', 'Gujarat', 380001, 9876543212),
            ('Karan', 'Malhotra', 'karan.malhotra@gmail.com', 28, 'Hyderabad', 'Telangana', 500001, 9654321789),
            ('Neha', 'Gupta', 'neha.gupta87@gmail.com', 29, 'Kolkata', 'West Bengal', 700001, 9123456789),
            ('Vikas', 'Yadav', 'vikas.yadav@gmail.com', 31, 'Pune', 'Maharashtra', 411001, 9345678901),
            ('Anjali', 'Mehra', 'anjali.mehra@gmail.com', 26, 'Jaipur', 'Rajasthan', 302001, 9765432187),
            ('Siddharth', 'Chopra', 'sid.chopra@gmail.com', 33, 'Lucknow', 'Uttar Pradesh', 226001, 9456783210),
            ('Rohan', 'Kapoor', 'rohan.kapoor@gmail.com', 35, 'Chandigarh', 'Chandigarh', 160001, 9876549876)
        ]

        cursor.executemany("INSERT INTO Customers VALUES (?,?,?,?,?,?,?,?)", Customers)

        connection.commit()

    

def showAll(connection,cursor):
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()

def AddOne(connection,cursor,Record:tuple):
    cursor.execute(f"INSERT INTO Customers VALUES {Record}")
    connection.commit()

def DeleteRecord(connection,cursor,rowid:int):
    cursor.execute(f"DELETE FROM Customers WHERE rowid = {rowid}")
    connection.commit()

def AddMultipleRecords(connection,cursor,Records:list):
    cursor.executemany("INSERT INTO Customers VALUES (?,?,?,?,?,?,?,?)", Records)
    connection.commit()

def lookupFromRow(connection,cursor,rowid:int,*columns):
    columns = ','.join(columns)
    cursor.execute(f"SELECT {columns} FROM Customers WHERE rowid = {rowid}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()

def closeConnection(connection):
    connection.close() 