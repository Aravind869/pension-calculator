import sqlite3


def connect():
    con = sqlite3.connect("pension.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS pension(id INTEGER PRIMARY KEY,name text,age INTEGER,basicpay INTEGER,avgsal INTEGER,totservice INTEGER,totpen INTEGER,totcom INTEGER)")
    con.commit()
    con.close()


def insert(name,age,basicpay,avgsal,totser,totpen,totcom):
    con = sqlite3.connect("pension.db")
    cur = con.cursor()
    cur.execute("INSERT INTO pension VALUES(NULL,?,?,?,?,?,?,?)",(name,age,basicpay,avgsal,totser,totpen,totcom))
    con.commit()
    con.close()


def views():
    con = sqlite3.connect("pension.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM pension")
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("pension.db")
    cur = con.cursor()
    cur.execute("DELETE FROM pension WHERE id=?", (id,))
    con.commit()
    con.close()

connect()
