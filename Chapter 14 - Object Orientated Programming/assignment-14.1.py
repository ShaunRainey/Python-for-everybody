import sqlite3
import re

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Counts""")
cur.execute("""DROP TABLE IF EXISTS Counts2""")
cur.execute("""CREATE TABLE Counts (org TEXT, count INTEGER)""")

fname = input("Enter file name: ")
if(len(fname)) < 1: fname = "mbox.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    #print(line)
    pieces = line.split()
    org = re.findall("@([a-zA-Z]+\.[a-zA-Z]+.[a-zA-Z]*.[a-zA-Z]*)",pieces[1])
    if len(org) <1: continue
    else: org = org[0]

    cur.execute("SELECT count FROM Counts WHERE org = ?",(org,))
    row = cur.fetchone()
    if row is None:
        cur.execute("""INSERT INTO Counts (org,count) VALUES (?, 1)""",(org,))
    else: 
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))
    conn.commit()

sqlStr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

newList = list()

for row in cur.execute(sqlStr):
    newList.append(row)
    #print(f"Mail from {row[0]} appears {row[1]} times")

cur.close()
