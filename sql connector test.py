import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shashi2022!",
    database="test"
)
cursor = mydb.cursor()

cursor.execute("insert into test_table values(2,\"Shash\",09754321)")

cursor.execute("SELECT * FROM test_table;")

rows = cursor.fetchall()
print (rows)

mydb.commit()

cursor.close()
mydb.close()
