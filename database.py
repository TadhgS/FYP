import sqlite3

connect = sqlite3.connect('scoodydoo.db')

cursor = connect.cursor()

#cursor.execute("""CREATE TABLE location (
#                local text,
#                wether text
#                )""")
#cursor.execute("""CREATE TABLE monsters (
#                monster text,
#                local text,
#                name text
#                )""")
#cursor.execute("""CREATE TABLE words(
#                word text,
#                type text,
#                local text,
#                freq integer
#                )""")
x = 8
word = "Hello"
#cursor.execute("INSERT INTO words VALUES ('Hello','NN','Castle','6')")

#cursor.execute("UPDATE words SET freq "+str(x)+" WHERE word = "+word+"")

#cursor.execute("SELECT * FROM words")
#print(cursor.fetchall())
connect.commit()
