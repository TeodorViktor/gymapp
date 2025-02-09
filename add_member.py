import customtkinter as ctk
from datetime import datetime, timedelta
import sqlite3
from tkinter import messagebox

class AddMemeber(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.member_name = ctk.CTkEntry(self, placeholder_text="Member Name")
        self.member_name.pack(pady=20)

        self.member_birthday = ctk.CTkEntry(self, placeholder_text="Birthday (YYYY-MM-DD)")
        self.member_birthday.pack(pady=20)

        self.confirm_membership = ctk.CTkButton(self, text="Confirm Membership", command=self.confirm_membership)
        self.confirm_membership.pack(pady=20)
        self.success_label = ctk.CTkLabel(self, text="", text_color="green", height=0)  # Initially empty
        self.success_label.pack(pady=0)
        self.back_todashboard = ctk.CTkButton(self, text="Back to Dashboard", command=self.back_to_dashboard)
        self.back_todashboard.pack(pady=20)

    def confirm_membership(self):
        today = datetime.today().date()
        user_birthday = datetime.strptime(self.member_birthday.get(), "%Y-%m-%d").date()
        age = today.year - user_birthday.year

        expiry_date = datetime.now() + timedelta(days=30)

        con = sqlite3.connect("gym.db")
        cur = con.cursor()
        cur.execute("INSERT INTO members (name, age, membership_expiry) VALUES (?, ?, ?)",
                    (self.member_name.get(), age, expiry_date))
        con.commit()
        con.close()
        self.success_label.configure(height=5, pady=10)
        self.success_label.configure(text="✅ Member registered successfully!", text_color="green")

    def back_to_dashboard(self):
        from ui.dashboard import Dashboard  # ✅ Corrected Import

        self.pack_forget()  # Hide this frame
        dashboard = Dashboard(self.master)  # Show the dashboard again
        dashboard.pack(fill="both", expand=True)
