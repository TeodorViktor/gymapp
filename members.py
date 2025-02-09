import customtkinter as ctk
import sqlite3


class ViewMember(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)  # Accept `master` and initialize the parent class
        self.master = master
        self.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        self.member_name = ctk.CTkEntry(self, placeholder_text="Enter Member's Name")
        self.member_name.pack(pady=20)

        self.member_id = ctk.CTkEntry(self, placeholder_text="ID")  # Renamed from `id` to `member_id`
        self.member_id.pack(pady=20)

        self.view_membership_button = ctk.CTkButton(self, text="View Membership", command=self.view_membership)
        self.view_membership_button.pack(pady=20)

        self.back_to_dashboard_button = ctk.CTkButton(self, text="Back to Dashboard", command=self.back_to_dashboard)
        self.back_to_dashboard_button.pack(pady=20)

    def view_membership(self):
        membername = self.member_name.get()
        try:
            member_id = int(self.member_id.get())  # Convert ID to integer
        except ValueError:
            print("Invalid ID format")
            return

        con = sqlite3.connect("gym.db")
        cur = con.cursor()
        cur.execute("SELECT membership_expiry FROM members WHERE name=? AND id=?", (membername, member_id))
        result = cur.fetchone()

        if result:
            self.expire_date = result[0]
            print("Membership Expiry:", self.expire_date)
        else:
            print("Member not found.")

        con.close()

    def back_to_dashboard(self):
        from ui.dashboard import Dashboard
        self.pack_forget()  # Hide this frame
        dashboard = Dashboard(self.master)  # Show Dashboard frame
        dashboard.pack(fill="both", expand=True)
