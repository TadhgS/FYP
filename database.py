import sqlite3


nouns = []
nounsplural = []
propernounS = []
propernounP = []
verbs = []
verbpast = []
verb3person = []
adverb = []
useless = []
unUsedWords = []
adjective = []

file = open("testfile.txt","w")


connect = sqlite3.connect('scoodydoo.db')

cursor = connect.cursor()

#cursor.execute("""CREATE TABLE location (
#                local text,
#                wether text
#                )""")
#cursor.execute("""CREATE TABLE monsters (
#                monster text,
#                local text,
#                name text,
#                clue text
#                )""")
#cursor.execute("""CREATE TABLE words(
#                word text,
#                type text,
#                local text,
#                freq integer
#                )""")

#cursor.execute("INSERT INTO words VALUES ('Hello','NN','Castle','6')")

#cursor.execute("UPDATE words SET freq "+str(x)+" WHERE word = "+word+"")
#cursor.execute("SELECT * FROM words")
#print(cursor.fetchall())

#cursor.execute("DELETE FROM monsters")
#cursor.execute("SELECT * FROM monsters")

#print(cursor.fetchall())
connect.commit()
