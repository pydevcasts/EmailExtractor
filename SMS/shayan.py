# from googlesearch import search

# query = 'java'


# for i in search(query,        # The query you want to run
#                 tld = 'com',  # The top level domaincd 
#                 lang = 'en',  # The language
#                 num = 10,     # Number of results per page
#                 start = 0,    # First result to retrieve
#                 stop = None,  # Last result to retrieve
#                 pause = 0,  # Lapse between HTTP requests
#                 safe = 'high'

#                ):
#     print(i)
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.nasa.gov')
# headlines = driver.find_elements_by_class_name("headline")
# for headline in headlines:
#     # print(headline.text.strip())
#     print("hi")
# driver.close()
# ======================
# import time
# import re

# from selenium import webdriver
# from selenium import *
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# # # from selenium.webdriver.opera.options import Options
# # # driver = webdriver.Opera('drivers\operadriver.exe')


# driver =  webdriver.Chrome("C:/Users/shayan/Desktop/chromedriver-win64/chromedriver.exe")

# driver.get("https://www.google.com")
# print(driver.title)
# x = input("what do you want to search?")
# driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(x)
# # driver.find_element(By.CSS_SELECTOR, '[name="btnK"]')
# # driver.find_element(By.CLASS_NAME, 'gNO89b').click()

# attr = driver.switch_to.active_element.get_attribute("title")
# print(attr)
# ================
# from googlesearch import search
# import requests
# import re

# url = []

# query = input("what do you want to search?")

# for i in search(query, tld="co.in",pause=2):
#     url.append(i)
# try:
#     for i in url:
#         reponse = requests.get(i)
#         phone_number = re.findall(r'\b(09\d{9})\b', reponse.text)
#         phone_number = list(set(phone_number))
#         print(phone_number)

#         with open("phone.txt", 'a') as file:
#             file.write(i + " = " + str(phone_number) + "\n")

# except Exception as err:
#     print(f"we have e error: {err}")


# ===================


# import asyncio
# from googlesearch import search
# import requests
# import re
# from urllib.parse import urlparse

# async def fetch(url):
#     response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#     print(response,6666666666666)
#     return response

# async def search_phone_numbers(query):
#     urls = []
#     for result in search(query, tld="co.in", pause=2):
#         urls.append(result)

#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.ensure_future(fetch(url)))

#     responses = await asyncio.gather(*tasks)

#     for i, response in enumerate(responses):
#         phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#         phone_numbers = list(set(phone_numbers))
#         parsed_url = urlparse(urls[i])
#         domain = parsed_url.netloc
#         print(f"Phone numbers for {domain}:")
#         print("Mobile numbers:", phone_numbers)
#         city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#         city_numbers = list(set(city_numbers))
#         print("City numbers:", city_numbers)

#         with open("phone.txt", 'a') as file:
#             file.write(f"URL: {urls[i]} = [\n")
#             file.write(f"Mobile numbers: {phone_numbers}\n")
#             file.write(f"City numbers: {city_numbers} ]\n")
#             file.write("\n ==================================================================")

# query = input("What do you want to search? ")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(search_phone_numbers(query))

#=====================================


# <<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3

# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#         print(response, 666666)
#         return response
#     except:
#         print('erooooorrrr :(')
# async def search_phone_numbers(query):
#     urls = []
#     for result in search(query, tld="co.in", num = 20, stop = 20, pause = 2):
#         urls.append(result)

#     tasks = []
#     try:
#         for url in urls:
#             tasks.append(asyncio.ensure_future(fetch(url)))
#     except:
#         print("erorr 2")

#     responses = await asyncio.gather(*tasks)

#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers
#                  (url TEXT, mobile_numbers TEXT, city_numbers TEXT)''')

#     for i, response in enumerate(responses):
#         phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#         phone_numbers = list(set(phone_numbers))
#         domain = response.url.split('/')[2]
#         print(f"Phone numbers for {domain}:")
#         print("Mobile numbers:", phone_numbers)
        
#         city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#         city_numbers = list(set(city_numbers))
#         print("City numbers:", city_numbers)
        
#         c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)",
#                   (response.url, ', '.join(phone_numbers), ', '.join(city_numbers)))

#     conn.commit()
#     conn.close()

# query = input("What do you want to search? ")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(search_phone_numbers(query))

# ===================================
# from tkinter import *
# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3
# root = Tk()
# canvas1 = Canvas(root, width=400, height=800)
# canvas1.pack()
# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#         print(response, 666666)
#         return response
#     except:
#         print('erooooorrrr :(')
# async def search_phone_numbers(query):
#     urls = []
#     for result in search(query, tld="co.in", num = 20, stop = 20, pause = 2):
#         urls.append(result)

#     tasks = []
#     try:
#         for url in urls:
#             tasks.append(asyncio.ensure_future(fetch(url)))
#     except:
#         print("erorr 2")

#     responses = await asyncio.gather(*tasks)

#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers
#                  (url TEXT, mobile_numbers TEXT, city_numbers TEXT)''')

#     for i, response in enumerate(responses):
#         phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#         phone_numbers = list(set(phone_numbers))
#         domain = response.url.split('/')[2]
#         print(f"Phone numbers for {domain}:")
#         print("Mobile numbers:", phone_numbers)
        
#         city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#         city_numbers = list(set(city_numbers))
#         print("City numbers:", city_numbers)
        
#         c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)",
#                   (response.url, ', '.join(phone_numbers), ', '.join(city_numbers)))

#     conn.commit()
#     conn.close()

# entry1 = Entry(root) 
# canvas1.create_window(200, 140, window=entry1)
# query = entry1

# loop = asyncio.get_event_loop()
# loop.run_until_complete(search_phone_numbers(query))







# root.mainloop()


# =========================================================================

# import asyncio 
# from googlesearch import search 
# import requests 
# import re 
# import sqlite3 
# import tkinter as tk 



# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url) 
#         print(response, 11111111111111)
#         return response 
#     except:
#         print("eroorrrrrr :(")
    


# async def search_phone_numbers(query, output_text):
#     urls = [] 
#     for result in search(query, tld="co.in",num = 10, stop= 10 , pause=2):
#         urls.append(result) 

#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.ensure_future(fetch(url))) 

#     responses = await asyncio.gather(*tasks) 

#     conn = sqlite3.connect('urlgetphonenumber.db') 
#     c = conn.cursor() 

#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers (url TEXT, mobile_numbers TEXT, city_numbers TEXT)''') 
    
#     for i, response in enumerate(responses):
#         try:
#             phone_numbers = re.findall(r'\b(09\d{9})\b', response.text) 
#             phone_numbers = list(set(phone_numbers)) 
#             domain = response.url.split('/')[2] 
#             output_text.insert(tk.END, f"Phone numbers for {domain}:\n") 
#             output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")

#             city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text) 
#             city_numbers = list(set(city_numbers)) 
#             output_text.insert(tk.END, f"City numbers: {city_numbers}\n===========================================================\n") 
#             c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)", 
#                     (response.url, ', '.join(phone_numbers), ', '.join(city_numbers))) 
#         except:
#             print("text erorr")


#     print("END")
#     conn.commit() 
#     conn.close()


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



# ================================================

# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3
# import tkinter as tk
# from twilio.rest import Client

# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#         return response
#     except:
#         print("e 1")
# async def search_phone_numbers(query, output_text):
#     urls = []
#     for result in search(query, tld="co.in",num=1,stop = 1, pause=2):
#         urls.append(result)
        
#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.ensure_future(fetch(url)))
        
#     responses = await asyncio.gather(*tasks)
    
#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers (url TEXT, mobile_numbers TEXT, city_code TEXT)''')
#     c.execute('''CREATE TABLE IF NOT EXISTS cities (code TEXT, name TEXT)''')
    
#     twilio_account_sid = input("Enter your Twilio Account SID: ")
#     twilio_auth_token = input("Enter your Twilio Auth Token: ")
#     twilio_phone_number = input("Enter your Twilio Phone Number: ")
    
#     client = Client(twilio_account_sid, twilio_auth_token)
    
#     for i, response in enumerate(responses):
#         try:
#             # phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#             phone_numbers = "09304307827"
#             phone_numbers = list(set(phone_numbers))
#             domain = response.url.split('/')[2]
            
#             output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
#             output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")
            
#             city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#             city_numbers = list(set(city_numbers))
#             output_text.insert(tk.END, f"City numbers: {city_numbers}\n")
            
#             c.execute("INSERT INTO phone_numbers (url, mobile_numbers) VALUES (?, ?)", (response.url, ', '.join(phone_numbers)))
            
#             city_codes = []
#             for city_number in city_numbers:
#                 city_code = city_number.split('-')[0]
#                 city_codes.append(city_code)
                
#                 c.execute("SELECT code FROM cities WHERE code=?", (city_code,))
#                 result = c.fetchone()
                
#                 if result is None:
#                     city_name = input(f"Enter the name of the city with code {city_code}: ")
#                     c.execute("INSERT INTO cities (code, name) VALUES (?, ?)", (city_code, city_name))
            
#         except:
#             print("e 2")        
#         c.execute("UPDATE phone_numbers SET city_code=? WHERE rowid=?", (', '.join(city_codes), i+1))
        
#         for number in phone_numbers:
#             message = client.messages.create(
#                 body=f"New phone number found: {number}",
#                 from_=twilio_phone_number,
#                 to=number
#             )
#             output_text.insert(tk.END, f"SMS sent to {number}: {message.sid}\n")
            
#     c.execute('''DELETE FROM phone_numbers WHERE rowid NOT IN (
#                     SELECT MIN(rowid) FROM phone_numbers GROUP BY mobile_numbers, city_code
#                 )''')
    
#     conn.commit()
#     conn.close()

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

# output_text = tk.Text(root, height=10, width=50)
# output_text.pack()

# root.mainloop()


# =========================================
# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3
# import tkinter as tk
# from twilio.rest import Client


# async def fetch(url):
#     response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#     return response

# async def search_phone_numbers(query, output_text):
#     urls = []
#     for result in search(query, tld="co.in", pause=2):
#         urls.append(result)
        
#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.ensure_future(fetch(url)))
        
#     responses = await asyncio.gather(*tasks)
    
#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers (url TEXT, mobile_numbers TEXT, city_code TEXT)''')
#     c.execute('''CREATE TABLE IF NOT EXISTS cities (code TEXT, name TEXT)''')
    
#     twilio_account_sid = input("Enter your Twilio Account SID: ")
#     twilio_auth_token = input("Enter your Twilio Auth Token: ")
#     twilio_phone_number = input("Enter your Twilio Phone Number: ")
    
#     client = Client(twilio_account_sid, twilio_auth_token)
    
#     for i, response in enumerate(responses):
#         phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#         phone_numbers = list(set(phone_numbers))
#         domain = response.url.split('/')[2]
        
#         output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
#         output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")
        
#         city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#         city_numbers = list(set(city_numbers))
#         output_text.insert(tk.END, f"City numbers: {city_numbers}\n")
        
#         c.execute("INSERT INTO phone_numbers (url, mobile_numbers) VALUES (?, ?)", (response.url, ', '.join(phone_numbers)))
        
#         city_codes = []
#         for city_number in city_numbers:
#             city_code = city_number.split('-')[0]
#             city_codes.append(city_code)
            
#             c.execute("SELECT code FROM cities WHERE code=?", (city_code,))
#             result = c.fetchone()
            
#             if result is None:
#                 city_name = input(f"Enter the name of the city with code {city_code}: ")
#                 c.execute("INSERT INTO cities (code, name) VALUES (?, ?)", (city_code, city_name))
                
#         c.execute("UPDATE phone_numbers SET city_code=? WHERE rowid=?", (', '.join(city_codes), i+1))
        
#         for number in phone_numbers:
#             message = client.messages.create(
#                 body=f"New phone number found: {number}",
#                 from_=twilio_phone_number,
#                 to=number
#             )
#             output_text.insert(tk.END, f"SMS sent to {number}: {message.sid}\n")
            
#     c.execute('''DELETE FROM phone_numbers WHERE rowid NOT IN (
#                     SELECT MIN(rowid) FROM phone_numbers GROUP BY mobile_numbers, city_code
#                 )''')
    
#     conn.commit()
#     conn.close()

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

# output_text = tk.Text(root, height=10, width=50)
# output_text.pack()

# root.mainloop()

# ========================================

# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3
# import tkinter as tk
# from nexmo import Client



# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#         print(response, 1111111111111111)
#         return response

#     except:
#         print("e 1")

# async def search_phone_numbers(query, output_text):
#     urls = []
#     for result in search(query, tld="co.in",num = 2, stop = 2, pause=2): 
#         urls.append(result)

#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.ensure_future(fetch(url)))

#     responses = await asyncio.gather(*tasks)

#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers
#                  (url TEXT, mobile_numbers TEXT, city_code TEXT)''')

#     c.execute('''CREATE TABLE IF NOT EXISTS cities
#                  (code TEXT, name TEXT)''')

#     client = Client(key=nexmo_api_key, secret=nexmo_api_secret)

#     for i, response in enumerate(responses):
#         try:
#             phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)

#             phone_numbers = list(set(phone_numbers))
#             # phone_numbers = "09304307827"
#             domain = response.url.split('/')[2]
#             output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
#             output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")

#             city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#             city_numbers = list(set(city_numbers))
#             output_text.insert(tk.END, f"City numbers: {city_numbers}\n")

#             c.execute("INSERT INTO phone_numbers (url, mobile_numbers) VALUES (?, ?)",
#                     (response.url, ', '.join(phone_numbers)))

#             # Add city codes
#             city_codes = []
#             for city_number in city_numbers:
#                 city_code = city_number.split('-')[0]
#                 city_codes.append(city_code)

#                 # Check if city code already exists in cities table
#                 c.execute("SELECT code FROM cities WHERE code=?", (city_code,))
#                 result = c.fetchone()
#                 if result is None:
#                     city_name = input(f"Enter the name of the city with code {city_code}: ")
#                     c.execute("INSERT INTO cities (code, name) VALUES (?, ?)", (city_code, city_name))

#             c.execute("UPDATE phone_numbers SET city_code=? WHERE rowid=?", (', '.join(city_codes), i+1))

#             # Send SMS
#             for number in phone_numbers:
#                 response = client.send_message({
#                     "from": nexmo_phone_number,
#                     "to": number,
#                     "text": f"New phone number found: {number}"
#                 })

#                 output_text.insert(tk.END, f"SMS sent to {number}: {response['messages'][0]['status']}\n")
#         except:
#             print("e 2")
#     # Remove duplicate phone numbers
#     c.execute('''DELETE FROM phone_numbers WHERE rowid NOT IN (
#                     SELECT MIN(rowid) FROM phone_numbers GROUP BY mobile_numbers, city_code
#                 )''')

#     conn.commit()
#     conn.close()

# def search_button_click(query, output_text):
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(search_phone_numbers(query.get(), output_text))

# root = tk.Tk()
# root.title("URL Phone Number Search")

# query_label = tk.Label(root, text="What do you want to search?")
# query_label.pack()


# query_entry = tk.Entry(root)
# query_entry.pack()

# nexmo_api_key_t = tk.Label(root, text="Enter your Nexmo API Key: ")
# nexmo_api_key_t.pack()

# nexmo_api_key = tk.Entry(root)
# nexmo_api_key.pack()

# nexmo_api_secret_t = tk.Label(root, text="Enter your Nexmo API Secret: ")
# nexmo_api_secret_t.pack()

# nexmo_api_secret = tk.Entry(root)
# nexmo_api_secret.pack()

# nexmo_phone_number_t = tk.Label(root, text="Enter your Nexmo Phone Number: ")
# nexmo_phone_number_t.pack()

# nexmo_phone_number = tk.Entry(root)
# nexmo_phone_number.pack()

# search_button = tk.Button(root, text="Search", command=lambda: search_button_click(query_entry, output_text))
# search_button.pack()


# output_text = tk.Text(root, height=10, width=50)
# output_text.pack()

# root.mainloop()


# ============================================================================================================================================




# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3
# import tkinter as tk
# from nexmo import Client
# from kavenegar import *
# # کاوه نگار
# # api = KavenegarAPI('7344376363534F765236714345497948636635475956755A71355369785047506D50384D7569694C4D63343D')
# api = KavenegarAPI('7344376363534F765236714345497948636635475956755A71355369785047506D50384D7569694C4D63343D')

# # sender = "09..."
# # receptor = number
# # params = { sender : '09....', 'receptor':receptor, 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
# # response = api.sms_send( params)
# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#         print(response, 1111111111111111)
#         return response

#     except:
#         print("e 1")

# async def search_phone_numbers(query, output_text):
#     urls = []
#     for result in search(query, tld="co.in",num = 10, stop = 10, pause=2): 
#         urls.append(result)

#     tasks = []
#     for url in urls:
#         tasks.append(asyncio.ensure_future(fetch(url)))

#     responses = await asyncio.gather(*tasks)

#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers
#                  (url TEXT, mobile_numbers TEXT, city_code TEXT)''')

#     c.execute('''CREATE TABLE IF NOT EXISTS cities
#                  (code TEXT, name TEXT)''')

#     # nexmo_api_key = input("Enter your Nexmo API Key: ")
#     # nexmo_api_secret = input("Enter your Nexmo API Secret: ")
#     # nexmo_phone_number = input("Enter your Nexmo Phone Number: ")


#     # client = Client(key=nexmo_api_key, secret=nexmo_api_secret)

#     for i, response in enumerate(responses):
        
#             # phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)

#             phone_numbers = list(set(phone_numbers))
#             phone_numbers = ["09304307827"]
#             domain = response.url.split('/')[2]
#             output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
#             output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")

#             city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#             city_numbers = list(set(city_numbers))
#             output_text.insert(tk.END, f"City numbers: {city_numbers}\n")

#             c.execute("INSERT INTO phone_numbers (url, mobile_numbers) VALUES (?, ?)",
#                     (response.url, ', '.join(phone_numbers)))

#             # Add city codes
#             city_codes = []
#             for city_number in city_numbers:
#                 city_code = city_number.split('-')[0]
#                 city_codes.append(city_code)

#                 # Check if city code already exists in cities table
#                 c.execute("SELECT code FROM cities WHERE code=?", (city_code,))
#                 result = c.fetchone()
#                 if result is None:
#                     city_name = input(f"Enter the name of the city with code {city_code}: ")
#                     c.execute("INSERT INTO cities (code, name) VALUES (?, ?)", (city_code, city_name))

#             c.execute("UPDATE phone_numbers SET city_code=? WHERE rowid=?", (', '.join(city_codes), i+1))

#             # Send SMS
#             for number in phone_numbers:
#                 receptor = number
#                 # response = client.send_message({
#                 #     "from": nexmo_phone_number,
#                 #     "to": number,
#                 #     "text": f"New phone number found: {number}"
#                 # })

                
#                 params = { 'sender': phone_number, 'receptor':'09304307827', 'message' :message }
#                 response = api.sms_send( params)
#                 print(22222222222222222222222222222222222222222222)
#     #     except:
#     #         print("e 2")
#     # # Remove duplicate phone numbers
#     # c.execute('''DELETE FROM phone_numbers WHERE rowid NOT IN (
#     #                 SELECT MIN(rowid) FROM phone_numbers GROUP BY mobile_numbers, city_numbers
#     #             )''')

#     conn.commit()
#     conn.close()

# def search_button_click(query, output_text):
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(search_phone_numbers(query.get(), output_text))

# root = tk.Tk()
# root.title("Phone Number SMS")


# # label = tk.Label(root, bg="grey", font=('consolas', 4))
# # label.pack()

# # canvas = tk.Canvas(root, bg="pink", height=200, width=200)
# # canvas.pack()

# query_label = tk.Label(root, text="What do you want to search?")
# query_label.pack()


# query_entry = tk.Entry(root)
# query_entry.pack()

# message_t = tk.Label(root, text="Your message: ")
# message_t.pack()

# message = tk.Entry(root)
# message.pack()

# api_secret_t = tk.Label(root, text="Enter your kavenegar API Secret: ")
# api_secret_t.pack()

# api_secret = tk.Entry(root)
# api_secret.pack()

# phone_number_t = tk.Label(root, text="Enter your Phone Number: ")
# phone_number_t.pack()

# phone_number = tk.Entry(root)
# phone_number.pack()

# # api_geter_t = tk.Label(root, text="Enter your API")
# # api_geter_t.pack()

# # api_geter = tk.Entry(root)
# # api_geter.pack()

# api = KavenegarAPI(api_secret)

# search_button = tk.Button(root, text="Search", command=lambda: search_button_click(query_entry, output_text))
# search_button.pack()


# output_text = tk.Text(root, height=100, width=500)
# output_text.pack()

# root.mainloop()


# ========================================================================




# import asyncio
# from googlesearch import search
# import requests
# import re
# import sqlite3
# import tkinter as tk

# async def fetch(url):
#     try:
#         response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#         print(response, 11111111111)
#         return response
#     except:
#         print("e......1")

# async def search_phone_numbers(query, output_text, sender_number, message):
#     urls = []
#     for result in search(query, tld="co.in",num = 2, stop = 2, pause=2):
#         urls.append(result)

#     tasks = [asyncio.ensure_future(fetch(url)) for url in urls]
#     responses = await asyncio.gather(*tasks)

#     conn = sqlite3.connect('urlgetphonenumber.db')
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers
#                  (url TEXT, mobile_numbers TEXT, city_code TEXT)''')

#     c.execute('''CREATE TABLE IF NOT EXISTS cities
#                  (code TEXT, name TEXT)''')

#     api_key = input("Enter your Kavenegar API Key: ")

#     for i, response in enumerate(responses):
#         try:
#             phone_numbers = list(set(re.findall(r'\b(09\d{9})\b', response.text)))
#             domain = response.url.split('/')[2]
#             output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
#             output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")

#             city_numbers = list(set(re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)))
#             output_text.insert(tk.END, f"City numbers: {city_numbers}\n")

#             c.execute("INSERT INTO phone_numbers (url, mobile_numbers) VALUES (?, ?)",
#                     (response.url, ', '.join(phone_numbers)))

#             # Add city codes
#             city_codes = []
#             for city_number in city_numbers:
#                 city_code = city_number.split('-')[0]
#                 city_codes.append(city_code)

#                 # Check if city code already exists in cities table
#                 c.execute("SELECT code FROM cities WHERE code=?", (city_code,))
#                 result = c.fetchone()
#                 if result is None:
#                     city_name = input(f"Enter the name of the city with code {city_code}: ")
#                     c.execute("INSERT INTO cities (code, name) VALUES (?, ?)", (city_code, city_name))

#             c.execute("UPDATE phone_numbers SET city_code=? WHERE rowid=?", (', '.join(city_codes), i+1))

#             # Send SMS
#             for number in phone_numbers:
#                 payload = {
#                     'receptor': number,
#                     'message': message,
#                     'sender': sender_number
#                 }
#                 headers = {
#                     'apikey': api_key
#                 }
#                 response = requests.post(f'https://api.kavenegar.com/v1/{api_key}/sms/send.json', data=payload, headers=headers)
#                 print(response.json())
#         except:
#             print("e......2")
# root = tk.Tk()
# root.title("Phone Number Scraper")
# root.geometry("500x400")

# label = tk.Label(root, text="Enter search query:")
# label.grid(row=0, column=0)

# entry = tk.Entry(root)
# entry.grid(row=0, column=1)

# sender_label = tk.Label(root, text="Enter sender number:")
# sender_label.grid(row=1, column=0)

# sender_entry = tk.Entry(root)
# sender_entry.grid(row=1, column=1)

# message_label = tk.Label(root, text="Enter message:")
# message_label.grid(row=2, column=0)

# message_entry = tk.Entry(root)
# message_entry.grid(row=2, column=1)

# output_text = tk.Text(root)
# output_text.grid(row=3, columnspan=2)

# button = tk.Button(root, text="Search", command=lambda: asyncio.run(search_phone_numbers(entry.get(), output_text, sender_entry.get(), message_entry.get())))
# button.grid(row=4, columnspan=2)

# root.mainloop()



# =====================================


import asyncio
from googlesearch import search
import requests
import re
import sqlite3
import tkinter as tk
from tkinter import ttk

async def fetch(url):
    try:
        response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
        print(response, 11111111111)
        return response
    except:
        print("e......1")



async def search_phone_numbers(query, output_text, sender_number, message, api_key_entry):
    urls = []   
    for result in search(query, tld="co.in",num =10,stop =10, pause=2):
        urls.append(result)

    tasks = [asyncio.ensure_future(fetch(url)) for url in urls]
    responses = await asyncio.gather(*tasks)

    conn = sqlite3.connect('urlgetphonenumber.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS phone_numbers
                (url TEXT, mobile_numbers TEXT, city_code TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS cities
                (code TEXT, name TEXT)''')

    # api_key = input("Enter your Kavenegar API Key: ")

    for i, response in enumerate(responses):
        try:
            phone_numbers = list(set(re.findall(r'\b(09\d{9})\b', response.text)))
            domain = response.url.split('/')[2]
            output_text.insert(tk.END, f"Phone numbers for {domain}:\n")
            output_text.insert(tk.END, f"Mobile numbers: {phone_numbers}\n")

            city_numbers = list(set(re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)))
            output_text.insert(tk.END, f"City numbers: {city_numbers}\n")

            c.execute("INSERT INTO phone_numbers (url, mobile_numbers) VALUES (?, ?)",
                    (response.url, ', '.join(phone_numbers)))

            # # Add city codes
            # city_codes = []
            # for city_number in city_numbers:
            #     city_code = city_number.split('-')[0]
            #     city_codes.append(city_code)

                # Check if city code already exists in cities table
                # c.execute("SELECT code FROM cities WHERE code=?", (city_code,))
                # result = c.fetchone()
                # if result is None:
                #     city_name = input(f"Enter the name of the city with code {city_code}: ")
                #     c.execute("INSERT INTO cities (code, name) VALUES (?, ?)", (city_code, city_name))

            # c.execute("UPDATE phone_numbers SET city_code=? WHERE rowid=?", (', '.join(city_codes), i+1))

            # Send SMS
            try:
                for number in phone_numbers:
                    payload = {
                        'receptor': number,
                        'message': message.get("1.0", tk.END),
                        'sender': sender_number
                    }
                    
                    headers = {
                        'apikey': api_key_entry

                    }
                    response = requests.post(f'https://api.kavenegar.com/v1/{api_key_entry}/sms/send.json', data=payload, headers=headers)
                    print(response.json())
            except:
                print("e.......3")
        except:
            print("e.......2")

root = tk.Tk()
root.title("Phone Number Scraper")
root.geometry("643x800")

# تغییر رنگ پس زمینه به حالت تاریک
root.configure(bg="#222222")

# تغییر رنگ متن به سفید
root.tk_setPalette(background="#222222", foreground="white")

# تغییر رنگ المان‌های تکینتر
style = ttk.Style()
style.configure("TLabel", foreground="white", background="#222222")
style.configure("TEntry", foreground="black", background="#ffffff")
style.configure("TButton", foreground="white", background="#444444")
style.configure("TText", foreground="white", background="#333333")

label = ttk.Label(root, text="Enter search query:")
label.grid(row=0, column=0)
entry = ttk.Entry(root)
entry.grid(row=0, column=1)

sender_label = ttk.Label(root, text="Enter sender number:")
sender_label.grid(row=1, column=0)

sender_entry = ttk.Entry(root)
sender_entry.grid(row=1, column=1)

api_key_label = ttk.Label(root, text="Enter sender API:")
api_key_label.grid(row=2, column=0)

api_key_entry = ttk.Entry(root)
api_key_entry.grid(row=2, column=1)

message_label = ttk.Label(root, text="Enter message:")
message_label.grid(row=3, column=0)

message_entry = tk.Text(root, height=10, width=50)
message_entry.grid(row=3, column=1)

output_text = tk.Text(root)
output_text.grid(row=4, columnspan=4)

button = ttk.Button(root, text="Search", command=lambda: asyncio.run(search_phone_numbers(entry.get(), output_text, sender_entry.get(), message_entry.get, api_key_entry.get())))
button.grid(row=5, columnspan=3)

root.mainloop()



# from kavenegar import *
# api = KavenegarAPI('7344376363534F765236714345497948636635475956755A71355369785047506D50384D7569694C4D63343D')
# params = { 'sender' : '1000689696', 'receptor': '09304307827', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
# response = api.sms_send( params)