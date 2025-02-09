import customtkinter as ctk
from tkinter import messagebox
from auth import login_agent
from ui.dashboard import Dashboard


class LoginApp(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Please login", font=("Arial", 20)).pack(pady=20)

        self.user_name = ctk.CTkEntry(self, placeholder_text="Username")
        self.user_name.pack(pady=20)

        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.pack(pady=20)

        ctk.CTkButton(self, text="login", command=self.authenticate).pack(pady=10)

    def authenticate(self):
        username = self.user_name.get()
        password = self.password.get()

        if login_agent(username, password):
            messagebox.showinfo("Login successful", "Welcome")
            self.pack_forget()
            dashboard = Dashboard(self.master)
            dashboard.pack(fill="both", expand=True)

        else:
            messagebox.showinfo("Login Failed", "Invalid credentials!")
