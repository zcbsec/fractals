#!/usr/bin/env python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.hi_there.bind("<Enter>", self.turn_red)

    def say_hi(self):
        print("hi there, everyone!")

    def turn_red(self, event):
        event.widget["activeforeground"] = "red"


root = tk.Tk()
app = Application(master=root)

app.master.title("My graphing application")




app.mainloop()




