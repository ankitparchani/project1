import sqlite3

conn = sqlite3.connect('emailid.sqlite') #if there is not file then will create a new file with the given name
curr = conn.cursor() #to get the access to open and send sql command and get the response

curr.execute('''DROP TABLE IF EXISTS Counts''')

curr.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')

if(len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    print(pieces)
    email = pieces[1]
    curr.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = curr.fetchone()
    if row is None:
        curr.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        curr.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    conn.commit()
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in curr.execute(sqlstr):
    print(str(row[0]), row[1])

curr.close()