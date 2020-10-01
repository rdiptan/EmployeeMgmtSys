from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import pickle
import os
import EMS


class User:
    """
    This class provides login form to use the programme.

    Methods:
        show()
        reset_btn()
        verify()
        exit_handler()

    """

    def __init__(self, window):
        self.window = window
        self.window.configure(bg="sky blue")
        self.window.geometry("1366x768+0+0")

        self.usr_id_ent_val = StringVar()
        self.password_ent_val = StringVar()

        # title name
        self.title = Label(self.window, text="ABC Company\nWelcome to login page", font=("arial", 20, "bold"),
                           fg="#ffffff", bg="gray")
        self.title.place(x=0, y=0, relwidth=1)
        self.title2 = Label(self.window, text="You are accessing the portal of ABC Company, any misuse will be "
                                              "against company law. And addressed as Federal crime.\n", font=("arial",
                                                                                                              12,
                                                                                                              "bold"),
                            fg="#000000", bg="sky blue")
        self.title2.pack(side=BOTTOM)

        self.line = Canvas(self.window, width=1200, height=1, bg="#ffffff").pack(side=BOTTOM)

        # frame
        self.frame1 = LabelFrame(self.window, text="Login to continue", padx=5, pady=15)
        self.frame1.place(x=600, y=100)
        self.frame1.configure(bg="sky blue")

        self.frame2 = Frame(self.window)
        self.frame2.place(x=50, y=100)

        # photos
        self.img = ImageTk.PhotoImage(Image.open("ems.jpg"))
        panel = Label(self.frame2, image=self.img)
        panel.pack(side="bottom", fill="both", expand="yes")

        self.bg_uname = PhotoImage(file="u25.png")
        self.bg_pass = PhotoImage(file="p25.png")

        # user id label
        self.usr_id = Label(self.frame1, text="User ID", image=self.bg_uname, compound=LEFT, font=("arial", 18, "bold"),
                            fg="#000000", bg="sky blue")
        self.usr_id.grid(row=0, column=0, padx=5, pady=5)
        # user id textbox
        self.usr_id_ent = Entry(self.frame1, font=("arial", 18), textvariable=self.usr_id_ent_val)
        self.usr_id_ent.grid(row=0, column=1, padx=5, pady=5)
        self.usr_id_ent.focus()

        # password label
        self.password = Label(self.frame1, text="Password", image=self.bg_pass, compound=LEFT,
                              font=("arial", 18, "bold"), fg="#000000", bg="sky blue")
        self.password.grid(row=1, column=0, padx=5, pady=5)
        # password textbox
        self.password_ent = Entry(self.frame1, font=("arial", 18), textvariable=self.password_ent_val)
        self.password_ent.default_show_val = self.password_ent["show"]
        self.password_ent["show"] = "*"
        self.password_ent.grid(row=1, column=1, padx=5, pady=5)

        # checkbutton
        self.check = IntVar()
        self.pa = Checkbutton(self.frame1, bg="#ffffff", variable=self.check, command=self.show)
        self.pa.place(x=400, y=55)

        # login button
        self.login = Button(self.frame1, text="LOGIN", font=("arial", 16), command=self.verify)
        self.login.grid(row=2, columnspan=2, padx=5, pady=5)

        # reset button
        self.reset = Button(self.frame1, text="RESET", font=("arial", 16), command=self.reset_btn)
        self.reset.grid(row=2, column=1, padx=5, pady=5, sticky=E)

        # register option label
        self.title2 = Label(self.frame1, text="If you don't have a account to proceed\nyou can consider with your "
                                              "higher authorities for registration.", font=("arial", 12),
                            fg="#000000", bg="sky blue")
        self.title2.grid(row=3, columnspan=2, padx=5, pady=5)

        # quit button
        self.exit = Button(self.window, text="EXIT", activebackground="red", activeforeground="white",
                           font=("arial", 16), command=self.exit_handler)
        self.exit.place(x=970, y=345)

    def show(self):
        """shows the password if checkbutton is clicked"""
        if self.check.get() == 0:
            self.password_ent["show"] = "*"
        else:
            self.password_ent["show"] = ""

    def reset_btn(self):
        """resets the input values to blank"""
        self.usr_id_ent.delete(0, END)
        self.password_ent.delete(0, END)

    def verify(self):
        """check for if input fields are empty or not then verify the user id and password
        and then logged into the system and also checks if registered user file is empty or not"""
        le = os.path.getsize("/home/theodis/PycharmProjects/Assignment/reg.txt")
        if self.usr_id_ent_val.get() is "" or self.password_ent_val.get() is "":
            tkinter.messagebox.showerror("error", "enter all values")

        elif le > 0:
            f = open("reg.txt", "rb+")
            ld = pickle.load(f)
            for i, j in ld.items():
                if i == self.usr_id_ent_val.get() and j["password"] == self.password_ent_val.get():
                    # a = tkinter.messagebox.showinfo("Success", "Login Success")
                    self.window.withdraw()
                    # if a == "ok":
                    self.newwindow = Toplevel(self.window)
                    EMS.EMS(self.newwindow)

                    f.close()
                    return
            else:
                tkinter.messagebox.showerror("Error", "Account doesn't exist\nIf you forget your id or password "
                                                      "please contact your higher authorities")
                f.close()
        else:
            tkinter.messagebox.showerror("Error", "File is Empty")

    def exit_handler(self):
        """quit the program"""
        a = tkinter.messagebox.askyesno("EXIT", "Are you sure you want to exit")
        if a == 1:
            self.window.quit()


def main():
    wn = Tk()
    wn.title("Employee Management System")
    User(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()

