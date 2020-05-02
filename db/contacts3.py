import sqlite3

db = sqlite3.connect("contacts.sqlite")


cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for row in cursor:
    print(row)
