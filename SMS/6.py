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
    urls = [result for result in search(query, tld="co.in", num=30)]
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[fetch(url, session) for url in urls])

    # Extract all the phone numbers from the HTML responses
    phone_numbers = []
    for response in responses:
        phone_numbers.extend(re.findall(r"\d{10}", response[0]))

    # Insert the phone numbers into the text widget
    for phone_number in phone_numbers:
        print(phone_number, 0000000000)
        output_text.insert("end", phone_number + "\n")

def search_button_click():
    asyncio.run(search_phone_numbers(query_entry.get(), output_text))

root = tk.Tk()
root.title("URL Phone Number Search")

query_label = tk.Label(root, text="What do you want to search?")
query_label.pack()

query_entry = tk.Entry(root)
query_entry.pack()

search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.pack()

output_text = tk.Text(root, height=30, width=100)
output_text.pack()

root.mainloop()
