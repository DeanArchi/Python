import sqlite3
from pprint import pprint

db = sqlite3.connect("db/database_1.sqlite")

cursor = db.cursor()

query = ("SELECT COUNT(id) as users FROM users "
         "WHERE age > 30")
res = cursor.execute(query)
pprint(res.fetchall())