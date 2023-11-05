
import aiohttp
import asyncio
from googlesearch import search
import re
import sqlite3
import tkinter as tk

async def fetch(url, session):
    try:
        async with session.get(url) as response:
            return await response.text(), response.url
    except Exception as e:
        print(f"Error goes to: {e}")
        pass

async def search_phone_numbers(query, output_text):
    urls = [result for result in search(query, tld="co.in", num=5)]
    async with aiohttp.ClientSession() as session:
        asyncio.sleep(1)
        corons = [fetch(url, session) for url in urls]
        responses = await asyncio.gather(*corons) #type list
        conn = sqlite3.connect('SMS/sqlit3.db')
        c = conn.cursor()
# 
        c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers (url TEXT, mobile_numbers TEXT, city_numbers TEXT)''')

        for i, response in enumerate(responses):
            print(i, 0000000000000)
            print(response, 22222222222222222222222222222)
            try:
                phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
                print(type(phone_numbers, 444444444444444444444444))
                phone_numbers = list(set(phone_numbers))
                city_numbers = re.findall(r'\b(0^\+?\d+$)\b', response.text) 
                city_numbers = list(set(city_numbers)) 
                print(response[1], 11111111111)
                domain = response[1].split('/')[2]
                print(domain, 33333333333333333333)
               
                output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
                output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")
                output_text.insert(tk.END, f"City numbers: {city_numbers}\n============================================================\n")

                c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)", 
                    (response.url, ', '.join(phone_numbers), ', '.join(city_numbers))) 

            except Exception as err:
                print(f"Text error goes to {err}")

        print("END")
        conn.commit()
        conn.close()

def search_button_click(query, output_text):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(search_phone_numbers(query.get(), output_text))

root = tk.Tk()
root.title("PHONE BANK")

query_label = tk.Label(root, text="KEYWORD SEARCH")
query_label.pack()

query_entry = tk.Entry(root)
query_entry.pack()

search_button = tk.Button(root, text="Search", command=lambda: search_button_click(query_entry, output_text))
search_button.pack()

output_text = tk.Text(root, height=30, width=100)
output_text.pack()

root.mainloop()

