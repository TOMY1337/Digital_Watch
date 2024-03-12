import tkinter as tk
import time

root = tk.Tk()
root.title('Digital Watch')
root.geometry('200x100')
root.config(bg='#000000')

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time, bg='#000000')
    root.after(1000, update_time) 
    

time_label = tk.Label(root, font=('Arial', 32, 'bold'), fg='#F3FA05')
time_label.pack(pady=20)

update_time()

root.mainloop()