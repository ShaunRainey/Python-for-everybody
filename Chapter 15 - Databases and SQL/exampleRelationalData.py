import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
                  
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
                  
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
                  
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')

handle = open('tracks.csv')

genreDict = dict()

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces)<6: continue

    genre = pieces[6]
    #if genre == '0': print(line)
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))

x = cur.execute('SELECT * FROM Genre')

for row in x:
    genreDict[row[1]] = row[0]

handle = open('tracks.csv')

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 6 : continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]
    
    if genre in genreDict:
        genre_id = genreDict[genre]
    #print(genre)
    #print(genre_id)
    #print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ?)''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()

sqlQuery = """
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
"""

x = cur.execute(sqlQuery)

for row in x:
    print(row)

    



