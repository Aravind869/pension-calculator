from tkinter import *
import tkinter.messagebox as MessageBox
import database


def Calculate():
    bp = int(e_id.get())
    serv = int(e_service.get())
    total = (bp * serv * 12 * (70 / 3000))
    commute = (bp * serv * 12 * (70 / 3000)) * (0.03)
    total.delete(0, END)
    total.insert(END, total)
    e_commute.delete(0, END)
    e_commute.insert(END, commute)
    return total, commute


def save():
    name = str(e_name.get())
    age = int(e_age.get())
    basic = int(e_id.get())
    avg = int(e_avgsal.get())
    ser = int(e_service.get())
    total, commute = Calculate()
    database.insert(name, age, basic, avg, ser, total, commute)
    view_command()


def get_selected_row(event):
    global selected_tuple
    index = listBox.curselection()[0]
    selected_tuple = listBox.get(index)
    e_name.delete(0, END)
    e_name.insert(END, selected_tuple[1])
    e_age.delete(0, END)
    e_age.insert(END, selected_tuple[2])
    e_id.delete(0, END)
    e_id.insert(END, selected_tuple[3])
    e_avgsal.delete(0, END)
    e_avgsal.insert(END, selected_tuple[4])
    e_service.delete(0, END)
    e_service.insert(END, selected_tuple[5])
    total.delete(0, END)
    total.insert(END, selected_tuple[6])
    e_commute.delete(0, END)
    e_commute.insert(END, selected_tuple[7])


def view_command():
    listBox.delete(0, END)
    for rows in database.views():
        listBox.insert(END, rows)


def delete_command():
    database.delete(selected_tuple[0])
    view_command()
    reset()


def reset():
    e_name.delete(0, END)
    e_age.delete(0, END)
    e_id.delete(0, END)
    e_avgsal.delete(0, END)
    e_service.delete(0, END)
    total.delete(0, END)
    e_commute.delete(0, END)


root = Tk()
root.geometry("700x600")
root.title("Python+Tkinter+MySql")

title = Label(root, text='Pension Caluclator', font=('bold', 20))
title.place(x=180, y=15)

id = Label(root, text='Enter Basic Pay', font=('bold', 10))
id.place(x=20, y=60)

name = Label(root, text='Enter Name', font=('bold', 10))
name.place(x=20, y=90)

age = Label(root, text='Enter Age', font=('bold', 10))
age.place(x=20, y=120)

gender = Label(root, text='Enter Avg Sal(Last 12 Months)', font=('bold', 10))
gender.place(x=20, y=150)

service = Label(root, text='Enter total service years', font=('bold', 10))
service.place(x=20, y=180)

e_id = Entry()
e_id.place(x=200, y=60)

e_name = Entry()
e_name.place(x=200, y=90)

e_age = Entry()
e_age.place(x=200, y=120)

e_avgsal = Entry()
e_avgsal.place(x=200, y=150)

e_service = Entry()
e_service.place(x=200, y=180)

total = Entry()
total.place(x=200, y=280)

e_commute = Entry()
e_commute.place(x=200, y=310)

Button(text="Caluclate", font="bold 10", command=Calculate).place(x=180, y=230)
Button(text="Save", font="bold 10", command=save).place(x=250, y=230)
Button(text="delete", font="bold 10", command=delete_command).place(x=300, y=230)
Button(text="view All", font="bold 10", command=view_command).place(x=350, y=230)
Button(text="close", font="bold 10", command=root.destroy).place(x=420, y=230)
Button(text="reset", font="bold 10", command=reset).place(x=420, y=230)
pension = Label(root, text="Total Pension :", font="bold 10")
pension.place(x=20, y=280)

commute = Label(root, text="Total Commutation :", font="bold 10")
commute.place(x=20, y=310)

listBox = Listbox(root, height=10, width=50)
listBox.place(x=20, y=350)

sb1 = Scrollbar(root)
sb1.grid(row=2, column=3, rowspan=6)
listBox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listBox.yview)
listBox.bind("<<ListboxSelect>>", get_selected_row)
view_command()

"""insert = Button(root, text"insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=200)

delete = Button(root, text"delete", font=("italic", 10), bg="white", command=insert)
delete.place(x=70, y=200)

update = Button(root, text"update", font=("italic", 10), bg="white", command=insert)
update.place(x=120, y=200)

get = Button(root, text"get", font=("italic", 10), bg="white", command=insert)
get.place(x=170, y=200)"""

root.mainloop()
