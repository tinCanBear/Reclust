__author__ = 'UriA12'
insert_or_ignore = "INSERT OR IGNORE"

def insert(table, values):
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist, ))
def select(field, table, fields)
    # cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    # artist_id = cur.fetchone()[0]
    #
    # cur.execute('''INSERT OR IGNORE INTO Genre (name)
    #     VALUES ( ? )''', (genre, ))
    # cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    # genre_id = cur.fetchone()[0]
    #
    # cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
    #     VALUES ( ?, ? )''', ( album, artist_id ) )
    # cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    # album_id = cur.fetchone()[0]
    #
    # cur.execute('''INSERT OR REPLACE INTO Track
    #     (title, album_id, genre_id, len, rating, count)
    #     VALUES ( ?, ?, ?, ?, ?, ? )''',
    #     (name, album_id, genre_id, length, rating, count))
