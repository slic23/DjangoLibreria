import sqlite3
con = sqlite3.connect('db.sqlite3')

cur = con.cursor()

# Create table
datos = cur.execute('''select * from catalog_book''').fetchmany()

print(datos)

datos = cur.execute("select * from catalog_book").fetchmany()
print(datos)
todos = cur.execute("select * from catalog_book").fetchall()

print(todos)


