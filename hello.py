import tkinter as tk

class Application:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.button = tk.Button(
                self.frame, 
                text="QUIT",
                fg="red",
                command=self.frame.quit
        )
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(self.frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.TOP)


    def say_hi(self):
        print("Hello")


root = tk.Tk()
app = Application(root)

root.mainloop()
root.destroy()
