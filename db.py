import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()
dict_lookup = dict()
fhand = open("output.txt", "r+")
for line in fhand:
    words = line.split(",")
    host = words[0]
    value = words[1]
	if host 	
	

cursor.execute(INSERT INTO test (host, address)
                   VALUES(%s, %s), (host, value))

db.commit()
db.close()

print "Done."