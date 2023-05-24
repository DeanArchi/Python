import sqlite3

db = sqlite3.connect("db/database.sqlite")

cursor = db.cursor()

# Create table query
existing_check = "DROP TABLE IF EXISTS users"
cursor.execute(existing_check)

query = ("CREATE TABLE users ("
         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
         "first_name TEXT,"
         "last_name TEXT,"
         "age INTEGER)")

cursor.execute(query)

# Insert into table query
insert_query = ("INSERT INTO users (first_name, last_name, age) VALUES "
                "('Aliona', 'Kovalenko', 23),"
                "('Ivan', 'Ivanov', 19),"
                "('Maxym', 'Lysenko', 33),"
                "('Volodymyr', 'Shevchenko', 29),"
                "('Mariya', 'Sydorenko', 21),"
                "('Oleksandr', 'Petrov', 25)")

cursor.execute(insert_query)
db.commit()
