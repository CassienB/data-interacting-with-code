# pylint: disable=missing-docstring, C0103
import sqlite3

def directors_count(db):
    # return the number of directors contained in the database
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    db.execute('''
        SELECT COUNT(d.id)
        FROM directors d ''')
    count = db.fetchone()
    return count[0]

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute('''
        SELECT d.name
        FROM directors d
        ORDER BY d.name  ASC  ''')
    tuples = db.fetchall()
    order = []
    for tuple in tuples:
        order.append(tuple[0])
    return order



def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db.execute('''
        SELECT *
        FROM movies m
        WHERE UPPER(m.title) LIKE '%love%' OR "%love'%" OR '%love,' OR '%love.%'
        ORDER BY m.title ASC
          ''')
    order = db.fetchall()
    return order


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    db.execute(f'''
        SELECT COUNT(d.id)
        FROM directors d
        WHERE UPPER(d.name) LIKE '% {name} %' ''')
    count = db.fetchone()
    return count[0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    db.execute(f'''
        SELECT *
        FROM movies m
        WHERE m.minutes > {min_length}
        ORDER BY m.title ASC
  ''')
    tuples = db.fetchall()
    order = []
    for tuple in tuples:
        order = order.append(tuple[0])
        return order
