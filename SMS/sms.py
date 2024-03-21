from tkinter import *
import asyncio
from googlesearch import search
import requests
import re
from cleardata import clearData
import sqlite3




# تغییر رنگ پس زمینه به حالت تاریک
# root.configure(bg="white")

# frame = Frame(root).pack() 
# bottomframe = Frame(root).pack(side = BOTTOM)
# Label(root, text='ENTER KEYWORD :').pack()

# redbutton = Button(frame, text ='clearData',fg ='red',command=lambda: clearData()).pack( side = LEFT ) 
# output_text = Text(root)
# query_entry = Entry(root).pack()

# # greenbutton = Button(frame, text = 'search', fg='green',command=lambda: search_button_click(query_entry, output_text)).pack() 
# Button(bottomframe, text="Quit",bg='red',fg ='black', command=root.destroy).pack() #button to close the window

#######################################
root = Tk() 
root.title("PHONE BANK")
root.geometry("500x500")

query_label =Label(root, text="ENTER KEYWORD:",  height=2) 
query_label.pack(fill='x') 

query_entry = Entry(root, justify="right", width=25, font=("calibri 15 italic"), cursor="pencil", selectbackground="red", selectforeground="green") 
query_entry.pack() 


search_button =Button(root, text="Search",border=4, bg='green',fg="white",command=lambda: search_button_click(query_entry, output_text)) 
search_button.pack(pady=10) 

output_text = Text(root, height=300, width=100) 
output_text.pack() 

conn = sqlite3.connect('SMS/sqlit.db') 
c = conn.cursor() 
c.execute('''
        CREATE TABLE IF NOT EXISTS phone_numbers
        (url TEXT, mobile_numbers TEXT, city_numbers TEXT)
        ''') 


async def fetch(url):
    try:
        response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url) 
        return response 
    except Exception as err:
        print(f"error goes to :{err}")
    

async def search_phone_numbers(query, output_text):
    urls = [] 
    for result in search(query, tld="co.in",num = 30):
        urls.append(result) 
    tasks = [asyncio.ensure_future(fetch(url)) for url in urls]
    responses = await asyncio.gather(*tasks) 
    for i, response in enumerate(responses):
        try:
            phone_numbers = re.findall(r'\b(09\d{9})\b', response.text) 
            city_numbers = re.findall(r'\b(0^\+?\d+$)\b', response.text) 
            phone_numbers = list(set(phone_numbers)) 
            city_numbers = list(set(city_numbers)) 
            domain = response.url.split('/')[2] 
            output_text.insert(END, f"Phone numbers for {domain}:\n") 
            output_text.insert(END, f"Mobile numbers: {phone_numbers}\n")
            output_text.insert(END, f"City numbers: {city_numbers}\n===========================================================\n") 

            c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)", 
                    (response.url, ', '.join(phone_numbers), ', '.join(city_numbers))) 
        except Exception as err:
            print(f"Text erorr goes to {err}")

    print("END")
    conn.commit()
    conn.close()


def search_button_click(query, output_text): 
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(search_phone_numbers(query.get(), output_text)) 


root.mainloop()