import sqlite3


def create_database():
    conn = sqlite3.connect('star_wars.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            birth_year TEXT,
            eye_color TEXT,
            films TEXT,
            gender TEXT,
            hair_color TEXT,
            height INTEGER,
            homeworld TEXT,
            mass INTEGER,
            name TEXT UNIQUE,
            skin_color TEXT,            
            species TEXT,            
            starships  text , 
            vehicles   text 
            )
        """)

create_database()