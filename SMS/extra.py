# # import tkinter as tk
# # from tkinter import messagebox
# # from tkinter import ttk
# # from signup import SignupPage

# # """
# # Useful Links:
# # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter Most useful in my opinion
# # https://www.tutorialspoint.com/python/python_gui_programming.htm
# # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
# # https://www.youtube.com/watch?v=HjNHATw6XgY&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk
# # """

# # # You can also use a pandas dataframe for pokemon_info.
# # # you can convert the dataframe using df.to_numpy.tolist()
# # pokemon_info = [['Bulbasaur', 'Grass', '318'], ['Ivysaur', 'Grass', '405'], ['Venusaur', 'Grass', '525'], ['Charmander', 'Fire', '309'], ['Charmeleon', 'Fire', '405'], ['Charizard', 'Fire', '534'], ['Squirtle', 'Water', '314'], ['Wartortle', 'Water', '405'], ['Blastoise', 'Water', '530'], ['Caterpie', 'Bug', '195'], ['Metapod', 'Bug', '205'], ['Butterfree', 'Bug', '395'], ['Weedle', 'Bug', '195'], ['Kakuna', 'Bug', '205'], ['Beedrill', 'Bug', '395'], ['Pidgey', 'Normal', '251'], ['Pidgeotto', 'Normal', '349'], ['Pidgeot', 'Normal', '479'], ['Rattata', 'Normal', '253'], ['Raticate', 'Normal', '413'], ['Spearow', 'Normal', '262'], ['Fearow', 'Normal', '442'], ['Ekans', 'Poison', '288'], ['Arbok', 'Poison', '448'], ['Pikachu', 'Electric', '320'], ['Raichu', 'Electric', '485'], ['Sandshrew', 'Ground', '300'], ['Sandslash', 'Ground', '450'], ['Nidoran?', 'Poison', '275'], ['Nidorina', 'Poison', '365'], ['Nidoqueen', 'Poison', '505'], ['Nidoran?', 'Poison', '273'], ['Nidorino', 'Poison', '365'], ['Nidoking', 'Poison', '505'], ['Clefairy', 'Fairy', '323'], ['Clefable', 'Fairy', '483'], ['Vulpix', 'Fire', '299'], ['Ninetales', 'Fire', '505'], ['Jigglypuff', 'Normal', '270'], ['Wigglytuff', 'Normal', '435'], ['Zubat', 'Poison', '245'], ['Golbat', 'Poison', '455'], ['Oddish', 'Grass', '320'], ['Gloom', 'Grass', '395'], ['Vileplume', 'Grass', '490'], ['Paras', 'Bug', '285'], ['Parasect', 'Bug', '405'], ['Venonat', 'Bug', '305'], ['Venomoth', 'Bug', '450'], ['Diglett', 'Ground', '265'], ['Dugtrio', 'Ground', '425'], ['Meowth', 'Normal', '290'], ['Persian', 'Normal', '440'], ['Psyduck', 'Water', '320'], ['Golduck', 'Water', '500'], ['Mankey', 'Fighting', '305'], ['Primeape', 'Fighting', '455'], ['Growlithe', 'Fire', '350'], ['Arcanine', 'Fire', '555'], ['Poliwag', 'Water', '300'], ['Poliwhirl', 'Water', '385'], ['Poliwrath', 'Water', '510'], ['Abra', 'Psychic', '310'], ['Kadabra', 'Psychic', '400'], ['Alakazam', 'Psychic', '500'], ['Machop', 'Fighting', '305'], ['Machoke', 'Fighting', '405'], ['Machamp', 'Fighting', '505'], ['Bellsprout', 'Grass', '300'], ['Weepinbell', 'Grass', '390'], ['Victreebel', 'Grass', '490'], ['Tentacool', 'Water', '335'], ['Tentacruel', 'Water', '515'], ['Geodude', 'Rock', '300'], ['Graveler', 'Rock', '390'], ['Golem', 'Rock', '495'], ['Ponyta', 'Fire', '410'], ['Rapidash', 'Fire', '500'], ['Slowpoke', 'Water', '315'], ['Slowbro', 'Water', '490'], ['Magnemite', 'Electric', '325'], ['Magneton', 'Electric', '465'], ["Farfetch'd", 'Normal', '377'], ['Doduo', 'Normal', '310'], ['Dodrio', 'Normal', '470'], ['Seel', 'Water', '325'], ['Dewgong', 'Water', '475'], ['Grimer', 'Poison', '325'], ['Muk', 'Poison', '500'], ['Shellder', 'Water', '305'], ['Cloyster', 'Water', '525'], ['Gastly', 'Ghost', '310'], ['Haunter', 'Ghost', '405'], ['Gengar', 'Ghost', '500'], ['Onix', 'Rock', '385'], ['Drowzee', 'Psychic', '328'], ['Hypno', 'Psychic', '483'], ['Krabby', 'Water', '325'], ['Kingler', 'Water', '475'], ['Voltorb', 'Electric', '330'], ['Electrode', 'Electric', '490'], ['Exeggcute', 'Grass', '325'], ['Exeggutor', 'Grass', '530'], ['Cubone', 'Ground', '320'], ['Marowak', 'Ground', '425'], ['Hitmonlee', 'Fighting', '455'], ['Hitmonchan', 'Fighting', '455'], ['Lickitung', 'Normal', '385'], ['Koffing', 'Poison', '340'], ['Weezing', 'Poison', '490'], ['Rhyhorn', 'Ground', '345'], ['Rhydon', 'Ground', '485'], ['Chansey', 'Normal', '450'], ['Tangela', 'Grass', '435'], ['Kangaskhan', 'Normal', '490'], ['Horsea', 'Water', '295'], ['Seadra', 'Water', '440'], ['Goldeen', 'Water', '320'], ['Seaking', 'Water', '450'], ['Staryu', 'Water', '340'], ['Starmie', 'Water', '520'], ['Scyther', 'Bug', '500'], ['Jynx', 'Ice', '455'], ['Electabuzz', 'Electric', '490'], ['Magmar', 'Fire', '495'], ['Pinsir', 'Bug', '500'], ['Tauros', 'Normal', '490'], ['Magikarp', 'Water', '200'], ['Gyarados', 'Water', '540'], ['Lapras', 'Water', '535'], ['Ditto', 'Normal', '288'], ['Eevee', 'Normal', '325'], ['Vaporeon', 'Water', '525'], ['Jolteon', 'Electric', '525'], ['Flareon', 'Fire', '525'], ['Porygon', 'Normal', '395'], ['Omanyte', 'Rock', '355'], ['Omastar', 'Rock', '495'], ['Kabuto', 'Rock', '355'], ['Kabutops', 'Rock', '495'], ['Aerodactyl', 'Rock', '515'], ['Snorlax', 'Normal', '540'], ['Articuno', 'Ice', '580'], ['Zapdos', 'Electric', '580'], ['Moltres', 'Fire', '580'], ['Dratini', 'Dragon', '300'], ['Dragonair', 'Dragon', '420'], ['Dragonite', 'Dragon', '600'], ['Mewtwo', 'Psychic', '680'], ['Mew', 'Psychic', '600']]


# # frame_styles = {"relief": "groove",
# #                 "bd": 3, "bg": "#BEB2A7",
# #                 "fg": "#073bb3", "font": ("Arial", 9, "bold")}


# # class LoginPage(tk.Tk):

# #     def __init__(self, *args, **kwargs):

# #         tk.Tk.__init__(self, *args, **kwargs)

# #         main_frame = tk.Frame(self, bg="#708090", height=431, width=626)  # this is the background
# #         main_frame.pack(fill="both", expand="true")

# #         self.geometry("626x431")  # Sets window size to 626w x 431h pixels
# #         self.resizable(0, 0)  # This prevents any resizing of the screen
# #         title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

# #         text_styles = {"font": ("Verdana", 14),
# #                        "background": "blue",
# #                        "foreground": "#E1FFFF"}

# #         frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
# #         frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

# #         label_title = tk.Label(frame_login, title_styles, text="Login Page")
# #         label_title.grid(row=0, column=1, columnspan=1)

# #         label_user = tk.Label(frame_login, text_styles, text="Username:")
# #         label_user.grid(row=1, column=0)

# #         label_pw = tk.Label(frame_login, text_styles, text="Password:")
# #         label_pw.grid(row=2, column=0)

# #         entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
# #         entry_user.grid(row=1, column=1)

# #         entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
# #         entry_pw.grid(row=2, column=1)

# #         button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
# #         button.place(rely=0.70, relx=0.50)

# #         signup_btn = ttk.Button(frame_login, text="Register", command=lambda: get_signup())
# #         signup_btn.place(rely=0.70, relx=0.75)

# #         def get_signup():
# #             SignupPage()

# #         def getlogin():
# #             username = entry_user.get()
# #             password = entry_pw.get()
# #             # if your want to run the script as it is set validation = True
# #             validation = validate(username, password)
# #             if validation:
# #                 tk.messagebox.showinfo("Login Successful",
# #                                        "Welcome {}".format(username))
# #                 root.deiconify()
# #                 top.destroy()
# #             else:
# #                 tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")

# #         def validate(username, password):
# #             # Checks the text file for a username/password combination.
# #             try:
# #                 with open("credentials.txt", "r") as credentials:
# #                     for line in credentials:
# #                         line = line.split(",")
# #                         if line[1] == username and line[3] == password:
# #                             return True
# #                     return False
# #             except FileNotFoundError:
# #                 print("You need to Register first or amend Line 71 to     if True:")
# #                 return False

# # class MenuBar(tk.Menu):
# #     def __init__(self, parent):
# #         tk.Menu.__init__(self, parent)

# #         menu_file = tk.Menu(self, tearoff=0)
# #         self.add_cascade(label="Menu1", menu=menu_file)
# #         menu_file.add_command(label="All Widgets", command=lambda: parent.show_frame(Some_Widgets))
# #         menu_file.add_separator()
# #         menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())

# #         menu_orders = tk.Menu(self, tearoff=0)
# #         self.add_cascade(label="Menu2", menu=menu_orders)

# #         menu_pricing = tk.Menu(self, tearoff=0)
# #         self.add_cascade(label="Menu3", menu=menu_pricing)
# #         menu_pricing.add_command(label="Page One", command=lambda: parent.show_frame(PageOne))

# #         menu_operations = tk.Menu(self, tearoff=0)
# #         self.add_cascade(label="Menu4", menu=menu_operations)
# #         menu_operations.add_command(label="Page Two", command=lambda: parent.show_frame(PageTwo))
# #         menu_positions = tk.Menu(menu_operations, tearoff=0)
# #         menu_operations.add_cascade(label="Menu5", menu=menu_positions)
# #         menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
# #         menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

# #         menu_help = tk.Menu(self, tearoff=0)
# #         self.add_cascade(label="Menu6", menu=menu_help)
# #         menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())


# # class MyApp(tk.Tk):

# #     def __init__(self, *args, **kwargs):

# #         tk.Tk.__init__(self, *args, **kwargs)
# #         main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
# #         main_frame.pack_propagate(0)
# #         main_frame.pack(fill="both", expand="true")
# #         main_frame.grid_rowconfigure(0, weight=1)
# #         main_frame.grid_columnconfigure(0, weight=1)
# #         # self.resizable(0, 0) prevents the app from being resized
# #         # self.geometry("1024x600") fixes the applications size
# #         self.frames = {}
# #         pages = (Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
# #         for F in pages:
# #             frame = F(main_frame, self)
# #             self.frames[F] = frame
# #             frame.grid(row=0, column=0, sticky="nsew")
# #         self.show_frame(Some_Widgets)
# #         menubar = MenuBar(self)
# #         tk.Tk.config(self, menu=menubar)

# #     def show_frame(self, name):
# #         frame = self.frames[name]
# #         frame.tkraise()

# #     def OpenNewWindow(self):
# #         OpenNewWindow()

# #     def Quit_application(self):
# #         self.destroy()


# # class GUI(tk.Frame):
# #     def __init__(self, parent):
# #         tk.Frame.__init__(self, parent)
# #         self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
# #         # self.main_frame.pack_propagate(0)
# #         self.main_frame.pack(fill="both", expand="true")
# #         self.main_frame.grid_rowconfigure(0, weight=1)
# #         self.main_frame.grid_columnconfigure(0, weight=1)


# # class Some_Widgets(GUI):  # inherits from the GUI class
# #     def __init__(self, parent, controller):
# #         GUI.__init__(self, parent)

# #         frame1 = tk.LabelFrame(self, frame_styles, text="This is a LabelFrame containing a Treeview")
# #         frame1.place(rely=0.05, relx=0.02, height=400, width=400)

# #         frame2 = tk.LabelFrame(self, frame_styles, text="Some widgets")
# #         frame2.place(rely=0.05, relx=0.45, height=500, width=500)

# #         button1 = tk.Button(frame2, text="tk button", command=lambda: Refresh_data())
# #         button1.pack()
# #         button2 = ttk.Button(frame2, text="ttk button", command=lambda: Refresh_data())
# #         button2.pack()

# #         Var1 = tk.IntVar()
# #         Var2 = tk.IntVar()
# #         Cbutton1 = tk.Checkbutton(frame2, text="tk CheckButton1", variable=Var1, onvalue=1, offvalue=0)
# #         Cbutton1.pack()
# #         Cbutton2 = tk.Checkbutton(frame2, text="tk CheckButton2", variable=Var2, onvalue=1, offvalue=0)
# #         Cbutton2.pack()

# #         Cbutton3 = ttk.Checkbutton(frame2, text="ttk CheckButton1", variable=Var1, onvalue=1, offvalue=0)
# #         Cbutton3.pack()
# #         Cbutton3 = ttk.Checkbutton(frame2, text="ttk CheckButton2", variable=Var2, onvalue=1, offvalue=0)
# #         Cbutton3.pack()

# #         Lbox1 = tk.Listbox(frame2, selectmode="multiple")
# #         Lbox1.insert(1, "This is a tk ListBox")
# #         Lbox1.insert(2, "Github")
# #         Lbox1.insert(3, "Python")
# #         Lbox1.insert(3, "StackOverflow")
# #         Lbox1.pack(side="left")

# #         Var3 = tk.IntVar()
# #         R1 = tk.Radiobutton(frame2, text="tk Radiobutton1", variable=Var3, value=1)
# #         R1.pack()
# #         R2 = tk.Radiobutton(frame2, text="tk Radiobutton2", variable=Var3, value=2)
# #         R2.pack()
# #         R3 = tk.Radiobutton(frame2, text="tk Radiobutton3", variable=Var3, value=3)
# #         R3.pack()

# #         R4 = tk.Radiobutton(frame2, text="ttk Radiobutton1", variable=Var3, value=1)
# #         R4.pack()
# #         R5 = tk.Radiobutton(frame2, text="ttk Radiobutton2", variable=Var3, value=2)
# #         R5.pack()
# #         R6 = tk.Radiobutton(frame2, text="ttk Radiobutton3", variable=Var3, value=3)
# #         R6.pack()

# #         # This is a treeview.
# #         tv1 = ttk.Treeview(frame1)
# #         column_list_account = ["Name", "Type", "Base Stat Total"]
# #         tv1['columns'] = column_list_account
# #         tv1["show"] = "headings"  # removes empty column
# #         for column in column_list_account:
# #             tv1.heading(column, text=column)
# #             tv1.column(column, width=50)
# #         tv1.place(relheight=1, relwidth=0.995)
# #         treescroll = tk.Scrollbar(frame1)
# #         treescroll.configure(command=tv1.yview)
# #         tv1.configure(yscrollcommand=treescroll.set)
# #         treescroll.pack(side="right", fill="y")

# #         def Load_data():
# #             for row in pokemon_info:
# #                 tv1.insert("", "end", values=row)

# #         def Refresh_data():
# #             # Deletes the data in the current treeview and reinserts it.
# #             tv1.delete(*tv1.get_children())  # *=splat operator
# #             Load_data()

# #         Load_data()


# # class PageOne(GUI):
# #     def __init__(self, parent, controller):
# #         GUI.__init__(self, parent)

# #         label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
# #         label1.pack(side="top")


# # class PageThree(GUI):
# #     def __init__(self, parent, controller):
# #         GUI.__init__(self, parent)

# #         label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Three")
# #         label1.pack(side="top")


# # class PageFour(GUI):
# #     def __init__(self, parent, controller):
# #         GUI.__init__(self, parent)

# #         label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Four")
# #         label1.pack(side="top")


# # class PageTwo(GUI):
# #     def __init__(self, parent, controller):
# #         GUI.__init__(self, parent)

# #         label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Two")
# #         label1.pack(side="top")


# # class OpenNewWindow(tk.Tk):

# #     def __init__(self, *args, **kwargs):

# #         tk.Tk.__init__(self, *args, **kwargs)

# #         main_frame = tk.Frame(self)
# #         main_frame.pack_propagate(0)
# #         main_frame.pack(fill="both", expand="true")
# #         main_frame.grid_rowconfigure(0, weight=1)
# #         main_frame.grid_columnconfigure(0, weight=1)
# #         self.title("Here is the Title of the Window")
# #         self.geometry("500x500")
# #         self.resizable(0, 0)

# #         frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
# #         frame1.pack(expand=True, fill="both")

# #         label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
# #         label1.pack(side="top")


# # top = LoginPage()
# # top.title("Tkinter App Template - Login Page")
# # root = MyApp()
# # root.withdraw()
# # root.title("Tkinter App Template")

# # root.mainloop()
# ###############################################