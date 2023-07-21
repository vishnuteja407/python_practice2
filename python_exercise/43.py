import tkinter

window = tkinter.Tk()

window.title("Data Entry")

data = []

def add_line():
    line = line_entry.get()
    data.append(line)
    line_entry.delete(0,"end")

def save_changes():
    add_line()
    with open("user_gui.txt","a+") as gui_data:
        for val in data:
            gui_data.write(val+"\n")
    data.clear()

def save_and_close():
    save_changes()
    window.destroy()

frame = tkinter.Frame(window)
frame.pack()

line_entry = tkinter.Entry(frame)
line_entry.grid(row=0, column=0)

button = tkinter.Button(frame, text="Add Line", command=add_line)
button.grid(row=0, column=1)

button = tkinter.Button(frame, text="Save Changes", command=save_changes)
button.grid(row=0, column=2)

button = tkinter.Button(frame, text="Save and Close", command=save_and_close)
button.grid(row=0, column=3)
for widget in frame.winfo_children():
    widget.grid_configure(padx=2, pady=2)

window.mainloop()




# from tkinter import *
    
# window = Tk()
    
# file = open("user_gui.txt", "a+")
    
# def add():
#     file.write(user_value.get() + "\n")
#     entry.delete(0, END)
    
# def save():
#     global file
#     file.close()
#     file = open("user_gui.txt", "a+")
    
# def close():
#     file.close()
#     window.destroy()
    
# user_value = StringVar()
# entry = Entry(window, textvariable=user_value)
# entry.grid(row=0, column=0)
    
# button_add = Button(window, text="Add line", command=add)
# button_add.grid(row=0, column=1)
    
# button_save = Button(window, text="Save changes", command=save)
# button_save.grid(row=0, column=2)
    
# button_close = Button(window, text="Save and Close", command=close)
# button_close.grid(row=0,column=3)
    
# window.mainloop()