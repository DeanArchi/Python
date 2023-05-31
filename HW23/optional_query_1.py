import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases "
         "FROM users "
         "JOIN purchase on users.id = purchase.user_id "
         "JOIN books on books.id = purchase.book_id "
         "GROUP BY users.id, users.first_name, users.last_name")

result = cursor.execute(query)
pprint(result.fetchall())
