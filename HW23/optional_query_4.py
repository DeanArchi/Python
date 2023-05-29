import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT books.author, SUM(books.price) AS total_purchases, COUNT(purchase.id) AS purchases_count "
         "FROM books "
         "JOIN purchase on books.id = purchase.book_id "
         "GROUP BY books.author")

result = cursor.execute(query)
pprint(result.fetchall())
