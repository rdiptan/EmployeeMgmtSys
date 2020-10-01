from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import Department_Form
import Employee_Management
import Login_User
import Register_User


class EMS:
    """
    Homepage for employee management system
    This class provides the different option to goes to
    employee, department, registration forms.

    Methods:
        emp_btn()
        dept_btn()
        signup_handler()
        logout_btn()

    """
    def __init__(self, window):
        self.window = window
        self.window.configure(background="sky blue")
        self.window.geometry("1366x768+0+0")

        # title name
        self.title = Label(self.window, text="Employee Management System\nABC Company", font=("arial", 20, "bold"),
                           fg="#ffffff", bg="gray")
        self.title.place(x=0, y=0, relwidth=1)

        # frames
        self.frame1 = LabelFrame(self.window, text="Employee Management System", padx=10, pady=10)
        self.frame1.place(x=600, y=100)
        self.frame1.configure(background="sky blue")

        self.frame2 = Frame(self.window)
        self.frame2.place(x=50, y=100)
        self.frame2.configure(background="sky blue")

        self.frame3 = LabelFrame(self.window, text="Add New Users", padx=10, pady=10)
        self.frame3.place(x=900, y=100)
        self.frame3.configure(background="sky blue")

        # loading image
        self.img = ImageTk.PhotoImage(Image.open("e3.png"))
        panel = Label(self.frame2, image=self.img)
        panel.pack(side="bottom", fill="both", expand="yes")

        # Employee button
        self.emp = Button(self.frame1, text="EMPLOYEE", font=("arial", 16), width=12, command=self.emp_btn)
        self.emp.grid(row=1, column=1, padx=25, pady=50)
        # Department button
        self.dept = Button(self.frame1, text="DEPARTMENT", font=("arial", 16), width=12, command=self.dept_btn)
        self.dept.grid(row=2, column=1, padx=25, pady=50)

        # register button
        self.register = Button(self.frame3, text="REGISTER", font=("arial", 16), command=self.signup_handler)
        self.register.grid(row=6, columnspan=2, padx=5, pady=50)

        # logout button
        self.dept = Button(self.window, text="LOGOUT", font=("arial", 16), activebackground="red",
                           activeforeground="#ffffff", command=self.logout_btn)
        self.dept.place(x=1111, y=110)

    def emp_btn(self):
        """opens employee management form"""
        self.window.withdraw()
        self.newwindow = Toplevel(self.window)
        Employee_Management.Management(self.newwindow)

    def dept_btn(self):
        """opens depertment management form"""
        self.window.withdraw()
        self.newwindow = Toplevel(self.window)
        Department_Form.Department(self.newwindow)

    def signup_handler(self):
        """open new user registration form"""
        self.window.withdraw()
        self.newwindow = Toplevel(self.window)
        Register_User.Register(self.newwindow)

    def logout_btn(self):
        """logout the current user"""
        a = tkinter.messagebox.askyesno("LOGOUT", "Are you sure you want to logout")
        if a == 1:
            self.window.withdraw()
            self.newwindow = Toplevel(self.window)
            Login_User.User(self.newwindow)


def main():
    wn = Tk()
    wn.title("Employee Management System")
    EMS(wn)
    wn.mainloop()


if __name__ == "__main__":
    main()
