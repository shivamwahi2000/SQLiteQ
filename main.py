import database as db

connection,cursor = db.connection()

#db.executeCreateAndInsert(connection,cursor)
#db.AddOne(connection,cursor,('Radha','Krishnan','rk123@gmail.com',24,'Delhi','Delhi',110032,7825649371))
#db.DeleteRecord(connection,cursor)

# records = [
#     ('John', 'Doe', 'john.doe@example.com', 29, 'New York', 'New York', 10001, 2125551234),
#     ('Sara', 'Smith', 'sara.smith@example.com', 34, 'Los Angeles', 'California', 90001, 3235555678),
#     ('Mohan', 'Reddy', 'mohan.reddy@example.in', 25, 'Hyderabad', 'Telangana', 500001, 9705551234),
#     ('Lina', 'Chavez', 'lina.chavez@example.com', 28, 'Miami', 'Florida', 33101, 3055559876),
#     ('Nina', 'Patel', 'nina.patel@example.co.uk', 32, 'London', 'England', 11101, 2075554321),
#     ('Rakesh', 'Gupta', 'rakesh.gupta@example.in', 27, 'Delhi', 'Delhi', 110085, 9812346578),
#     ('Sophia', 'Martinez', 'sophia.martinez@example.com', 30, 'Dallas', 'Texas', 75201, 2145559876),
#     ('Kiran', 'Sharma', 'kiran.sharma@example.in', 33, 'Chennai', 'Tamil Nadu', 600017, 9383456789),
#     ('Emma', 'Jones', 'emma.jones@example.com', 24, 'Chicago', 'Illinois', 60601, 3125552468),
#     ('Raj', 'Patel', 'raj.patel@example.in', 36, 'Mumbai', 'Maharashtra', 400001, 9223345678)
# ]

#db.AddMultipleRecords(connection,cursor,records)

#db.showAll(connection,cursor)

#db.lookupFromRow(connection,cursor,1,'f_name','l_name','email')

db.closeConnection(connection)