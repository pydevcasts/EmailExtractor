import sqlite3
def clearData():
    try:
        conn = sqlite3.connect('SMS/sqlit.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS  phone_numbers')
        conn.commit()
    except:
        print("not exits")

