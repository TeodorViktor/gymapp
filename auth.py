import sqlite3
import bcrypt


def register_agent(username, password):
    con = sqlite3.connect("gym.db")
    cur = con.cursor()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cur.execute("INSERT INTO agents (username, password) VALUES (?, ?)", (username, hashed))
        con.commit()
    except sqlite3.IntegrityError:
        print("Username already exists. Please create a new one")
    con.close()


def login_agent(username, password):
    con = sqlite3.connect("gym.db")
    cur = con.cursor()
    try:
        cur.execute("SELECT password FROM agents WHERE username=?", (username,))
        result = cur.fetchone()
        if result and bcrypt.checkpw(password.encode(), result[0]):
            return True
        return False
    finally:
        con.close()
