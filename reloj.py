import time, datetime
import tkinter as tk


root = tk.Tk()
root.title = "reloj"
root.geometry("400x200")


hora =tk.Label(root, text="hora")
hora.config(bg="yellow", font=("Arial", 40))
hora.pack()


def reloj():
 
    hora.config(text=time.strftime("%H:%M:%S"))
    hora.after(1000, reloj)

    


reloj()


root.mainloop()
