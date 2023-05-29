import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT users.id, users.first_name, users.last_name, books.title "
         "FROM users "
         "JOIN purchase ON purchase.user_id = users.id "
         "JOIN books ON purchase.book_id = books.id " 
         "ORDER BY purchase.user_id")

result = cursor.execute(query)
pprint(result.fetchall())
