import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Counts""")
cur.execute("""CREATE TABLE Counts (org TEXT, count INTEGER)""")

fname = input("Enter file name: ")
if(len(fname)) < 1: fname = "mbox.txt"
fh = open(fname)

for line in fh:
    if not line.startswith("From: "): continue
    
    pieces = line.split()
    pos = pieces[1].index("@") + 1
    org = pieces[1][pos:]   

    cur.execute("SELECT count FROM Counts WHERE org = ?",(org,))
    row = cur.fetchone()

    if row is None:
        cur.execute("""INSERT INTO Counts (org,count) VALUES (?, 1)""",(org,))
    else: 
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))
        #print(row)
    conn.commit()

sqlStr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
cur.execute(sqlStr)
conn.commit()

newList = list()

for row in cur.execute(sqlStr):
    newList.append(row)
    #print(row)
    print(f"Mail from {row[0]} appears {row[1]} times")

cur.close()
