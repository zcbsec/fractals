import tkinter as tk


master = tk.Tk()

w = tk.Canvas(master, width=800,height=800)
w.pack()


def pset(x,y):
    w.create_line(x+400,y+400,x+401,y+401)



A = .8
B = 1.2
C= 2 - (1.28 * A)
P= 12000

X = .35 
Y = 200

W = A*X + C*X*X / (1+X*X)

for n in range(P):
    if n > 100:
        pset(X,Y)
    Z = X
    X = B*Y + W
    U = X*X
    W = A* X + C*U / (1+U)
    Y = W - Z



tk.mainloop()
