import tkinter as tk
import database

database.connect()

window = tk.Tk()
window.title("HRMS - Employee Manager")

tk.Label(window, text="Name").grid(row=0, column=0)
tk.Label(window, text="Age").grid(row=0, column=2)
tk.Label(window, text="Gender").grid(row=1, column=0)
tk.Label(window, text="Department").grid(row=1, column=2)
tk.Label(window, text="Salary").grid(row=2, column=0)

name_text, age_text, gender_text, dept_text, salary_text = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
e1, e2, e3, e4, e5 = [tk.Entry(window, textvariable=v) for v in [name_text, age_text, gender_text, dept_text, salary_text]]
e1.grid(row=0, column=1); e2.grid(row=0, column=3)
e3.grid(row=1, column=1); e4.grid(row=1, column=3)
e5.grid(row=2, column=1)

list1 = tk.Listbox(window, height=8, width=60)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)

sb1 = tk.Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, tk.END); e1.insert(tk.END, selected_tuple[1])
    e2.delete(0, tk.END); e2.insert(tk.END, selected_tuple[2])
    e3.delete(0, tk.END); e3.insert(tk.END, selected_tuple[3])
    e4.delete(0, tk.END); e4.insert(tk.END, selected_tuple[4])
    e5.delete(0, tk.END); e5.insert(tk.END, selected_tuple[5])

list1.bind("<<ListboxSelect>>", get_selected_row)

def view_command():
    list1.delete(0, tk.END)
    for row in database.view():
        list1.insert(tk.END, row)

def add_command():
    database.insert(name_text.get(), age_text.get(), gender_text.get(), dept_text.get(), salary_text.get())
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], name_text.get(), age_text.get(), gender_text.get(), dept_text.get(), salary_text.get())
    view_command()

tk.Button(window, text="View All", width=12, command=view_command).grid(row=3, column=3)
tk.Button(window, text="Add", width=12, command=add_command).grid(row=4, column=3)
tk.Button(window, text="Update", width=12, command=update_command).grid(row=5, column=3)
tk.Button(window, text="Delete", width=12, command=delete_command).grid(row=6, column=3)
tk.Button(window, text="Close", width=12, command=window.destroy).grid(row=7, column=3)

window.mainloop()

# Ammar's Project 
