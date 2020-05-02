import sqlite3

db = sqlite3.connect('contacts.sqlite')

# to update rows we may use strings which we can pass to cursor and then
# even get amount of updated  rows
update_sql = "UPDATE contacts SET email = 'updated@updated.com' WHERE " \
             "contacts.phone = 234"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))
print(db.commit == update_cursor.connection.commit)
update_cursor.connection.commit()
update_cursor.close()


c = db.cursor()
c.execute("SELECT * FROM contacts")
for name, phone, email in c:
    print(name, phone, email)

db.close()
