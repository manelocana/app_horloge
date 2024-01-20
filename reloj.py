import time
import tkinter as tk

# ventana
root = tk.Tk()
root.title = "reloj"
root.geometry("300x100")
root.resizable(False, False)

# parametros ventana
hora =tk.Label(root, text="hora")
hora.config(bg="yellow", font=("Arial", 50))
hora.pack(pady=10)

def reloj():
    #sacamos hora con modulo time
    hora.config(text=time.strftime("%H:%M:%S"))
    # actualiza cada segundo
    hora.after(1000, reloj)

reloj()

root.mainloop()