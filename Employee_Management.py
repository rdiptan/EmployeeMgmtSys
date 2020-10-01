from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle
import os
import EMS

d = {}


class Management:
    """
    this class provides a form to add new employee data in the system and view them

    Methods:
        box()
        view()
        reset()
        submit()
        back_btn()

    """

    def __init__(self, window):
        self.window = window
        self.window.title("Employee Management System")
        self.window.configure(background="sky blue")
        self.window.geometry("1366x768+0+0")

        # title name
        self.title = Label(self.window, text="Employee Management Form\nABC Company", font=("arial", 20, "bold"),
                           fg="#ffffff", bg="gray")
        self.title.place(x=0, y=0, relwidth=1)

        # frames
        self.frame1 = Frame(self.window)
        self.frame1.place(x=10, y=80)
        self.frame1.configure(background="sky blue")

        self.tab = ttk.Notebook(self.frame1)
        self.tab.configure(width=1150, height=550)

        tab1 = ttk.Frame(self.tab)
        tab2 = ttk.Frame(self.tab)

        self.tab.add(tab1, text="ADD NEW EMPLOYEE")
        self.tab.add(tab2, text="VIEW EMPLOYEE")

        self.tab.pack(expand=1, fill="both")

        # register criteria label
        self.title2 = Label(tab1, text="All fields are to be filled compulsorily except middle name that is optional.",
                            font=("arial", 12), fg="#000000")
        self.title2.grid(row=0, columnspan=3, padx=5, pady=5)

        # employee ID label
        self.id = Label(tab1, text="Employee ID", font=("arial", 18, "bold"))
        self.id.grid(row=1, column=0, padx=5, pady=5)
        # Employee ID textbox
        self.id_ent = Entry(tab1, font=("arial", 18))
        self.id_ent.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # first name label
        self.fname = Label(tab1, text="Employee First Name", font=("arial", 18, "bold"))
        self.fname.grid(row=2, column=0, padx=5, pady=5)
        # first name textbox
        self.fname_ent = Entry(tab1, font=("arial", 18))
        self.fname_ent.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # middle name label
        self.mname = Label(tab1, text="Employee Middle Name", font=("arial", 18, "bold"))
        self.mname.grid(row=3, column=0, padx=5, pady=5)
        # middle name textbox
        self.mname_ent = Entry(tab1, font=("arial", 18))
        self.mname_ent.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        # last name label
        self.lname = Label(tab1, text="Employee Last Name", font=("arial", 18, "bold"))
        self.lname.grid(row=4, column=0, padx=5, pady=5)
        # last name textbox
        self.lname_ent = Entry(tab1, font=("arial", 18))
        self.lname_ent.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        # DOB label
        self.dob = Label(tab1, text="Date of Birth (yyyy-mm-dd)", font=("arial", 18, "bold"))
        self.dob.grid(row=5, column=0, padx=5, pady=5)
        # DOB textbox
        self.dob_ent = Entry(tab1, font=("arial", 18))
        self.dob_ent.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        # nationality label
        self.nat = Label(tab1, text="Nationality", font=("arial", 18, "bold"))
        self.nat.grid(row=6, column=0, padx=5, pady=5)
        # nationality textbox
        self.nat_ent = Entry(tab1, font=("arial", 18))
        self.nat_ent.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

        # gender label
        self.gender = Label(tab1, text="Gender", font=("arial", 18, "bold"))
        self.gender.grid(row=7, column=0, padx=5, pady=5)
        # gender buttons
        self.gender_value = StringVar()
        self.gender_ent1 = Radiobutton(tab1, text="Male", variable=self.gender_value, value="Male",
                                       font=("arial", 18))
        self.gender_ent1.grid(row=7, column=1)
        self.gender_ent2 = Radiobutton(tab1, text="Female", variable=self.gender_value, value="Female",
                                       font=("arial", 18))
        self.gender_ent2.grid(row=7, column=2)
        self.gender_ent3 = Radiobutton(tab1, text="Others", variable=self.gender_value, value="Others",
                                       font=("arial", 18))
        self.gender_ent3.grid(row=7, column=3)

        # contact label
        self.contact = Label(tab1, text="Contact", font=("arial", 18, "bold"))
        self.contact.grid(row=8, column=0, padx=5, pady=5)
        # contact textbox
        self.contact_ent = Entry(tab1, font=("arial", 18))
        self.contact_ent.grid(row=8, column=1, columnspan=2, padx=5, pady=5)

        # email label
        self.email = Label(tab1, text="Email", font=("arial", 18, "bold"))
        self.email.grid(row=9, column=0, padx=5, pady=5)
        # email textbox
        self.email_ent = Entry(tab1, font=("arial", 18))
        self.email_ent.grid(row=9, column=1, columnspan=2, padx=5, pady=5)

        # address label
        self.add = Label(tab1, text="Address", font=("arial", 18, "bold"))
        self.add.grid(row=10, column=0, padx=5, pady=5)
        # address textbox
        self.add_ent = Entry(tab1, font=("arial", 18))
        self.add_ent.grid(row=10, column=1, columnspan=2, padx=5, pady=5)

        # department label
        self.dept = Label(tab1, text="Department", font=("arial", 18, "bold"))
        self.dept.grid(row=11, column=0, padx=5, pady=5)
        # department textbox
        val1 = self.box()
        self.dept_ent = ttk.Combobox(tab1, font=("arial", 18), width=19, state="readonly", values=val1)
        self.dept_ent.grid(row=11, column=1, columnspan=2, padx=5, pady=5)

        # save button
        self.save = Button(tab1, text="SAVE", command=self.submit)
        self.save.grid(row=12, column=1, padx=5, pady=5)
        # reset button
        self.reset = Button(tab1, text="CLEAR", command=self.reset)
        self.reset.grid(row=12, column=2, padx=5, pady=5)

        # back button
        self.back = Button(self.window, text="BACK", command=self.back_btn)
        self.back.place(x=10, y=675)

        # refresh button
        self.refresh = Button(tab2, text="Refresh", command=self.view)
        self.refresh.grid(row=0, column=0, padx=5, pady=5)

        self.display = Text(tab2)
        self.display.grid(row=1, column=0, columnspan=24)
        self.view()

    def box(self):
        """returns the department data to combobox"""
        a = []
        f = open("Dept.txt", "rb")
        d = pickle.load(f)
        for i, j in d.items():
            a.append(j["dept_name"])
        return a

    def view(self):
        """view the saved employee data"""
        le = os.path.getsize("/home/theodis/PycharmProjects/Assignment/emp.txt")
        if le == 0:
            tkinter.messagebox.showerror("error", "File is empty")
        else:
            f = open("emp.txt", "rb")
            d = pickle.load(f)
            data = ""
            for i, j in d.items():
                da = ""
                for k, l in j.items():
                    da = da + k + " " + ":" + " " + l + "\n"
                data = data + da + "\n"
            self.display.insert(END, data)
            self.display.config(state=DISABLED)

    def reset(self):
        """resets the input value to blank"""
        self.id_ent.delete(0, END)
        self.fname_ent.delete(0, END)
        self.mname_ent.delete(0, END)
        self.lname_ent.delete(0, END)
        self.dob_ent.delete(0, END)
        self.contact_ent.delete(0, END)
        self.email_ent.delete(0, END)
        self.add_ent.delete(0, END)
        self.gender_value.set("")

    def submit(self):
        """
                verify if employee id is taken or not
                check if any values is left empty or not
                saves the employee data in a text file in pickled form

                """
        global d
        objs = []
        while 1:
            try:
                with open("emp.txt", "rb") as f:
                    objs.append(pickle.load(f))
            except EOFError:
                break
            finally:
                break
        exists = False
        for i in objs:
            for j in i:
                if j == self.id_ent.get():
                    exists = True
                    break
                else:
                    exists = False

        if exists == True:
            tkinter.messagebox.showerror("Error", "Employee ID occupied")

        elif self.id_ent.get() is '' or self.fname_ent.get() is '' or self.lname_ent.get() is '' \
                or self.dob_ent.get() is '' or self.nat_ent.get() is '' or self.gender_value.get() is '' \
                or self.contact_ent.get() is '' or self.email_ent.get() is '' or self.add_ent.get() is '' or\
                self.dept_ent.get() is '':
            tkinter.messagebox.showerror("error", "enter all values")

        else:
            id = self.id_ent.get()
            fname = self.fname_ent.get()
            mname = self.mname_ent.get()
            lname = self.lname_ent.get()
            dob = self.dob_ent.get()
            nationality = self.nat_ent.get()
            gender = self.gender_value.get()
            contact = self.contact_ent.get()
            email = self.email_ent.get()
            address = self.add_ent.get()
            department = self.dept_ent.get()

            dict = {
                id: {"ID": id, "First Name": fname, "Middle Name": mname, "Last Name": lname, "Date of Birth": dob,
                     "Nationality": nationality, "Gender": gender, "Contact": contact, "Email": email,
                     "Address": address, "Department": department}}

            le = os.path.getsize("/home/theodis/PycharmProjects/Assignment/emp.txt")

            if le > 0:
                f = open("emp.txt", "rb+")
                d = pickle.load(f)
                d.update(dict)
                f.seek(0)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo("Success", "Saved successfully")
                f.close()

            else:
                f = open("emp.txt", "wb")
                d.update(dict)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo("Success", "Saved successfully")
                f.close()

    def back_btn(self):
        self.window.withdraw()
        self.newwindow = Toplevel(self.window)
        EMS.EMS(self.newwindow)


def main():
    wn = Tk()
    Management(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
