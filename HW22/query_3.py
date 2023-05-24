import sqlite3
from pprint import pprint

db = sqlite3.connect("db/database_1.sqlite")

cursor = db.cursor()

query = ("SELECT age, COUNT(id) as users FROM users "
         "GROUP BY age")
res = cursor.execute(query)
pprint(res.fetchall())
