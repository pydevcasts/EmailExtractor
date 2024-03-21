# import tkinter.messagebox
# import customtkinter
# import re
# import sqlite3
# import asyncio
# import requests
# import tkinter.messagebox
# from PIL import Image, ImageTk
# from googlesearch import search
# from cleardata import clearData

# # customtkinter.ScalingTracker.set_user_scaling(0.5)
# customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# class App(customtkinter.CTk):
#     WIDTH = 780
#     HEIGHT = 520

#     def __init__(self):
#         super().__init__()

#         self.title("📋")
#         self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
#         self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

#         # ============ create two frames ============

#         # configure grid layout (2x1)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         self.frame_left = customtkinter.CTkFrame(master=self,
#                                                  width=180,
#                                                  corner_radius=0)
#         self.frame_left.grid(row=0, column=0, sticky="nswe")

#         self.frame_right = customtkinter.CTkFrame(master=self)
#         self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

#         # ============ frame_left ============

#         # configure grid layout (1x11)
#         self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
#         self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
#         self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
#         self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

#         self.button_1 = customtkinter.CTkButton(master=self.frame_left,
#                                                 text=" CTkButton",
#                                                 fg_color=("gray75", "gray30"))  # <- custom tuple-color
#         self.button_1.grid(row=2, column=0, pady=10, padx=20)

#         self.my_image = customtkinter.CTkImage(light_image=Image.open("guigit.py/Sales-and-Inventory-Management-System/images/my_profile.png"),
#                                                dark_image=Image.open("guigit.py/Sales-and-Inventory-Management-System/images/my_profile.png"),
#                                                size=(30, 30))

#         self.image_label = customtkinter.CTkLabel(master=self.frame_left, image=self.my_image, text="")  # display image with a CTkLabel
#         self.image_label.grid(row=1, column=0, pady=10, padx=10)
#         self.button_2 = customtkinter.CTkButton(master=self.frame_left,
#                                                 text=" Database",
#                                                 fg_color=("red", "red"),  # <- custom tuple-color
#                                                 command=lambda: asyncio.run(clearData())
#                                                 )
#         self.button_2.grid(row=3, column=0, pady=10, padx=20)

#         self.switch = customtkinter.CTkSwitch(master=self.frame_left,
#                                               text="Dark Mode",
#                                               command=self.change_mode)
#         self.switch.grid(row=10, column=0, pady=10, padx=20, sticky="w")

#         # ============ frame_right ============

#         # configure grid layout (3x7)
#         self.frame_right.rowconfigure((0, 1, 2, 3), weight=0)
#         self.frame_right.rowconfigure(7, weight=10)
#         self.frame_right.columnconfigure((0, 1), weight=1)
#         self.frame_right.columnconfigure(2, weight=0)

#         self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
#         self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

#         # ============ frame_info ============

#         # configure grid layout (1x1)
#         self.frame_info.rowconfigure(0, weight=1)
#         self.frame_info.columnconfigure(0, weight=1)
#         self.output_text = customtkinter.CTkTextbox(master=self.frame_info,
#                                                     fg_color=("white", "gray20"),
#                                                     )
#         self.output_text.grid(row=0, column=0, sticky="nwe", padx=15, pady=15)

#         # ============ frame_right ============

#         self.radio_var = tkinter.IntVar(value=0)

#         self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
#                                                          text="CTkRadioButton Group:")
#         self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

#         self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
#                                                             variable=self.radio_var,
#                                                             value=0)
#         self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

#         self.progressbar = customtkinter.CTkProgressBar(master=self.frame_right,
#                                                          orientation="horizontal")

#         self.entry = customtkinter.CTkEntry(master=self.frame_right,
#                                             width=120,
#                                             text_color="white",
#                                             placeholder_text="Search ...",
#                                             )
#         self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

#         self.button_5 = customtkinter.CTkButton(master=self.frame_right,
#                                                 text=" ◀",
#                                                 command=lambda: self.button_event(self.entry, self.output_text))
#         self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

#         # set default values
#         self.radio_button_1.select()
#         self.switch.select()

#         # ===============sqlite3 connect ============

#         self.conn = sqlite3.connect('SMS/sqlite.db')
#         self.c = self.conn.cursor()
#         self.c.execute('''
#             CREATE TABLE IF NOT EXISTS phone_numbers
#             (url TEXT, mobile_numbers TEXT, city_numbers TEXT)
#             ''')
#         # ======================================================

#     async def fetch(self, url):
#         try:
#             response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
#             return response
#         except Exception as err:
#             print(f"error goes to :{err}")

#     async def search_phone_numbers(self, query, output_text=None):
#         self.progressbar.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="nwe")  # اضافه شده
#         self.progressbar.start()  
#         urls = [result for result in search(query, tld="co.in", num=5)]
#         tasks = [asyncio.ensure_future(self.fetch(url)) for url in urls]
#         total_urls = len(urls)
#         for i, response in enumerate(await asyncio.gather(*tasks)):
#             try:
#                 phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#                 city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#                 phone_numbers = list(set(phone_numbers))
#                 city_numbers = list(set(city_numbers))
#                 domain = response.url.split('/')[2]
#                 self.output_text.insert("0.0", f"\u2714 Name Domain is: {domain}\n")
#                 self.output_text.insert("0.0", f"\u2714 Mobile numbers: {phone_numbers}\n")
#                 self.output_text.insert("0.0", f"\u2714 City numbers: {city_numbers}\n============================\n")
#                 self.c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)",
#                                (response.url, ', '.join(phone_numbers), ', '.join(city_numbers)))
#             except Exception as err:
#                 print(f"Text erorr goes to {err}")
#             progress_value = (i + 1) / total_urls  # محاسبه مقدار پیشرفت
#             self.progressbar.step(progress_value * 100)  # تنظیم مقدار پیشرفت به صورت درصدی
#             self.progressbar.update()  # به‌روز‌رسانی ProgressBar
#             await asyncio.sleep(1)
#         print("END")
#         self.progressbar.stop()  # متوقف کردن نوار پیشرفت
#         self.conn.commit()
#         self.conn.close()

#     def button_event(self, query, output_text):
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(self.search_phone_numbers(query.get(), output_text))

#     def change_mode(self):
#         if self.switch.get() == 1:
#             customtkinter.set_appearance_mode("dark")
#         else:
#             customtkinter.set_appearance_mode("light")

#     def on_closing(self, event=0):
#         self.destroy()

#     def start(self):
#         self.mainloop()


# if __name__ == "__main__":
#     app = App()
#     app.start()
########################################################333
# import tkinter as tk
# import customtkinter
# import re
# import sqlite3
# import asyncio
# import requests
# from PIL import Image
# from googlesearch import search
# from cleardata import clearData
# from tabview import MyTabOneView, MyTabTwoView

# # customtkinter.ScalingTracker.set_user_scaling(0.5)
# customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# class App(customtkinter.CTk):
#     WIDTH = 780
#     HEIGHT = 520

#     def __init__(self):
#         super().__init__()

#         self.title("📋")
#         self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
#         self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
#         # ============ create two frames ============
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=1)
#         self.frame_left = customtkinter.CTkFrame(master=self,
#                                                  width=180,
#                                                  corner_radius=0)
#         self.frame_left.grid(row=0, column=0, sticky="nswe")
#         self.frame_right = customtkinter.CTkFrame(master=self)
#         self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
#         # ============ frame_left ============
#         self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
#         self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
#         self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
#         self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

#         self.my_image = customtkinter.CTkImage(light_image=Image.open("SMS/image/icons8-phone-book-48.png"),
#                                                dark_image=Image.open("SMS/image/icons8-phone-book-48.png"),
#                                                size=(30, 30))
#         self.image_label = customtkinter.CTkLabel(master=self.frame_left, image=self.my_image, text="")  # display image with a CTkLabel
#         self.image_label.grid(row=1, column=0, pady=10, padx=10)

#         self.button_1 = customtkinter.CTkButton(master=self.frame_left,text=" phone",fg_color=("gray75", "gray30"),command=self.show_tab_1_content)  # <- custom tuple-color
#         self.button_1.grid(row=2, column=0, pady=10, padx=10)
#         self.button_2 = customtkinter.CTkButton(master=self.frame_left,text="message",fg_color=("gray75", "gray30"),command=self.show_tab_2_content)
#         self.button_2.grid(row=3, column=0, pady=10, padx=20)


#         self.rm_db = customtkinter.CTkImage(light_image=Image.open("SMS/image/icons8-delete-database-20.png"),
#                                                dark_image=Image.open("SMS/image/icons8-delete-database-20.png"),
#                                                size=(25, 25))
#         self.rm_db_label = customtkinter.CTkLabel(master=self.frame_left, image=self.rm_db, text="")  # display image with a CTkLabel
#         self.rm_db_label.grid(row=4, column=0, pady=10, padx=10)
#         self.button_3 = customtkinter.CTkButton(master=self.frame_left, image=self.rm_db,text="",fg_color=("gray75", "gray30"),command=lambda: asyncio.run(clearData()))
#         self.button_3.grid(row=4, column=0, pady=10, padx=20)
        

#         self.switch = customtkinter.CTkSwitch(master=self.frame_left,
#                                               text="Dark Mode",
#                                               command=self.change_mode)
#         self.switch.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        
#         # ============ frame_right ============

#         # configure grid layout (3x7)
#         self.frame_right.rowconfigure((0, 1, 2, 3), weight=0)
#         self.frame_right.rowconfigure(7, weight=10)
#         self.frame_right.columnconfigure((0, 1), weight=1)
#         self.frame_right.columnconfigure(2, weight=0)
#         self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
#         self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        
#         # ============ frame_info ============

#         self.frame_info.rowconfigure(0, weight=1)
#         self.frame_info.columnconfigure(0, weight=1)
#         self.output_text = customtkinter.CTkTextbox(master=self.frame_info,
#                                                     fg_color=("white", "gray20"),
#                                                     )
#         self.output_text.grid(row=0, column=0, sticky="nwe", padx=15, pady=15)

#         # ============ frame_right ============
#         self.progressbar = customtkinter.CTkProgressBar(master=self.frame_right,
#                                                          orientation="horizontal")
#         self.entry = customtkinter.CTkEntry(master=self.frame_right,
#                                             width=120,
#                                             text_color=("gray20", "white"),
#                                             placeholder_text="Search ...",
#                                             )
#         self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

#         self.button_5 = customtkinter.CTkButton(master=self.frame_right,
#                                                 text=" ◀",
#                                                 command=lambda: self.button_event(self.entry, self.output_text))
#         self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

#         # set default values
  
#         self.switch.select()
        
#         # ===============sqlite3 connect ============

#         self.conn = sqlite3.connect('SMS/sqlite.db')
#         self.c = self.conn.cursor()
#         self.c.execute('''
#             CREATE TABLE IF NOT EXISTS phone_numbers
#             (url TEXT, mobile_numbers TEXT, city_numbers TEXT)
#             ''')
#         # ======================================================
#     def show_tab_1_content(self):
#         self.tab_view = MyTabOneView(master=self.frame_right)
#         self.tab_view.grid(row=0, column=1, padx=20, pady=20)
    
#     def show_tab_2_content(self):
#         self.tab_view = MyTabTwoView(master=self.frame_right)
#         self.tab_view.grid(row=1, column=1, padx=20, pady=20)
    
#     async def fetch(self, url):
#         try:
#             response = await asyncio.wait_for(asyncio.get_event_loop().run_in_executor(None, requests.get, url), timeout=10)
#             return response
#         except asyncio.TimeoutError:
#             print(f"Timeout occurred for URL: {url}")
#             return None
#         except Exception as err:
#             print(f"Error for URL {url}: {err}")
#             return None


#     async def search_phone_numbers(self, query, output_text=None):
#         self.progressbar.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="nwe")  # اضافه شده
#         self.progressbar.start()
        
#         urls = [result for result in search(query, tld="co.in", num=2)]
#         tasks = [asyncio.ensure_future(self.fetch(url)) for url in urls]
#         total_urls = len(urls)
#         for i, response in enumerate(await asyncio.gather(*tasks)):
#             try:
#                 phone_numbers = re.findall(r'\b(09\d{9})\b', response.text)
#                 city_numbers = re.findall(r'\b(0\d{2,3}-\d{7,8})\b', response.text)
#                 phone_numbers = list(set(phone_numbers))
#                 city_numbers = list(set(city_numbers))
#                 domain = response.url.split('/')[2]
#                 self.output_text.insert("0.0", f"\u2714 Name Domain is: {domain}\n")
#                 self.output_text.insert("0.0", f"\u2714 Mobile numbers: {phone_numbers}\n")
#                 self.output_text.insert("0.0", f"\u2714 City numbers: {city_numbers}\n============================\n")
#                 self.c.execute("INSERT INTO phone_numbers (url, mobile_numbers, city_numbers) VALUES (?, ?, ?)",
#                                (response.url, ', '.join(phone_numbers), ', '.join(city_numbers)))
#             except Exception as err:
#                 print(f"Text erorr goes to {err}")
#             progress_value = (i + 1) / total_urls  # محاسبه مقدار پیشرفت
#             self.progressbar.set(progress_value * 100)
#             self.progressbar.update()  # به‌روز‌رسانی ProgressBar
#             await asyncio.sleep(1)
#         print("END")
#         self.progressbar.stop()  # متوقف کردن نوار پیشرفت
#         self.conn.commit()
#         self.conn.close()
#         tk.messagebox.showinfo(title=None, message="جستجوی شماره‌های تلفن با موفقیت انجام شد!") # نمایش پیام اطلاعات پس از پایان عملیات
         

#     def button_event(self, query, output_text):
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(self.search_phone_numbers(query.get(), output_text))

#     def change_mode(self):
#         if self.switch.get() == 1:
#             customtkinter.set_appearance_mode("dark")
#         else:
#             customtkinter.set_appearance_mode("light")

#     def on_closing(self, event=0):
#         self.destroy()

#     def start(self):
#         self.mainloop()


# if __name__ == "__main__":
#     asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())  # برای همه‌ی سیستم‌ها
#     app = App()
#     app.start()
   



