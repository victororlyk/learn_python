import sqlite3

db = sqlite3.connect("contacts.sqlite")

n = input("Enter a name")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts WHERE name Like ?", (n,))

for row in cursor:
    print(row)

db.close()
