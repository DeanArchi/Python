import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT purchase.id, purchase.date, users.first_name, users.last_name "
         "FROM purchase JOIN users "
         "ON purchase.user_id = users.id")

result = cursor.execute(query)
pprint(result.fetchall())
