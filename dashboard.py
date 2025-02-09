import customtkinter as ctk
from tkinter import messagebox


class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.add_member = ctk.CTkButton(self, text="Add Member", command=self.add_member)
        self.add_member.pack(pady=20)

        self.view_member = ctk.CTkButton(self, text="View member", command=self.view_member)
        self.view_member.pack(pady=20)

        self.log_out = ctk.CTkButton(self, text="Log out", command=self.logout)
        self.log_out.pack(pady=20)

    def add_member(self):
        from ui.add_member import AddMemeber

        self.pack_forget()  # Hide the dashboard frame
        add_member_screen = AddMemeber(self.master)  # Show AddMember frame in the same window
        add_member_screen.pack(fill="both", expand=True)

    def view_member(self):
        from members import ViewMember
        self.pack_forget()
        view_member_screen = ViewMember(self.master)
        view_member_screen.pack(fill="both", expand=True)

    def logout(self):
        from ui.login import LoginApp
        self.pack_forget()
        LoginApp(self.master).pack(fill="both", expand=True)
