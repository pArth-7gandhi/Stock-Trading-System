import sqlite3

def get_db_connection():
    conn = sqlite3.connect("orders.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            order_type TEXT NOT NULL,
            limit_price REAL,
            status TEXT DEFAULT 'pending',
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
