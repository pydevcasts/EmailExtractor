import sqlite3


async def clearData():
    
    try:
        conn = sqlite3.connect('SMS/sqlite.db')
        cur = conn.cursor()
        await cur.execute('DROP TABLE IF EXISTS  phone_numbers')
        conn.commit()
    except:
        print("not exits")

