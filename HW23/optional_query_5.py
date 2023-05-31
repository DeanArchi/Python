import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT books.title, COUNT(purchase.id) as purchases_count "
         "FROM books "
         "LEFT JOIN purchase on books.id = purchase.book_id "
         "GROUP BY books.title "
         "ORDER BY purchases_count DESC")

result = cursor.execute(query)
pprint(result.fetchall())
