# Designing a program that converts degrees celsius to fahrenheit
# and vice versa

import tkinter as tk
import tkinter.ttk as ttk
import Code as cd
import tkinter.messagebox as messagebox


# Creating a window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("620x300")
window.resizable(0, 0)

# Creating a label and entry to insert temperature
temp_label = tk.Label(window, text="Enter Temperature:")
temp_label.grid(row=0, column=0, pady=20, padx=50)
temperature = tk.StringVar()
temp_ent = ttk.Entry(window, width=20, textvariable=temperature)
temp_ent.grid(row=0, column=1)
temp_ent.focus_get()

# Creating a label and menu to choose which unit to convert from
unit_label = tk.Label(window, text="Select a unit: ", )
unit_label.grid(row=1, column=0)
unit = tk.StringVar()
unit_box = ttk.Combobox(window, width=20, textvariable=unit, state="readonly")
unit_box["values"] = "Celsius, Fahrenheit"
unit_box.current(0)
unit_box.grid(row=1, column=1)

# Creating a menu to choose which unit to convert to
unit1 = tk.StringVar()
unit_box1 = ttk.Combobox(window, width=20, textvariable=unit1, state="readonly")
unit_box1["values"] = "Celsius Fahrenheit"
unit_box1.current(1)
unit_box1.grid(row=2, column=1, padx=50, pady=20)

# Creating an answer box
answer_label = tk.Label(window, text="Answer:")
answer_label.grid(row=3, column=0)


# Defining functions for the buttons below
def convert():
    try:
        if len(temperature.get()) < 8:
            ans = cd.temperature_converter(int(temperature.get()), unit.get(), unit1.get())
            global ans_frame
            ans_frame = tk.Frame(window, width=50, height=50)
            ans_frame.grid(row=3, column=1)
            win = tk.Label(ans_frame, text=f"{round(ans)} {unit1.get()}")
            win.grid(row=0, column=0)
        else:
            messagebox.showerror("Input Error", "Limit Of Entry is 7")
    except:
        messagebox.showerror("Input Error", "Enter A Number")


def clear():
    ans_frame.destroy()


def exit():
    window.destroy()


convert_btn = ttk.Button(window, text="Convert", command=convert)
convert_btn.grid(row=3, column=2)


clear_btn = ttk.Button(window, text="Clear", command=clear)
clear_btn.grid(row=4, column=2)


exit_btn = ttk.Button(window, text="Exit", command=exit)
exit_btn.grid(row=5, column=2)


window.mainloop()
