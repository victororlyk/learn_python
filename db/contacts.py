import sqlite3

db = sqlite3.connect('contacts.sqlite')
db.execute(
    "CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute(
    "INSERT INTO contacts(name, phone, email) values('Tim', 234234, 'tim@gmailc.om')")
db.execute("INSERT INTO contacts values ('brian', 234, 'brian@gamil.com')")

cursor = db.cursor()  # it is iterable because it is generator
cursor.execute("SELECT * FROM contacts")
# print(cursor.fetchall())
# [('Tim', 234234, 'tim@gmailc.om'), ('brian', 234, 'brian@gamil.com')]
for name, phone, email in cursor:
    print(name, phone, email)
    # if uncomment above code this will not be ooutputed

cursor.close()
db.commit() # without this code data will not be committed
db.close()
