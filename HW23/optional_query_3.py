import sqlite3
from pprint import pprint

db = sqlite3.connect("db/book_store.sqlite")
cursor = db.cursor()

query = ("SELECT books.author, COUNT(purchase.id) AS amount "
         "FROM purchase "
         "JOIN books on books.id = purchase.book_id "
         "AND books.author = 'Rowling' "
         "GROUP BY books.author")

result = cursor.execute(query)
pprint(result.fetchall())
