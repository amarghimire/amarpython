import tkinter as tk
from tkinter import filedialog
import pandas as pande

main_root = tk.Tk()
canvas_type = tk.Canvas(main_root, width=500, height=400, bg='gray')

canvas_type.pack()


def my_function():
    global df
    df = filedialog.askopenfilename()
    data = pande.read_excel(df)
    print(data)


my_button = tk.Button(text='Import Excel File Here',
                      command=my_function)

canvas_type.create_window(150, 150, window=my_button)

main_root.mainloop()