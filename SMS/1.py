from tkinter import *
import temp
import asyncio
from googlesearch import search
import requests
import sqlite3
import asyncio
import re


async def main():

    root = Tk() 
    root.geometry("500x500")
    frame = Frame(root) 
    frame.pack() 
    bottomframe = Frame(root) 
    bottomframe.pack(side = BOTTOM)
    Label(root, text='enter keyword :').pack()
    query_entry = Entry(root) 
    query_entry.pack()
    output_text = Text(root, height=40, width=100) 
    output_text.pack() 

    greenbutton = Button(frame, text = 'search', fg='brown',command=lambda: search_button_click(query_entry, output_text)) 
    greenbutton.pack( side = LEFT ) 

    bluebutton = Button(frame, text ='sendMessage', fg ='blue',command=temp.main) 
    bluebutton.pack( side = LEFT ) 

    redbutton = Button(frame, text ='clearData', fg ='red',command=lambda: asyncio.run(clearData())) 
    redbutton.pack( side = LEFT ) 

    Button(bottomframe, text="Quit",bg='red',fg ='black', command=root.destroy).pack() #button to close the window


    async def fetch(url):
        try:
            response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url) 
            return response 
        except:
            print("eroorrrrrr :(")
        


    async def search_phone_numbers(query, output_text):
        urls = [] 
        for result in search(query, tld="co.in"):
            urls.append(result) 

        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(fetch(url))) 

        responses = await asyncio.gather(*tasks) 

        conn = sqlite3.connect('urlgetphonenumber.db') 
        c = conn.cursor() 

        c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers (url TEXT, mobile_numbers TEXT, city_numbers TEXT)''') 
        
        for i, response in enumerate(responses):
            try:
                phone_numbers = re.findall(r'\b(09\d{9})\b', response.text) 
                phone_numbers = list(set(phone_numbers)) 
                domain = response.url.split('/')[2] 
                output_text.insert(END, f"Phone numbers for {domain}:\n") 
                output_text.insert(END, f"Mobile numbers: {phone_numbers}\n")

                city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text) 
                city_numbers = list(set(city_numbers)) 
                output_text.insert(END, f"City numbers: {city_numbers}\n===========================================================\n") 
                c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)", 
                        (response.url, ', '.join(phone_numbers), ', '.join(city_numbers))) 
            except:
                print("text erorr")


        print("END")
        conn.commit() 
        conn.close()


    def clearData():
        try:
            conn = sqlite3.connect('zaraDataBase.db')
            cur = conn.cursor()
            cur.execute('DROP TABLE IF EXISTS  informations')
            conn.commit()
        except:
            print("not exits")


    async def search_button_click(query, output_text): 
        loop = asyncio.get_event_loop() 
        loop.run_until_complete(search_phone_numbers(query.get(), output_text)) 


    root.mainloop()
if __name__ == "__main__":
    asyncio.run(main())