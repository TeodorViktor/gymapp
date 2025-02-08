import customtkinter as ctk
from datetime import datetime, timedelta
import sqlite3


class ViewMember(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("View Member")
        self.geometry("1000x800+400+100")
        self.member_name = ctk.CTkEntry(self, placeholder_text="Enter Member's Name")
        self.member_name.pack(pady=20)

        self.id = ctk.CTkEntry(self, placeholder_text="ID")
        self.id.pack(pady=20)

        self.view_memership = ctk.CTkButton(self, text="view Membership", command=self.view_membership)
        self.view_memership.pack(pady=20)

        self.back_todashboard = ctk.CTkButton(self, text="Back to Dashboard", command=self.back_todashboard)
        self.back_todashboard.pack(pady=20)

    def view_membership(self):
        membername = self.member_name.get()
        id = self.id.get()
        con = sqlite3.connect("gym.db")
        cur = con.cursor()
        cur.execute("SELECT membership_expiry FROM members WHERE name=? AND id =?", (membername, id,))
        result = cur.fetchone()
        self.expire_date = result[0]
        print(self.expire_date)
        con.commit()
        con.close()

    def back_todashboard(self):
        self.destroy()
        from ui.dashboard import Dashboard
        dashboard = Dashboard(self.master)
        dashboard.mainloop()