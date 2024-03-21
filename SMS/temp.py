import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
try:
    conn= sqlite3.connect('urlgetphonenumber.db')
    c = conn.cursor()
    c.execute(''' SELECT  phone_number FROM informations''')
    rows = c.fetchall()
    print(rows)
    # for row in rows:
    #     print(row)
except: pass

def main():
    window = Tk()
    window.config(bg="skyblue")
    message_entry =tk.Text(window, height=10, width=50)
    message_entry.pack()
    button = tk.Button(window, text="send", command=lambda:send_msg(message_entry) ) 
    button.pack()
    window.mainloop() 
    

def send_msg(message_entry):

    payload = {
                        'receptor': '+989059689236',
                        'message': message_entry.get("1.0", tk.END),
                        
                    }
    headers = {
        'API-KEY': '797931634D5A6F7A456A37484735762B6D43786830306E34726E363636694E51445A45502B5257335467593D'

    }
    API_KEY ='797931634D5A6F7A456A37484735762B6D43786830306E34726E363636694E51445A45502B5257335467593D'
    response = requests.post(f'https://api.kavenegar.com/v1/{API_KEY}/sms/send.json', data=payload, headers=headers)
    print(response.text)



if __name__ == '__main__':
    main()
