# import aiohttp
# import asyncio 
# from googlesearch import search 

# import re 
# import sqlite3 
# import tkinter as tk 

# async def fetch(url, session):
#     try:
#         async with session.get(url) as response:
#             return response.status 
#     except:
#         print("خطا")
#         return

# async def search_phone_numbers(query, output_text):
#     urls = [result for result in search(query, tld="co.in", num=30)] 
#     print(urls)
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(url, session) for url in urls]
#         responses = await asyncio.gather(*tasks)
#         conn = sqlite3.connect('SMS/sqlit.db') 
#         c = conn.cursor() 

#         c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers (url TEXT, mobile_numbers TEXT, city_numbers TEXT)''') 
        
#         for i, response in enumerate(responses):
#             try:
#                 phone_numbers = re.findall(r'\b(09\d{9})\b', response.text) 
#                 phone_numbers = list(set(phone_numbers)) 
#                 domain = response.url.split('/')[2] 
#                 output_text.insert(tk.END, f"Phone numbers for {domain}:\n") 
#                 output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")

#                 city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text) 
#                 city_numbers = list(set(city_numbers)) 
#                 output_text.insert(tk.END, f"City numbers: {city_numbers}\n===========================================================\n") 
#                 c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)", 
#                         (response.url, ', '.join(phone_numbers), ', '.join(city_numbers))) 
#             except:
#                 print("text erorr")


#         print("END")
#         conn.commit() 
#         conn.close()


# def search_button_click(query, output_text): 
#     loop = asyncio.get_event_loop() 
#     loop.run_until_complete(search_phone_numbers(query.get(), output_text)) 

# root = tk.Tk() 
# root.title("URL Phone Number Search") 

# query_label = tk.Label(root, text="What do you want to search?") 
# query_label.pack() 

# query_entry = tk.Entry(root) 
# query_entry.pack() 

# search_button = tk.Button(root, text="Search", command=lambda: search_button_click(query_entry, output_text)) 
# search_button.pack() 

# output_text = tk.Text(root, height=30, width=100) 
# output_text.pack() 

# root.mainloop()

####################################################################
