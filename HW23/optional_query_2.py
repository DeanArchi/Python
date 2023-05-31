import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT users.id, users.first_name, users.last_name, COUNT(purchase.id) AS purchases_count "
         "FROM users "
         "JOIN purchase on users.id = purchase.user_id "
         "GROUP BY users.id, users.first_name, users.last_name")

result = cursor.execute(query)
pprint(result.fetchall())
