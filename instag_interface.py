import tkinter as tk
from instag_bot import get_username_data

class interface(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.username_bar()
    
    def username_bar(self):
        #Labels
        tk.Label(self, text="Instagram Search Bot", font=("Comic Sans S",24),justify="center").grid(row="0",column="1", sticky="nswe", pady=50)
        tk.Label(self, text="Instagram Username:", font=("Comic Sans S",14)).grid(row="1",column="0", sticky="e", pady=50)
        
        #Entry
        self.username=tk.Entry(self, font=("Comic Sans S",14), bd="3", relief="sunken",width=30)
        self.username.grid(row="1",column="1")
        
        #Button
        tk.Button(self, text="Search",font=("Comic Sans S",14), width=14, height=2, command=lambda:get_username_data(self.username.get())).grid(row="2",column="1")
