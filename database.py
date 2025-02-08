import sqlite3


def init_db():
    # Create the db and connect with it
    con = sqlite3.connect("gym.db")

    # execute SQL statements and fetch results from SQL queries, we will need to use a database cursor
    cur = con.cursor()

    # Create db table for the gym memebers and agents
    cur.execute('''
        CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age DATE,
            membership_expiry DATE
        )
    ''')
    con.commit()
    con.close()


if __name__ == "__main__":
    init_db()
