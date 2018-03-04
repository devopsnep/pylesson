import sqlite3
filename='/Users/ezer/mbox.txt'
fh=open(filename)
eml=[]
for line in fh:
    if not line.startswith('From: '): continue
    email=line.split()[1]
    eml.append(email)
words={}
for w in eml:
    words[w]=words.get(w,0)+1

conn = sqlite3.connect('/Users/ezer/emailtable.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

for k,v in words.items():
    print(k,v)
    cur.execute('''INSERT INTO Counts (email, count) VALUES (?, ?)''',(k,v))
    conn.commit()

cur.close()


