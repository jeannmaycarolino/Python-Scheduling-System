import tkinter as tk
from tkinter import messagebox

class UILogin:
    def __init__(self, main):
        self.main = main
        self.loginFrame = tk.Tk()

        # Frame
        self.loginFrame.title("Patient Appointment Scheduling System")
        self.loginFrame.geometry("1366x768")
        self.loginFrame.resizable(False, False)
        self.loginFrame.iconbitmap("images/logo.ico")
        self.loginFrame.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Logo
        self.icon = tk.PhotoImage(file="images/logo.png")
        self.icon2 = tk.PhotoImage(file="images/bgImage.jpg")
        self.scaledicon2 = self.icon2.subsample(2)
        self.logo = self.icon.subsample(2)

        # Labels for Image
        self.bgImageLabel = tk.Label(self.loginFrame, image=self.scaledicon2)
        self.bgImageLabel.place(x=0, y=-25)

        # Panels for prompting
        self.loginBox = tk.Frame(self.loginFrame, width=500, height=600, bg="white")
        self.loginBox.place(x=700, y=50)

        # Labels for Text
        self.title = tk.Label(self.loginFrame, text="Patient Appointment", font=("Dialog", 30, "bold"), fg="black")
        self.title.place(x=250, y=300)
        self.title2 = tk.Label(self.loginFrame, text="Scheduling System", font=("Dialog", 24, "bold"), fg="black")
        self.title2.place(x=250, y=340)
        self.logoLabel = tk.Label(self.loginFrame, image=self.logo)
        self.logoLabel.place(x=180, y=300)
        self.logotext = tk.Label(self.loginFrame, text="Sign in or create an account", font=("Dialog", 18), fg="black")
        self.logotext.place(x=250, y=385)
        self.signInText = tk.Label(self.loginFrame, text="Sign in", font=("Dialog", 36, "bold"), fg="black")
        self.signInText.place(x=750, y=100)

        # Text Fields for Username and Password
        self.username = tk.Entry(self.loginFrame, font=("Dialog", 18), fg="black", bg="white")
        self.username.place(x=750, y=200)
        self.usernameLabel = tk.Label(self.loginFrame, text="Username", font=("Dialog", 18), fg="gray")
        self.usernameLabel.place(x=750, y=180)
        self.password = tk.Entry(self.loginFrame, font=("Dialog", 18), fg="black", bg="white", show="*")
        self.password.place(x=750, y=280)
        self.passwordLabel = tk.Label(self.loginFrame, text="Password", font=("Dialog", 18), fg="gray")
        self.passwordLabel.place(x=750, y=260)

        # Buttons for Login and Create Account
        self.loginButton = tk.Button(self.loginFrame, text="Login", font=("Dialog", 18, "bold"), fg="white", bg="blue",
                                     command=self.login)
        self.loginButton.place(x=750, y=340)
        self.createAccountButton = tk.Button(self.loginFrame, text="Create Account", font=("Dialog", 18, "bold"),
                                             fg="white", bg="#40ab28", command=self.create_account)
        self.createAccountButton.place(x=750, y=465)
        self.createAccountLabel = tk.Label(self.loginFrame,
                                           text="Don't have saved information? Create an account.",
                                           font=("Sans Serif", 14), fg="black")
        self.createAccountLabel.place(x=790, y=520)

        self.loginFrame.mainloop()

    def login(self):
        success_icon = tk.PhotoImage(file="images/success.png")
        wrong_icon = tk.PhotoImage(file="images/wrong.png")
        self.loginButton.config(state=tk.DISABLED)

        username2 = self.username.get()
        password2 = self.password.get()

        if username2 == "admin" and password2 == "admin":
            messagebox.showinfo("Patient Appointment Scheduling System", "Administrator Login Successful!",
                                icon=success_icon)
            self.loginFrame.destroy()
            # Perform admin-related actions
        else:
            validation = self.main.login_Account(username2, password2)
            if validation:
                messagebox.showinfo("Patient Appointment Scheduling System", "Login Successful!", icon=success_icon)
                self.loginFrame.destroy()
                # Perform user-related actions
            else:
                messagebox.showerror("Patient Appointment Scheduling System", "Username or Password is incorrect!",
                                     icon=wrong_icon)
                self.loginButton.config(state=tk.NORMAL)

    def create_account(self):
        self.createAccountButton.config(state=tk.DISABLED)
        self.loginFrame.destroy()
        # Open create account window

    def on_closing(self):
        self.main.save()
        self.loginFrame.destroy()

# Usage
if __name__ == "__main__":
    main = None  # Replace with your Main class instance
    UILogin(main)
