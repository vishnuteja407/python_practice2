from email import message
import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl
import sqlite3
import csv

def enter_data():
    accepted = accept_var.get()
    if accepted == 'Accepted':
        #User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = semesters_spinbox.get()


            print(f"First name: {firstname}, Last name: {lastname}")
            print(f"Title: {title}, Age: {age}, Nationality: {nationality}")
            print(f"# Courses: {numcourses}, # Semesters: {numsemesters}")
            print(f"Registration status: {registration_status}")
            print("-"*50)

            # Writing to xls file

            filepath = "/Users/vibodapa/Desktop/Ciscoapps/python/python_exercise/data.xlsx"

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["First Name", "Last Name", "Title", "Age", "Nationality", "# Courses", "# Semesters", "Registration status"]
                sheet.append(heading)
                workbook.save(filepath)

            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, title, age, nationality, numcourses,
                        numsemesters, registration_status])
            workbook.save(filepath)

            # Writing to csv file
            filepath_1 = "/Users/vibodapa/Desktop/Ciscoapps/python/python_exercise/student_data.csv"
            fields = ["First Name", "Last Name", "Title", "Age", "Nationality", "# Courses", "# Semesters", "Registration status"]
            dict_to_write = {"First Name":firstname, "Last Name":lastname, "Title":title, "Age":age, "Nationality":nationality,
                            "# Courses": numcourses, "# Semesters": numsemesters, "Registration status": registration_status}

            if not os.path.exists(filepath_1):
                with open(filepath_1, "a+") as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fields)  
                    writer.writeheader()
                    writer.writerow(dict_to_write)
            else:
                with open(filepath_1, "a+") as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fields) 
                    writer.writerow(dict_to_write)

            # Create a Table
            conn = sqlite3.connect('data.db')
            table_create_query = ''' CREATE TABLE IF NOT EXISTS Student_Data
                  (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                  registration_status TEXT, num_courses INT, num_semesters INT)
            '''
            conn.execute(table_create_query)

            #Insert Data
            data_insert_query = ''' INSERT INTO Student_Data(firstname, lastname, title,
            age, nationality, registration_status, num_courses, num_semesters) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            data_insert_tuple = (firstname, lastname, title,
            age, nationality, registration_status, numcourses, numsemesters)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            tkinter.messagebox.showwarning(title="Error", message="Firstname and Lastname are required")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditions")

window = tkinter.Tk()

window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text='User Information')
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=['Asia', 'Africa', 'Antarctica', 'Australia', 'Europe', 'North America', 'South America'])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info

course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(course_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(course_frame, text="Currently Registered", 
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

semesters_label = tkinter.Label(course_frame, text="# Semesters")
semesters_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
semesters_label.grid(row=0, column=2)
semesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not accepted")
terms_check.grid(row=0, column=0)

#Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()