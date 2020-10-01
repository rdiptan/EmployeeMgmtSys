from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import pickle
import os
import EMS

d = {}


class Register:
    """
    This class provides a form to register new users.

    Methods:
        reset()
        submit()
        back()

    """
    def __init__(self, window):
        self.window = window
        self.window.configure(background="sky blue")
        self.window.geometry("1366x768+0+0")

        # passing string variable
        self.id_ent_val = StringVar()
        self.fname_ent_val = StringVar()
        self.mname_ent_val = StringVar()
        self.lname_ent_val = StringVar()
        self.email_ent_val = StringVar()
        self.password_ent_val = StringVar()
        self.repassword_ent_val = StringVar()

        # title name
        self.title = Label(self.window, text="New User Register\nABC Company", font=("arial", 20, "bold"), fg="#ffffff",
                           bg="gray")
        self.title.place(x=0, y=0, relwidth=1)

        # frames
        self.frame1 = LabelFrame(self.window,text="Register new user", padx=20, pady=5)
        self.frame1.place(x=600, y=100)
        self.frame1.configure(background="sky blue")

        self.frame2 = LabelFrame(self.window)
        self.frame2.place(x=50, y=100)

        self.img = ImageTk.PhotoImage(Image.open("e7.png"))
        panel = Label(self.frame2, image=self.img)
        panel.pack(side="bottom", fill="both", expand="yes")

        # register criteria label
        self.title2 = Label(self.frame1, text="All fields are to be filled compulsorily except middle name that is "
                                              "optional.", font=("arial", 12), fg="#ffffff", bg="sky blue")
        self.title2.grid(row=0, columnspan=3, padx=5, pady=5)

        # User ID label
        self.id = Label(self.frame1, text="User ID", font=("arial", 18, "bold"), fg="#ffffff", bg="sky blue")
        self.id.grid(row=1, column=0, padx=5, pady=5)
        # User ID textbox
        self.id_ent = Entry(self.frame1, font=("arial", 18, "bold"), textvariable=self.id_ent_val)
        self.id_ent.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # first name label
        self.fname = Label(self.frame1, text="First Name", font=("arial", 18, "bold"), fg="#ffffff",
                           bg="sky blue")
        self.fname.grid(row=2, column=0, padx=5, pady=5)
        # first name textbox
        self.fname_ent = Entry(self.frame1, font=("arial", 18, "bold"), textvariable=self.fname_ent_val)
        self.fname_ent.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # middle name label
        self.mname = Label(self.frame1, text="Middle Name", font=("arial", 18, "bold"), fg="#ffffff",
                           bg="sky blue")
        self.mname.grid(row=3, column=0, padx=5, pady=5)
        # middle name textbox
        self.mname_ent = Entry(self.frame1, font=("arial", 18, "bold"), textvariable=self.mname_ent_val)
        self.mname_ent.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        # last name label
        self.lname = Label(self.frame1, text="Last Name", font=("arial", 18, "bold"), fg="#ffffff",
                           bg="sky blue")
        self.lname.grid(row=4, column=0, padx=5, pady=5)
        # last name textbox
        self.lname_ent = Entry(self.frame1, font=("arial", 18, "bold"), textvariable=self.lname_ent_val)
        self.lname_ent.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        # email label
        self.email = Label(self.frame1, text="Email", font=("arial", 18, "bold"), fg="#ffffff",
                           bg="sky blue")
        self.email.grid(row=5, column=0, padx=5, pady=5)
        # email textbox
        self.email_ent = Entry(self.frame1, font=("arial", 18, "bold"), textvariable=self.email_ent_val)
        self.email_ent.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        # password label
        self.password = Label(self.frame1, text="Password", font=("arial", 18, "bold"), fg="#ffffff", bg="sky blue")
        self.password.grid(row=6, column=0, padx=5, pady=5)
        self.repassword = Label(self.frame1, text="Re-Enter Password", font=("arial", 18, "bold"), fg="#ffffff",
                                bg="sky blue")
        self.repassword.grid(row=7, column=0, padx=5, pady=5)
        # password textbox
        self.password_ent = Entry(self.frame1, show='*', font=("arial", 18, "bold"), textvariable=self.password_ent_val)
        self.password_ent.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
        self.repassword_ent = Entry(self.frame1, show='*', font=("arial", 18, "bold"),
                                    textvariable=self.repassword_ent_val)
        self.repassword_ent.grid(row=7, column=1, columnspan=2, padx=5, pady=5)

        # save button
        self.save = Button(self.frame1, text="SAVE", font=("arial", 16), command=self.submit)
        self.save.grid(row=8, column=1, padx=5, pady=5)
        # reset button
        self.reset = Button(self.frame1, text="RESET", font=("arial", 16), command=self.reset)
        self.reset.grid(row=8, column=2, padx=5, pady=5)

        # back option label
        self.title2 = Label(self.frame1, text="Already have an account?", font=("arial", 20), fg="#ffffff",
                            bg="sky blue")
        self.title2.grid(row=9, columnspan=3, padx=5, pady=5)
        # back button
        self.back = Button(self.frame1, text="BACK", font=("arial", 16), command=self.back)
        self.back.grid(row=10, column=1, padx=5, pady=5)

    def reset(self):
        """resets the input values to blank"""
        self.id_ent.delete(0, END)
        self.fname_ent.delete(0, END)
        self.lname_ent.delete(0, END)
        self.mname_ent.delete(0, END)
        self.email_ent.delete(0, END)
        self.password_ent.delete(0, END)
        self.repassword_ent.delete(0, END)

    def submit(self):
        """
        verify if user id is taken or not
        check if any values is left empty or not
        check for password match
        saves the user registration data in a text file in pickled form

        """
        global d
        objs = []
        while 1:
            try:
                with open("reg.txt", "rb") as f:
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
            tkinter.messagebox.showerror("Error", "User ID occupied")
        elif self.id_ent_val.get() is '' or self.fname_ent_val.get() is '' or self.lname_ent_val.get() is '' or \
                self.email_ent_val.get() is '' or self.password_ent_val.get() is '' or self.repassword_ent_val.get() \
                is '':
            tkinter.messagebox.showerror("error", "enter all values")
        elif self.password_ent_val.get() != self.repassword_ent_val.get():
            tkinter.messagebox.showerror("error", "passwords does not match")
            return

        else:
            id = self.id_ent_val.get()
            fname = self.fname_ent_val.get()
            mname = self.mname_ent_val.get()
            lname = self.lname_ent_val.get()
            email = self.email_ent_val.get()
            password = self.password_ent_val.get()
            dict = {id: {"fname": fname, "mname": mname, "lname": lname, "email": email, "password": password}}

            le = os.path.getsize("/home/theodis/PycharmProjects/Assignment/reg.txt")

            if le > 0:
                f = open("reg.txt", "rb+")
                d = pickle.load(f)
                d.update(dict)
                f.seek(0)
                pickle.dump(d, f)
                a = tkinter.messagebox.showinfo("Success", "New user successfully added")
                self.window.withdraw()
                if a == "ok":
                    newwindow = Toplevel(self.window)
                    EMS.EMS(newwindow)

                f.close()

            else:
                f = open("reg.txt", "wb")
                d.update(dict)
                pickle.dump(d, f)

                tkinter.messagebox.showinfo("Success", "Saved successfully")
                f.close()

    def back(self):
        """takes back to employee management system homepage"""
        self.window.withdraw()
        self.newwindow = Toplevel(self.window)
        EMS.EMS(self.newwindow)


def main():
    wn = Tk()
    wn.title("Employee Management System")
    Register(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
