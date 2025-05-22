from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *

user_list = read_from_file("user.dat")


def load_data(person_list):
    person_list = read_from_file("user.dat")
    for row in table.get_children():
        table.delete(row)

    for person in user_list:
        table.insert("", END, values=person)


def reset_form():
    id.set(len(user_list) + 1)
    user_name.set("")
    password.set("")
    status.set(value=True)
    name.set("")
    family.set("")
    load_data(user_list)


def save_btn_click():
    person = (id.get(), user_name.get(), password.get(), status.get(), name.get(), family.get())
    errors = user_validator(person)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Person saved")
        user_list.append(person)
        write_to_file("user.dat", user_list)
        reset_form()


def table_select(x):
    selected_user = table.item(table.focus())["values"]
    if selected_user:
        id.set(selected_user[0])
        user_name.set(selected_user[1])
        password.set(selected_user[2])
        status.set(selected_user[3])
        name.set(selected_user[3])
        family.set(selected_user[3])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("Person Info")
window.geometry("900x350")

# Id
Label(window, text="Id").place(x=30, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=20)

# User Name
Label(window, text="User Name").place(x=30, y=60)
user_name = StringVar()
Entry(window, textvariable=user_name).place(x=100, y=60)

# Password
Label(window, text="Password").place(x=30, y=100)
password = StringVar()
Entry(window, textvariable=password).place(x=100, y=100)

# Status
Label(window, text="Status").place(x=30, y=140)
status = BooleanVar(value=True)
Entry(window, textvariable=status).place(x=100, y=140)

# Name
Label(window, text="Name").place(x=30, y=180)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=180)

# Family
Label(window, text="Family").place(x=30, y=220)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=220)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="User Name")
table.heading(3, text="Password")
table.heading(4, text="Status")
table.heading(4, text="Name")
table.heading(4, text="Family")

table.column(1, width=60)
table.column(2, width=120)
table.column(3, width=120)
table.column(4, width=120)
table.column(5, width=120)
table.column(6, width=120)


table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20, height=305)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=300)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=95, y=300)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=170, y=300)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=260, width=203)

reset_form()

window.mainloop()
