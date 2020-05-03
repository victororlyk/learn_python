import sqlite3

db = sqlite3.connect('contacts.sqlite')

# to update rows we may use strings which we can pass to cursor and then
# even get amount of updated  rows
new_email = "w@gmail.com"
phone = input('please enter a number')  # if user would input something like
# 1;drop table contacts if we have no execute but executescript it will
# delete our table
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))

print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

c = db.cursor()
c.execute("SELECT * FROM contacts")
for name, phone, email in c:
    print(name, phone, email)

db.close()
