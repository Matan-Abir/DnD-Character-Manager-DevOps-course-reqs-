import sqlite3
import json
import os
from datetime import datetime

DB_PATH = '/var/db/dnd-app/characters.db'

def init_db():
    """Initialize SQLite database with characters table"""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE characters
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      level INTEGER NOT NULL,
                      race TEXT NOT NULL,
                      class TEXT NOT NULL,
                      stats TEXT NOT NULL,
                      inventory TEXT NOT NULL,
                      created_at TIMESTAMP)''')
        conn.commit()
        conn.close()

def add_character(name, level, race, char_class, stats, inventory):
    """Add a new character to the database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO characters 
                 (name, level, race, class, stats, inventory, created_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (name, level, race, char_class, json.dumps(stats), json.dumps(inventory), datetime.now()))
    conn.commit()
    char_id = c.lastrowid
    conn.close()
    return char_id

def get_all_characters():
    """Retrieve all characters"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM characters ORDER BY level DESC')
    rows = c.fetchall()
    conn.close()
    
    characters = []
    for row in rows:
        characters.append({
            'id': row[0],
            'name': row[1],
            'level': row[2],
            'race': row[3],
            'class': row[4],
            'stats': json.loads(row[5]),
            'inventory': json.loads(row[6])
        })
    return characters

def get_character(char_id):
    """Retrieve a single character by ID"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM characters WHERE id = ?', (char_id,))
    row = c.fetchone()
    conn.close()
    
    if row:
        return {
            'id': row[0],
            'name': row[1],
            'level': row[2],
            'race': row[3],
            'class': row[4],
            'stats': json.loads(row[5]),
            'inventory': json.loads(row[6])
        }
    return None

def update_character(char_id, name, level, race, char_class, stats, inventory):
    """Update an existing character"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''UPDATE characters 
                 SET name = ?, level = ?, race = ?, class = ?, stats = ?, inventory = ?
                 WHERE id = ?''',
              (name, level, race, char_class, json.dumps(stats), json.dumps(inventory), char_id))
    conn.commit()
    conn.close()

def delete_character(char_id):
    """Delete a character"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM characters WHERE id = ?', (char_id,))
    conn.commit()
    conn.close()

def search_characters(keyword):
    """Search characters by keyword"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM characters WHERE name LIKE ? OR race LIKE ? OR class LIKE ?',
              (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    rows = c.fetchall()
    conn.close()
    
    characters = []
    for row in rows:
        characters.append({
            'id': row[0],
            'name': row[1],
            'level': row[2],
            'race': row[3],
            'class': row[4],
            'stats': json.loads(row[5]),
            'inventory': json.loads(row[6])
        })
    return characters
