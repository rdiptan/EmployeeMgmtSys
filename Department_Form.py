from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle
import os
import EMS

d = {}


class Department:
    """
    this class provides a form to add new department data in the system and view them

    Methods:
        view()
        reset_btn()
        submit()
        back_btn()

    """
    def __init__(self, window):
        self.window = window
        self.window.title("Employee Management System")
        self.window.configure(background="sky blue")
        self.window.geometry("1366x768+0+0")

        self.dept_name_ent_val = StringVar()
        self.dept_id_ent_val = StringVar()

        self.title = Label(self.window, text="Department Registration Form\nABC Company", font=("arial", 20, "bold"),
                           fg="#ffffff", bg="gray")
        self.title.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.window)
        self.frame1.place(x=10, y=80)

        self.tab = ttk.Notebook(self.frame1)
        self.tab.configure(width=500, height=300)

        tab1 = ttk.Frame(self.tab)
        tab2 = ttk.Frame(self.tab)

        self.tab.add(tab1, text="ADD NEW DEPARTMENT")
        self.tab.add(tab2, text="VIEW DEPARTMENTS")

        self.tab.pack(expand=1, fill="both")

        # department code label
        self.dept_id = Label(tab1, text="Department Code", font=("arial", 12))
        self.dept_id.grid(row=1, column=0, padx=5, pady=5)
        # department code textbox
        self.dept_id_ent = Entry(tab1, font=("arial", 12), textvariable=self.dept_id_ent_val)
        self.dept_id_ent.grid(row=1, column=1, padx=5, pady=5)

        # department name label
        self.dept_name = Label(tab1, text="Department Name", font=("arial", 12))
        self.dept_name.grid(row=2, column=0, padx=5, pady=5)
        # department name textbox
        self.dept_name_ent = Entry(tab1, font=("arial", 12), textvariable=self.dept_name_ent_val)
        self.dept_name_ent.grid(row=2, column=1, padx=5, pady=5)

        # save button
        self.save = Button(tab1, text="SAVE", command=self.submit)
        self.save.grid(row=3, column=0, padx=5, pady=5)
        # reset button
        self.reset = Button(tab1, text="CLEAR", command=self.reset_btn)
        self.reset.grid(row=3, column=1, padx=5, pady=5)

        # back button
        self.back = Button(self.window, text="BACK", command=self.back_btn)
        self.back.place(x=10, y=425)

        # refresh button
        self.refresh = Button(tab2, text="Refresh", command=self.view)
        self.refresh.grid(row=0, column=0, padx=5, pady=5)

        self.item = Label(tab2, text="Department ID\tDepartment Name")
        self.item.grid(row=1, column=0, padx=5, pady=5)

        self.display = Text(tab2)
        self.display.grid(row=2, column=0, columnspan=24)
        self.view()

    def view(self):
        """view the saved department data"""
        le = os.path.getsize("/home/theodis/PycharmProjects/Assignment/Dept.txt")
        if le == 0:
            tkinter.messagebox.showerror("error", "File is empty")
        else:
            f = open("Dept.txt", "rb")
            d = pickle.load(f)
            data = ""
            for i, j in d.items():
                da = ""
                for k, l in j.items():
                    da = da + l + "\t" + "\t"
                data = data + da + "\n"
            self.display.insert(END, data)
            self.display.config(state=DISABLED)

    def reset_btn(self):
        """resets the input value to blank"""
        self.dept_id_ent.delete(0, END)
        self.dept_name_ent.delete(0, END)

    def submit(self):
        """
                verify if department code is taken or not
                check if any values is left empty or not
                saves the department data in a text file in pickled form

                """
        global d
        objs = []
        while 1:
            try:
                with open("Dept.txt", "rb") as f:
                    d = pickle.load(f)
                    for i, j in d.items():
                        objs.append(j["dept_id"])
            except EOFError:
                break
            finally:
                break
        exists = False
        for i in objs:
            if i == self.dept_id_ent_val.get():
                exists = True
                break
            else:
                exists = False

        if exists == True:
            tkinter.messagebox.showerror("Error", "Department ID occupied")

        elif self.dept_id_ent_val.get() is '' or self.dept_name_ent_val.get() is '':
            tkinter.messagebox.showerror("error", "enter all values")

        else:
            dept_id = self.dept_id_ent_val.get()
            dept_name = self.dept_name_ent_val.get()

            dict = {dept_id: {"dept_id": dept_id, "dept_name": dept_name}}

            le = os.path.getsize("/home/theodis/PycharmProjects/Assignment/Dept.txt")

            if le > 0:
                f = open("Dept.txt", "rb+")
                d = pickle.load(f)
                d.update(dict)
                f.seek(0)
                pickle.dump(d, f)
                tkinter.messagebox.showinfo("Success", "Saved successfully")
                f.close()

            else:
                f = open("Dept.txt", "wb")

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
    Department(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
