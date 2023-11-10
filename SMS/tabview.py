import customtkinter


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Get Phone")
        self.add("Send Message")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("Get Phone"))
        self.label.grid(row=4, column=0, padx=10, pady=10)