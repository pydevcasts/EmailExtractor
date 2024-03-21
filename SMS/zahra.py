from tkinter import *
import temp
import asyncio
from googlesearch import search
import requests
import sqlite3
import asyncio
import re




root = Tk() 
root.geometry("500x500")
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack(side = BOTTOM)
Label(root, text='enter keyword :').pack()
query_entry = Entry(root) 
query_entry.pack()

greenbutton = Button(frame, text = 'search', fg='brown',command=lambda: search_button_click(query_entry)) 
greenbutton.pack( side = LEFT ) 

bluebutton = Button(frame, text ='sendMessage', fg ='blue',command=temp.main) 
bluebutton.pack( side = LEFT ) 

redbutton = Button(frame, text ='clearData', fg ='red',command=lambda: asyncio.run(clearData())) 
redbutton.pack( side = LEFT ) 

Button(bottomframe, text="Quit",bg='red',fg ='black', command=root.destroy).pack() #button to close the window





conn= sqlite3.connect('zaraDataBase.db')
c = conn.cursor()
c.execute('''
        CREATE TABLE IF NOT EXISTS  informations
        ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [phone_number] TEXT, [url] TEXT)
        ''')

conn.commit()


def clearData():
    try:
        conn = sqlite3.connect('zaraDataBase.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS  informations')
        conn.commit()
    except:
        print("not exits")

T = Text(root, height=20, width=50) 
T.pack() 

def fetch_search(q):
        try:
            result=search(q, sleep_interval=2, num_results=30)
            for i in result:
                ourMessage = i+"\n"
                T.insert(END, ourMessage)
                getNumbers(i)
        except:
            print("no result")
        
            
                
def getNumbers(url):
    response = requests.get(url)
    mobile_phone_numbers = list(set(re.findall(r'\b(09\d{9})\b', response.text)))
    if mobile_phone_numbers == []: 
        mph="123"
    else:
        mph=mobile_phone_numbers[0]
    try:
        c.execute("INSERT INTO informations (phone_number, url ) VALUES (?, ?)" ,(mph,url))
        conn.commit()
    except: print("nooooooooooooooooo")

def search_button_click(query): 
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(fetch_search(query.get())) 


root.mainloop() 

